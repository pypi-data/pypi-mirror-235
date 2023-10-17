import asyncio
import itertools

import aiohttp
import requests
import ujson

from typing import Optional, Dict
from requests.sessions import HTTPAdapter
from urllib3.util.retry import Retry
from collections import OrderedDict

from fxsdk.x.cosmos.tx.v1beta1.service_pb2 import BroadcastMode, BROADCAST_MODE_SYNC, BROADCAST_MODE_ASYNC, \
    BROADCAST_MODE_BLOCK
from fxsdk.x.cosmos.tx.v1beta1.tx_pb2 import Tx, TxRaw

requests.models.json = ujson


def _get_headers():
    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }


class RPCException(Exception):
    def __init__(self, response):
        self.code = 0
        try:
            json_res = ujson.loads(response.content)
        except ValueError:
            self.message = 'Invalid JSON error message from Binance Chain: {}'.format(response.text)
        else:
            self.code = json_res['error']['code']
            self.message = json_res['error']['message']
        self.status_code = response.status_code
        self.response = response
        self.request = getattr(response, 'request', None)

    def __str__(self):  # pragma: no cover
        return f'RPCError(code={self.code}): {self.message}'


class RpcRequest:

    def __init__(self, method, req_id, params=None):
        self._method = method
        self._params = params
        self._id = req_id

    @staticmethod
    def _sort_request(request):
        sort_order = ["jsonrpc", "method", "params", "id"]
        return OrderedDict(sorted(request.items(), key=lambda k: sort_order.index(k[0])))

    def __str__(self):
        request = {
            'jsonrpc': '2.0',
            'method': self._method,
            'id': self._id
        }

        if self._params:
            request['params'] = self._params

        return ujson.dumps(self._sort_request(request), ensure_ascii=False)


class BaseRpcClient:
    id_generator = itertools.count(1)

    def __init__(self, endpoint_url, requests_params: Optional[Dict] = None):
        self._endpoint_url = endpoint_url
        self._requests_params = requests_params

        self.session = self._init_session()

    @staticmethod
    def _init_session():
        session = requests.session()
        session.headers.update(_get_headers())
        return session

    def _get_rpc_request(self, path, **kwargs) -> str:
        rpc_request = RpcRequest(path, next(self.id_generator), kwargs.get('data', None))
        return str(rpc_request)

    def request_kwargs(self, method, **kwargs):
        # set default requests timeout
        kwargs['timeout'] = 10

        # add our global requests params
        if self._requests_params:
            kwargs.update(self._requests_params)

        kwargs['data'] = kwargs.get('data', {})
        kwargs['headers'] = kwargs.get('headers', {})

        if kwargs['data'] and method == 'get':
            kwargs['params'] = kwargs['data']
            del (kwargs['data'])

        if method == 'post':
            kwargs['headers']['content-type'] = 'text/plain'

        return kwargs


class HttpRpcClient(BaseRpcClient):
    __doc__ = """
    https://docs.cometbft.com/main/rpc/
    """

    def __init__(self, endpoint_url, requests_params: Optional[Dict] = None, max_retries=3):
        super(HttpRpcClient, self).__init__(endpoint_url, requests_params)
        if max_retries:
            retries = Retry(total=max_retries,
                            backoff_factor=.5,
                            status_forcelist=[500, 502, 503, 504])
            self.session.mount('http://', HTTPAdapter(max_retries=retries))

    def _request(self, path, **kwargs):
        rpc_request = self._get_rpc_request(path, **kwargs)
        response = self.session.post(self._endpoint_url, data=rpc_request.encode(), headers=_get_headers())
        return self._handle_response(response)

    def _request_session(self, path, params=None):
        kwargs = {
            'params': params,
            'headers': _get_headers()
        }

        response = self.session.get(f"{self._endpoint_url}/{path}", **kwargs)

        return self._handle_session_response(response)

    @staticmethod
    def _handle_response(response):
        try:
            res = response.json()

            if 'error' in res and res['error']:
                raise RPCException(response)

            # by default return full response
            # if it's a normal response we have a data attribute, return that
            if 'result' in res:
                res = res['result']
            return res
        except ValueError:
            raise RPCException('Invalid Response: %s' % response.text)

    @staticmethod
    def _handle_session_response(response):
        if not str(response.status_code).startswith('2'):
            raise RPCException(response)
        try:
            res = response.json()

            if 'code' in res and res['code'] != "200000":
                raise RPCException(response)

            if 'success' in res and not res['success']:
                raise RPCException(response)

            # by default return full response
            # if it's a normal response we have a data attribute, return that
            if 'result' in res:
                res = res['result']
            return res
        except ValueError:
            raise Exception('Invalid Response: %s' % response.text)

    def get_path_list(self):
        res = self._request(self._endpoint_url, method="get")
        return res.content

    def get_abci_info(self):
        return self._request('abci_info')

    def get_consensus_state(self):
        return self._request('consensus_state')

    def dump_consensus_state(self):
        return self._request('dump_consensus_state')

    def get_genesis(self):
        return self._request('genesis')

    def get_net_info(self):
        return self._request('net_info')

    def get_num_unconfirmed_txs(self):
        return self._request('num_unconfirmed_txs')

    def get_unconfirmed_txs(self):
        return self._request('unconfirmed_txs')

    def get_status(self):
        return self._request('status')

    def get_health(self):
        return self._request('health')

    def get_validators(self, height: int, page: int = 1):
        data = {
            'height': str(height),
            'page': str(page),
            'per_page': '30'
        }
        return self._request('validators', data=data)

    def get_consensus_params(self, height: Optional[int] = None):
        data = {
            'height': str(height) if height else None
        }

        return self._request('consensus_params', data=data)

    def abci_query(self, data: str,
                   path: Optional[str] = None,
                   prove: Optional[bool] = None,
                   height: Optional[int] = None):
        data = {
            'data': data
        }
        if path:
            data['path'] = path
        if prove:
            data['prove'] = str(prove)
        if height:
            data['height'] = str(height)

        return self._request('abci_query', data=data)

    def get_block_header(self, height: Optional[int] = None):
        data = {
            'height': str(height) if height else None
        }

        return self._request('header', data=data)

    def get_block(self, height: Optional[int] = None):
        data = {
            'height': str(height) if height else None
        }

        return self._request('block', data=data)

    def block_search(self, query: str, prove: Optional[bool] = None,
                     page: Optional[int] = None, per_page: Optional[int] = None,
                     order_by: Optional[str] = None):
        data = {
            'query': query
        }
        if prove:
            data['prove'] = str(prove)
        if page:
            data['page'] = str(page)
        if per_page:
            data['per_page'] = str(per_page)
        if order_by:
            data['order_by'] = order_by

        return self._request('block_search', data=data)

    def get_block_results(self, height: int):
        data = {
            'height': str(height)
        }

        return self._request('block_results', data=data)

    def get_block_commit(self, height: int):
        data = {
            'height': str(height)
        }

        return self._request('commit', data=data)

    def get_blockchain_info(self, min_height: int, max_height: int):
        assert max_height > min_height

        data = {
            'minHeight': str(min_height),
            'maxHeight': str(max_height)
        }

        return self._request('blockchain', data=data)

    def check_tx(self, tx: Tx):
        tx_raw = TxRaw(body_bytes=tx.body.SerializeToString(),
                       auth_info_bytes=tx.auth_info.SerializeToString(),
                       signatures=tx.signatures)
        tx_bytes = tx_raw.SerializeToString()
        data = {
            'tx': '0x' + tx_bytes.hex(),
        }

        return self._request('check_tx', data=data)

    def broadcast_tx(self, tx: Tx, mode: BroadcastMode = BROADCAST_MODE_SYNC):
        tx_raw = TxRaw(body_bytes=tx.body.SerializeToString(),
                       auth_info_bytes=tx.auth_info.SerializeToString(),
                       signatures=tx.signatures)
        tx_bytes = tx_raw.SerializeToString()
        data = {
            'tx': '0x' + tx_bytes.hex(),
        }
        if mode == BROADCAST_MODE_SYNC:
            return self._broadcast_tx_sync(data)
        elif mode == BROADCAST_MODE_ASYNC:
            return self._broadcast_tx_async(data)
        elif mode == BROADCAST_MODE_BLOCK:
            return self._broadcast_tx_commit(data)

    def _broadcast_tx_async(self, tx_data: Dict):
        return self._request_session("broadcast_tx_async", params=tx_data)

    def _broadcast_tx_commit(self, tx_data: Dict):
        return self._request_session("broadcast_tx_commit", params=tx_data)

    def _broadcast_tx_sync(self, tx_data: Dict):
        return self._request_session("broadcast_tx_sync", params=tx_data)

    def get_tx(self, tx_hash: str, prove: Optional[bool] = None):
        data = {
            'hash': tx_hash
        }
        if prove:
            data['prove'] = str(prove)

        return self._request('tx', data=data)

    def tx_search(self, query: str, prove: Optional[bool] = None,
                  page: Optional[int] = None, per_page: Optional[int] = None,
                  order_by: Optional[str] = None):
        data = {
            'query': query
        }
        if prove:
            data['prove'] = str(prove)
        if page:
            data['page'] = str(page)
        if per_page:
            data['per_page'] = str(per_page)
        if order_by:
            data['order_by'] = order_by

        return self._request('tx_search', data=data)


class AsyncHttpRpcClient(BaseRpcClient):
    __doc__ = HttpRpcClient.__doc__

    @classmethod
    async def create(cls, endpoint_url):
        return AsyncHttpRpcClient(endpoint_url)

    def _init_session(self, **kwargs):
        loop = kwargs.get('loop', asyncio.get_event_loop())
        session = aiohttp.ClientSession(
            loop=loop,
            headers=_get_headers(),
            json_serialize=ujson.dumps
        )
        return session

    async def _request(self, path, **kwargs):
        rpc_request = self._get_rpc_request(path, **kwargs)
        response = await self.session.post(self._endpoint_url, data=rpc_request.encode(), headers=_get_headers())
        return await self._handle_response(response)

    async def _request_session(self, path, params=None):
        kwargs = {
            'params': params,
            'headers': _get_headers()
        }
        response = await self.session.get(f"{self._endpoint_url}/{path}", **kwargs)
        return await self._handle_session_response(response)

    @staticmethod
    async def _handle_response(response):
        try:
            res = await response.json()

            if 'error' in res and res['error']:
                raise RPCException(response)

            # by default return full response
            # if it's a normal response we have a data attribute, return that
            if 'result' in res:
                res = res['result']
            return res
        except ValueError:
            raise Exception('Invalid Response: %s' % response.text)

    @staticmethod
    async def _handle_session_response(response):
        if not str(response.status).startswith('2'):
            raise RPCException(response)
        try:
            res = await response.json()

            if 'code' in res and res['code'] != "200000":
                raise RPCException(response)

            if 'success' in res and not res['success']:
                raise RPCException(response)

            # by default return full response
            # if it's a normal response we have a data attribute, return that
            if 'result' in res:
                res = res['result']
            return res
        except ValueError:
            raise Exception('Invalid Response: %s' % await response.text())

    async def get_path_list(self):
        res = await self.session.get(self._endpoint_url)
        return await res.text()

    async def get_abci_info(self):
        return await self._request('abci_info')

    async def get_consensus_state(self):
        return await self._request('consensus_state')

    async def dump_consensus_state(self):
        return await self._request('dump_consensus_state')

    async def get_genesis(self):
        return await self._request('genesis')

    async def get_net_info(self):
        return await self._request('net_info')

    async def get_num_unconfirmed_txs(self):
        return await self._request('num_unconfirmed_txs')

    async def get_status(self):
        return await self._request('status')

    async def get_health(self):
        return await self._request('health')

    async def get_unconfirmed_txs(self):
        return await self._request('unconfirmed_txs')

    async def get_validators(self, height: int, page: int = 1):
        data = {
            'height': str(height),
            'page': str(page),
            'per_page': '30'
        }
        return await self._request('validators', data=data)

    async def abci_query(self, data: str, path: Optional[str] = None,
                         prove: Optional[bool] = None, height: Optional[int] = None):
        data = {
            'data': data
        }
        if path:
            data['path'] = path
        if prove:
            data['prove'] = str(prove)
        if height:
            data['height'] = str(height)

        return await self._request('abci_query', data=data)

    async def get_block_header(self, height: Optional[int] = None):
        data = {
            'height': str(height) if height else None
        }
        return await self._request('header', data=data)

    async def get_block(self, height: Optional[int] = None):
        data = {
            'height': str(height) if height else None
        }
        return await self._request('block', data=data)

    async def block_search(self, query: str, prove: Optional[bool] = None,
                           page: Optional[int] = None, per_page: Optional[int] = None,
                           order_by: Optional[str] = None):
        data = {
            'query': query
        }
        if prove:
            data['prove'] = str(prove)
        if page:
            data['page'] = str(page)
        if per_page:
            data['per_page'] = str(per_page)
        if order_by:
            data['order_by'] = order_by

        return await self._request('block_search', data=data)

    async def get_block_results(self, height: int):
        data = {
            'height': str(height)
        }
        return await self._request('block_results', data=data)

    async def get_block_commit(self, height: int):
        data = {
            'height': str(height)
        }
        return await self._request('commit', data=data)

    async def get_blockchain_info(self, min_height: int, max_height: int):
        assert max_height > min_height

        data = {
            'minHeight': str(min_height),
            'maxHeight': str(max_height)
        }

        return await self._request('blockchain', data=data)

    async def check_tx(self, tx: Tx):
        tx_raw = TxRaw(body_bytes=tx.body.SerializeToString(),
                       auth_info_bytes=tx.auth_info.SerializeToString(),
                       signatures=tx.signatures)
        tx_bytes = tx_raw.SerializeToString()
        data = {
            'tx': '0x' + tx_bytes.hex(),
        }

        return await self._request('check_tx', data=data)

    async def broadcast_tx(self, tx: Tx, mode: BroadcastMode = BROADCAST_MODE_SYNC):
        tx_raw = TxRaw(body_bytes=tx.body.SerializeToString(),
                       auth_info_bytes=tx.auth_info.SerializeToString(),
                       signatures=tx.signatures)
        tx_bytes = tx_raw.SerializeToString()
        data = {
            'tx': '0x' + tx_bytes.hex(),
        }
        if mode == BROADCAST_MODE_SYNC:
            return await self._broadcast_tx_sync(data)
        elif mode == BROADCAST_MODE_ASYNC:
            return await self._broadcast_tx_async(data)
        elif mode == BROADCAST_MODE_BLOCK:
            return await self._broadcast_tx_commit(data)

    async def _broadcast_tx_async(self, tx_data: Dict):
        return await self._request_session('broadcast_tx_async', params=tx_data)

    async def _broadcast_tx_commit(self, tx_data: Dict):
        return await self._request_session('broadcast_tx_commit', params=tx_data)

    async def _broadcast_tx_sync(self, tx_data: Dict):
        return await self._request_session('broadcast_tx_sync', params=tx_data)

    async def get_consensus_params(self, height: Optional[int] = None):
        data = {
            'height': str(height) if height else None
        }

        return await self._request('consensus_params', data=data)

    async def get_tx(self, tx_hash: str, prove: Optional[bool] = None):
        data = {
            'hash': tx_hash
        }
        if prove:
            data['prove'] = str(prove)

        return await self._request('tx', data=data)

    async def tx_search(self, query: str, prove: Optional[bool] = None,
                        page: Optional[int] = None, per_page: Optional[int] = None,
                        order_by: Optional[str] = None):
        data = {
            'query': query
        }
        if prove:
            data['prove'] = str(prove)
        if page:
            data['page'] = str(page)
        if per_page:
            data['per_page'] = str(per_page)
        if order_by:
            data['order_by'] = order_by

        return await self._request('tx_search', data=data)

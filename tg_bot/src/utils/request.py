from typing import Any, Dict, Optional

import aiohttp
from aiohttp.typedefs import LooseHeaders
from multidict import CIMultiDict


from conf.config import settings


class ClientSessionWithCorrId(aiohttp.ClientSession):
    def _prepare_headers(self, headers: Optional[LooseHeaders]) -> CIMultiDict[str]:
        headers = super()._prepare_headers(headers)

        return headers


async def do_request(
    url: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, Any]] = None, method: str = 'POST'
) -> Any:

    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()


    final_exc = None
    async with ClientSessionWithCorrId(connector=connector, timeout=timeout) as session:
        for _ in range(settings.RETRY_COUNT):
            try:
                async with session.request(
                    method,
                    url,
                    json=params,
                ) as response:
                    response.raise_for_status()
                    print(url)
                    return await response.json()
            except aiohttp.ClientResponseError as exc:
                final_exc = exc

    if final_exc is not None:
        raise final_exc

    raise RuntimeError('Unsupported')
"""HTTP handlers declarations."""

from aiohttp.web_urldispatcher import View

from web_utils import async_json_out


class Votes(View):
    """Dummy index endpoint."""

    @async_json_out
    async def post(self):
        """Return dummy json in response to HTTP GET request."""
        json_body = await self.request.json() if self.request.has_body else {}
        return {
            'cookies': dict(self.request.cookies),
            'has_body': self.request.has_body,
            'headers': dict(self.request.headers),
            'json_body': json_body,
            'query': dict(self.request.query),
        }

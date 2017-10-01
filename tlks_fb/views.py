"""HTTP handlers declarations."""

from aiohttp.web_urldispatcher import View

from web_utils import async_json_out
from db.models import TalkTbl


class Votes(View):
    """Dummy index endpoint."""

    @async_json_out
    async def post(self):
        """Return dummy json in response to HTTP POST request."""
        json_body = await self.request.json() if self.request.has_body else {}
        return {
            'cookies': dict(self.request.cookies),
            'has_body': self.request.has_body,
            'headers': dict(self.request.headers),
            'json_body': json_body,
            'match_info': dict(self.request.match_info),
            'query': dict(self.request.query),
        }


class Talk(View):
    """Dummy index endpoint."""

    @async_json_out
    async def get(self):
        """Return dummy json in response to HTTP GET request."""
        talk_name = self.request.match_info['name']
        async with self.request.app['db_engine'].accuire() as conn:
            talk_votes = await conn.execute(
                TalkTbl.select([
                    TalkTbl.positive,
                    TalkTbl.negative,
                    TalkTbl.neutral,
                ]).where(TalkTbl.name == talk_name)
            ).fetchone()
        # TODO: get talk by name
        return {
            'talk_name': talk_name,
            'positive': talk_votes['positive'],
            'negative': talk_votes['negative'],
            'neutral': talk_votes['neutral'],
        }

    @async_json_out
    async def post(self):
        """Return dummy json in response to HTTP POST request."""
        talk_name = self.request.match_info['name']
        # TODO: update talk by name
        return {
            'talk_name': talk_name,
        }

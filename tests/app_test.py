"""Basic tests suite for aiohttp app."""

from unittest.mock import patch

from tlks_fb.app import build_application


@patch('aiomysql.sa.create_engine')  # temporarily mock DB connection
async def test_app(test_client, loop):
    """Check availability of the root endpoint."""
    app = await build_application()
    client = await test_client(app)
    resp = await client.get('/')
    assert resp.status == 200
    text = await resp.text()
    assert '' == text

import http
from unittest.mock import (
    AsyncMock,
    patch,
)

import pytest

from que_sdk import (
    QueClient,
)


@pytest.mark.asyncio
async def test_signup():
    mock_response = AsyncMock()
    mock_response.json.return_value = [
        {
            "username": "newUsername1",
            "language": "en",
            "id": 100,
            "telegram_id": None,
            "roles": [],
        },
        {
            "username": "newUsername2",
            "language": "fr",
            "id": 200,
            "telegram_id": 1234,
            "roles": [{"title": "newRole", "id": 5}],
        },
    ]

    with patch("que_sdk.QueClient", new=mock_response):
        client = QueClient()
        response = await client.get_users()

    assert response[0] == http.HTTPStatus.OK

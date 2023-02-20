# from httpx import AsyncClient
# import pytest

# headers = {"Authorization": ""}


# @pytest.mark.asyncio
# async def test_get_hello_worlds_ok_status_200(client: AsyncClient) -> None:
#     response = await client.get("/api/v1/helloworlds/", headers=headers)
#     assert response.status_code == 200
#     assert response.json() == "Hello world!"


# @pytest.mark.asyncio
# async def test_get_hello_worlds_error_status_404(client: AsyncClient) -> None:
#     response = await client.get("/helloworlds/", headers=headers)
#     assert response.status_code == 404

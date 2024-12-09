import httpx


async_client = httpx.AsyncClient(timeout=None)


async def todo_fetch_helper():

    res = await async_client.get("https://dummyjson.com/todos")

    return {
        "success": True,
        "message": "Todos fetched successfully",
        "todos": res.json(),
    }

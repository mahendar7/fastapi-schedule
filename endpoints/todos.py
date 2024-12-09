from fastapi import APIRouter


router = APIRouter()

router = APIRouter(prefix="/todos", tags=["todos"])

from services import todo_service


@router.get("")
async def get_todos():
    return await todo_service.todo_fetch_helper()

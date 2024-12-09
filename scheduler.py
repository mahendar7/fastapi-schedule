import asyncio
import schedule

import time
from services.todo_service import todo_fetch_helper


async def track_pending_todo():
    todos = await todo_fetch_helper()

    print("todos fetched in scheduling", todos)


async def track_all_pending_todos():
    pending_todos = ["1"]

    tasks = [track_pending_todo() for todo in pending_todos]
    await asyncio.gather(*tasks)


def run_scheduler():
    schedule.every().day.at("23:18").do(asyncio.run, track_all_pending_todos())

    while True:
        schedule.run_pending()
        time.sleep(1)

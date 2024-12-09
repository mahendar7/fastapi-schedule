import threading  # You can use multiprocessing for a separate process
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

from fastapi.middleware.cors import CORSMiddleware
from scheduler import run_scheduler

from endpoints import todos


async def http_logs_middleware(request: Request, call_next):
    response = await call_next(request)
    # logger.info(f"Request: {request.method} {request.url} Response: {response.status_code}")
    return response


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()
    print(
        "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< WELCOME >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    )

    yield
    # Run shutdown events


app = FastAPI(lifespan=app_lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(http_logs_middleware)


app.include_router(todos.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, root_path="/api", log_level="info")

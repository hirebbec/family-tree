import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.config import settings
from api.router import project_router

app = FastAPI(
    title=settings().PROJECT_NAME,
    openapi_url="/api/openapi.json",
    docs_url="/api/swagger",
)

app.include_router(project_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app=app, host=settings().SERVER_HOST, port=settings().SERVER_PORT)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
import os

app = FastAPI(title="AllSeeing-AI Backend", version="1.0.0")

# CORS for frontend preview
frontend_url = os.getenv("FRONTEND_URL", "*")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*" if frontend_url == "*" else frontend_url],
    allow_credentials=True,
    allow_methods=["*"];
    allow_headers=["*"]
)


class HealthResponse(BaseModel):
    message: str
    service: str
    version: str


@app.get("/", response_model=HealthResponse)
async def root() -> HealthResponse:
    return HealthResponse(message="OK", service="allseeing-ai-backend", version="1.0.0")


@app.get("/test")
async def test() -> Dict[str, str]:
    # Marketing site only; return mock database connectivity info
    return {
        "backend": "OK",
        "database": "Not required for marketing site",
        "database_url": "n/a",
        "database_name": "n/a",
        "connection_status": "n/a",
        "collections": []
    }

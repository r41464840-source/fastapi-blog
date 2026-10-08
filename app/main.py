from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .routers import posts, users, auth, categories


app = FastAPI(
    title="Blog API",
    description="FastAPI + PostgreSQL + JWT Auth + Alembic",
    version="4.0.0",
    docs_url="/docs" if settings.debug else None,
    redoc_url="/redoc" if settings.debug else None,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(categories.router)


@app.get("/")
def root():
    return {"xabar": "Blog API v4.0 — Alembic bilan!"}
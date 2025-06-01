from fastapi import FastAPI, APIRouter
from typing import Dict, Any

# Create a router for API endpoints
api_router = APIRouter()

# API endpoints
@api_router.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Welcome to FastAPI"}

@api_router.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy"}

def create_app() -> FastAPI:
    app = FastAPI(
        title="Your API",
        description="Your API description",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json"
    )

    # Include the router with a prefix
    app.include_router(api_router, prefix="/api/v1")

    return app

# Create the application instance
app = create_app()

"""
Main application module for the Challenge API.

This module serves as the entry point for the FastAPI application,
configuring the main app instance, lifespan management, middleware,
and API route registration.

The API provides endpoints for various coding challenges including
string operations, sequence calculations, board game solutions,
and employment benefits computations.
"""

from core.logging import logger
from core.config import settings
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from api.routes import string, sequence, board_game, benefits


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for application startup and shutdown events.

    Handles initialization and cleanup operations for the application.
    The code before yield runs on startup, and code after yield runs on shutdown.

    Args:
        app (FastAPI): The FastAPI application instance

    Yields:
        None: Control is returned to the application runtime
    """
    logger.info(f"Application started: {settings.APP_NAME}")

    yield
    logger.info(f"Application stopped: {settings.APP_NAME}")


app = FastAPI(
    title=settings.APP_NAME,
    description="API for solving coding challenges",
    version="1.0.0",
    lifespan=lifespan,
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """
    HTTP middleware for logging incoming requests.

    Logs all incoming HTTP requests with method and URL information
    before passing them to the next middleware or route handler.

    Args:
        request (Request): The incoming HTTP request
        call_next (Callable): The next middleware or route handler

    Returns:
        Response: The HTTP response from the next handler
    """
    logger.info(
        "Request received", extra={"method": request.method, "url": str(request.url)}
    )
    response = await call_next(request)
    return response


# Register API routers
app.include_router(string.router, prefix="/api/v1")
app.include_router(sequence.router, prefix="/api/v1")
app.include_router(board_game.router, prefix="/api/v1")
app.include_router(benefits.router, prefix="/api/v1")

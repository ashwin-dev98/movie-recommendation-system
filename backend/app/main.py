import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.routes import router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

logger.info("Starting Movie Recommendation API...")

app = FastAPI(
    title="Movie Recommendation API",
    description="Content-Based Movie Recommendation System built using FastAPI and Scikit-Learn",
    version="1.0.0"
)

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

# Register API routes
app.include_router(router)

logger.info("API started successfully.")
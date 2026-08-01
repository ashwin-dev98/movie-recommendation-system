from fastapi import APIRouter, HTTPException, Query

from backend.app.schemas.recommendation import RecommendationResponse
from backend.app.services.recommendation_service import (
    get_recommendations
)

router = APIRouter()


@router.get("/", tags=["Home"])
def home():
    return {
        "message": "Movie Recommendation API is running!"
    }


@router.get(
    "/recommend",
    response_model=RecommendationResponse,
    tags=["Recommendations"],
    summary="Get movie recommendations",
    description="Returns the top 10 similar movies based on the movie title."
)
def recommend_movie(
    movie: str = Query(
        ...,
        min_length=2,
        max_length=100,
        description="Movie title to search"
    )
):
    recommendations = get_recommendations(movie)

    if recommendations is None:
        raise HTTPException(
            status_code=404,
            detail="Movie not found."
        )

    return RecommendationResponse(
        movie=movie,
        recommendations=recommendations
    )
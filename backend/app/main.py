from fastapi import FastAPI

from backend.recommendation.loader import load_models
from backend.recommendation.recommender import recommend

app = FastAPI(
    title="Movie Recommendation API",
    description="Content-Based Movie Recommendation System",
    version="1.0.0"
)

print("Loading ML models...")

movie_data, vectorizer, similarity_matrix = load_models()

print("Models loaded successfully!")


@app.get("/")
def home():
    return {
        "message": "Movie Recommendation API is running!"
    }


@app.get("/recommend")
def get_recommendations(movie: str):

    recommendations = recommend(
        movie,
        movie_data,
        similarity_matrix
    )

    if recommendations is None:
        return {
            "error": "Movie not found."
        }

    return {
        "movie": movie,
        "recommendations": recommendations
    }
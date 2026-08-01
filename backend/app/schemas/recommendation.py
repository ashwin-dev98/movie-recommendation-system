from pydantic import BaseModel


class MovieCard(BaseModel):
    title: str
    year: str
    rating: float
    overview: str
    poster: str | None = None


class RecommendationResponse(BaseModel):
    movie: str
    recommendations: list[MovieCard]
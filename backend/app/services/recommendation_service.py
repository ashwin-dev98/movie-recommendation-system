import logging

from backend.recommendation.loader import load_models
from backend.recommendation.recommender import recommend
from backend.app.external.tmdb import get_movie_details

logger = logging.getLogger(__name__)

logger.info("Loading ML models...")

movie_data, vectorizer, similarity_matrix = load_models()

logger.info("ML models loaded successfully.")


def get_recommendations(movie: str):
    """
    Returns enriched movie recommendations.
    """

    logger.info(f"Searching recommendations for '{movie}'")

    recommendations = recommend(
        movie,
        movie_data,
        similarity_matrix
    )

    # Debug
    print("\n==============================")
    print("ML Recommendations:")
    print(recommendations)
    print("==============================")

    if recommendations is None:
        logger.warning(f"Movie '{movie}' not found.")
        return None

    enriched_recommendations = []

    for title in recommendations:

        print(f"\nSearching TMDB for: {title}")

        details = get_movie_details(title)

        print("Returned:")
        print(details)

        if details:
            enriched_recommendations.append(details)

    logger.info("Recommendations generated successfully.")

    return enriched_recommendations
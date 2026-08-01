import os
import re
import requests

from dotenv import load_dotenv

# Load environment variables
load_dotenv("backend/.env")

API_KEY = os.getenv("TMDB_API_KEY")

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"


def search_movie(title: str):
    """
    Search TMDB for a movie.
    Removes the year (e.g., "(2014)") before searching.
    """

    # Remove year from title
    title = re.sub(r"\s*\(\d{4}\)$", "", title)

    url = f"{BASE_URL}/search/movie"

    params = {
        "api_key": API_KEY,
        "query": title
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    # Debug (temporary)
    print("\nTMDB Response:")
    print(data)

    results = data["results"]

    if not results:
        return None

    return results[0]


def get_movie_details(title: str):
    """
    Returns cleaned movie details.
    """

    movie = search_movie(title)

    if movie is None:
        return None

    return {
        "title": movie["title"],
        "year": movie["release_date"][:4]
        if movie.get("release_date")
        else "Unknown",
        "rating": movie["vote_average"],
        "overview": movie["overview"],
        "poster": (
            IMAGE_BASE_URL + movie["poster_path"]
            if movie.get("poster_path")
            else None
        )
    }
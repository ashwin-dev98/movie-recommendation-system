import pandas as pd


def load_data():
    movies = pd.read_csv("data/raw/movies.csv")
    tags = pd.read_csv("data/raw/tags.csv")
    return movies, tags


def preprocess(movies, tags):
    tag_data = (
        tags.groupby("movieId")["tag"]
        .apply(lambda x: " ".join(x))
        .reset_index()
    )

    movie_data = movies.merge(
        tag_data,
        on="movieId",
        how="left"
    )

    movie_data["tag"] = movie_data["tag"].fillna("")

    movie_data["genres"] = movie_data["genres"].str.replace(
        "|",
        " ",
        regex=False
    )

    movie_data["features"] = (
        movie_data["genres"] +
        " " +
        movie_data["tag"]
    )

    return movie_data
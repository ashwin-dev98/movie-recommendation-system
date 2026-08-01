import pandas as pd
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading datasets...")

# -----------------------------
# Read datasets
# -----------------------------
movies = pd.read_csv("data/raw/movies.csv")
tags = pd.read_csv("data/raw/tags.csv")

print("Datasets loaded successfully.")

# -----------------------------
# Group tags by movieId
# -----------------------------
tag_data = (
    tags.groupby("movieId")["tag"]
    .apply(lambda x: " ".join(x))
    .reset_index()
)

print("Tags grouped successfully.")

# -----------------------------
# Merge movies and tags
# -----------------------------
movie_data = movies.merge(
    tag_data,
    on="movieId",
    how="left"
)

print("Datasets merged.")

# -----------------------------
# Fill missing tags
# -----------------------------
movie_data["tag"] = movie_data["tag"].fillna("")

print("Missing values handled.")

# -----------------------------
# Replace | with spaces
# -----------------------------
movie_data["genres"] = movie_data["genres"].str.replace(
    "|",
    " ",
    regex=False
)

# -----------------------------
# Create features column
# -----------------------------
movie_data["features"] = (
    movie_data["genres"] +
    " " +
    movie_data["tag"]
)

print("Feature column created.")

# -----------------------------
# Vectorization
# -----------------------------
vectorizer = CountVectorizer(stop_words="english")

feature_matrix = vectorizer.fit_transform(
    movie_data["features"]
)

print("Vectorization completed.")

# -----------------------------
# Cosine Similarity
# -----------------------------
similarity_matrix = cosine_similarity(feature_matrix)

print("Similarity matrix created.")

# -----------------------------
# Save trained objects
# -----------------------------
pickle.dump(
    movie_data,
    open("backend/models/movie_data.pkl", "wb")
)

pickle.dump(
    vectorizer,
    open("backend/models/vectorizer.pkl", "wb")
)

pickle.dump(
    feature_matrix,
    open("backend/models/feature_matrix.pkl", "wb")
)

pickle.dump(
    similarity_matrix,
    open("backend/models/similarity_matrix.pkl", "wb")
)

print("\n===================================")
print("Model training completed!")
print("Files saved in backend/models/")
print("===================================")
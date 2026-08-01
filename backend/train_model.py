import pickle

from recommendation.preprocessing import (
    load_data,
    preprocess
)

from recommendation.trainer import train


movies, tags = load_data()

movie_data = preprocess(movies, tags)

vectorizer, feature_matrix, similarity_matrix = train(movie_data)


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

print("Training Complete!")
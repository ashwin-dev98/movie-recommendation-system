from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def train(movie_data):

    vectorizer = CountVectorizer(stop_words="english")

    feature_matrix = vectorizer.fit_transform(
        movie_data["features"]
    )

    similarity_matrix = cosine_similarity(
        feature_matrix
    )

    return (
        vectorizer,
        feature_matrix,
        similarity_matrix
    )
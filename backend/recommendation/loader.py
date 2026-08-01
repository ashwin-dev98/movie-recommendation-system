import pickle

def load_models():

    movie_data = pickle.load(
        open("backend/models/movie_data.pkl", "rb")
    )

    vectorizer = pickle.load(
        open("backend/models/vectorizer.pkl", "rb")
    )

    similarity_matrix = pickle.load(
        open("backend/models/similarity_matrix.pkl", "rb")
    )

    return movie_data, vectorizer, similarity_matrix
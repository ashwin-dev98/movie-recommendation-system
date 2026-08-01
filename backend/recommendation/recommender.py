def recommend(movie_title, movie_data, similarity_matrix):
    """
    Returns the top 10 movie recommendations.
    Returns None if no movie is found.
    """

    # Search movie (case-insensitive)
    matches = movie_data[
        movie_data["title"].str.contains(
            movie_title,
            case=False,
            na=False
        )
    ]

    # Movie not found
    if matches.empty:
        return None

    # First matching movie
    index = matches.index[0]

    # Calculate similarity
    similar_movies = sorted(
        list(enumerate(similarity_matrix[index])),
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    # Skip first movie (itself)
    for movie in similar_movies[1:11]:
        recommendations.append(
            movie_data.iloc[movie[0]]["title"]
        )

    return recommendations
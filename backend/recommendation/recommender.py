def recommend(movie_title, movie_data, similarity_matrix):

    matches = movie_data[
        movie_data["title"].str.contains(
            movie_title,
            case=False,
            na=False
        )
    ]

    if matches.empty:
        return []

    index = matches.index[0]

    similar_movies = sorted(
        list(enumerate(similarity_matrix[index])),
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for movie in similar_movies[1:11]:
        recommendations.append(
            movie_data.iloc[movie[0]]["title"]
        )

    return recommendations
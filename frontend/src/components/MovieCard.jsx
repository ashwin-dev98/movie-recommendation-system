import "../styles/MovieCard.css";

function MovieCard({ movie }) {

    return (

        <div className="movie-card">

            <img
                src={movie.poster}
                alt={movie.title}
            />

            <h3>{movie.title}</h3>

            <p>⭐ {movie.rating}</p>

            <p>{movie.year}</p>

        </div>

    );

}

export default MovieCard;
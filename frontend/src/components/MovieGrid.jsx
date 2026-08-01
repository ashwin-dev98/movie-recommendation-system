import MovieCard from "./MovieCard";

import "../styles/MovieGrid.css";

function MovieGrid({ recommendations }) {

    if (recommendations.length === 0) {

        return null;

    }

    return (

        <div className="movie-grid">

            {

                recommendations.map((movie, index) => (

                    <MovieCard

                        key={index}

                        movie={movie}

                    />

                ))

            }

        </div>

    );

}

export default MovieGrid;
import { useState } from "react";

import Header from "../components/Header";
import SearchBar from "../components/SearchBar";
import MovieGrid from "../components/MovieGrid";

import api from "../services/api";

function Home() {

    // Stores all recommended movies
    const [recommendations, setRecommendations] = useState([]);

    // Called whenever the user clicks Search
    const handleSearch = async (movie) => {

        try {

            const response = await api.get("/recommend", {
                params: {
                    movie: movie
                }
            });

            console.log("API Response:");
            console.log(response.data);

            // Save recommendations into state
            setRecommendations(response.data.recommendations);

        }

        catch (error) {

            console.error("Error fetching recommendations:", error);

            setRecommendations([]);

        }

    };

    return (

        <>

            <Header />

            <SearchBar
                onSearch={handleSearch}
            />

            <MovieGrid
                recommendations={recommendations}
            />

        </>

    );

}

export default Home;
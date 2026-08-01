import { useState } from "react";

import Header from "../components/Header";
import SearchBar from "../components/SearchBar";

import api from "../services/api";

function Home() {

    const [recommendations, setRecommendations] = useState([]);

    const handleSearch = async (movie) => {

        try {

            const response = await api.get("/recommend", {
                params: {
                    movie: movie
                }
            });

            console.log(response.data);

            setRecommendations(response.data.recommendations);

        }

        catch (error) {

            console.error(error);

        }

    };

    return (

        <>

            <Header />

            <SearchBar
                onSearch={handleSearch}
            />

        </>

    );

}

export default Home;
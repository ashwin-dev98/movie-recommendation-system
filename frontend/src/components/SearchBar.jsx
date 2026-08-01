import { useState } from "react";
import "../styles/SearchBar.css";

function SearchBar({ onSearch }) {
  const [movie, setMovie] = useState("");

  const handleSearch = () => {
    if (movie.trim() === "") return;

    onSearch(movie);
  };

  const handleKeyPress = (event) => {
    if (event.key === "Enter") {
      handleSearch();
    }
  };

  return (
    <div className="search-container">
      <input
        type="text"
        placeholder="Search for a movie..."
        value={movie}
        onChange={(event) => setMovie(event.target.value)}
        onKeyDown={handleKeyPress}
      />

      <button onClick={handleSearch}>
        Search
      </button>
    </div>
  );
}

export default SearchBar;
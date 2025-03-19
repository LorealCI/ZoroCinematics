document.addEventListener("DOMContentLoaded", function () {
    const wrapper = document.querySelector(".wrapper");

    // Fetch trending movies
    fetch("/trending/")
        .then(response => {
            if (!response.ok) {
                throw new Error("Failed to fetch trending movies");
            }
            return response.json();
        })
        .then(data => {
            // Populate the carousel with movie posters
            data.results.slice(0, 8).forEach((movie, index) => {
                const item = document.createElement("div");
                item.className = `item item${index + 1}`;
                item.style.backgroundImage = `url('https://image.tmdb.org/t/p/w200${movie.poster_path}')`;
                item.style.backgroundSize = "cover";
                item.style.backgroundPosition = "center";
                wrapper.appendChild(item);
            });
        })
        .catch(error => {
            console.error("Error fetching trending movies:", error);
        });
});

/* document.addEventListener("DOMContentLoaded", function () {
    fetch("/trending/")
        .then(response => response.json())
        .then(data => {
            const trendingDiv = document.getElementById("trending");
            let content = '<div class="row">';
            data.results.slice(0, 4).forEach(movie => {
                content += `
                    <div class="col-md-3 mb-4">
                        <div class="card h-100">
                            <img src="https://image.tmdb.org/t/p/w200${movie.poster_path}" class="card-img-top" alt="${movie.title}">
                            <div class="card-body">
                                <h5 class="card-title text-white">${movie.title}</h5>
                                <p class="card-text text-white">${movie.overview}</p>
                                <a href="/movie/${movie.id}/" class="btn btn-primary">View Details</a>
                            </div>
                        </div>
                    </div>
                `;
            });
            content += '</div>';
            trendingDiv.innerHTML = content;
        })
        .catch(error => {
            console.error("Error fetching trending movies:", error);
        });
}); */

/*document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search-input");
    const suggestionsList = document.getElementById("suggestions");

    searchInput.addEventListener("input", function () {
        const query = searchInput.value;

        if (query.length > 2) { // Fetch suggestions only if the input length is greater than 2
            fetch(`/autocomplete/?q=${query}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error("Failed to fetch suggestions");
                    }
                    return response.json();
                })
                .then(data => {
                    // Clear existing suggestions
                    suggestionsList.innerHTML = "";

                    // Populate the datalist with new suggestions
                    data.forEach(movie => {
                        const option = document.createElement("option");
                        option.value = movie.title; // Set the movie title as the value
                        suggestionsList.appendChild(option);
                    });
                })
                .catch(error => {
                    console.error("Error fetching autocomplete suggestions:", error);
                });
        } else {
            // Clear suggestions if the input is too short
            suggestionsList.innerHTML = "";
        }
    });
});*/
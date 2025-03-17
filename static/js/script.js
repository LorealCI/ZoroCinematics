document.addEventListener("DOMContentLoaded", function () {
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
});
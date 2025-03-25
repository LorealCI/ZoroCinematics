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


document.addEventListener('DOMContentLoaded', function () {
    const forms = document.querySelectorAll('.edit-review-form');

    forms.forEach(form => {
        form.addEventListener('submit', function (e) {
            e.preventDefault(); // Prevent default form submission

            const url = this.action;
            const formData = new FormData(this);

            fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
                },
                body: formData,
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        showTemporaryAlert('Review updated successfully!', 'success');
                        location.reload(); // Reload the page to reflect changes
                    } else {
                        showTemporaryAlert('Error: ' + JSON.stringify(data.errors), 'error');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    showTemporaryAlert('An unexpected error occurred.', 'error');
                });
        });
    });

    // Function to show a temporary alert
    function showTemporaryAlert(message, type,) {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type}`;
        alertDiv.textContent = message;
        alertDiv.style.position = 'fixed';
        alertDiv.style.top = '40px';
        alertDiv.style.right = '40px';
        alertDiv.style.zIndex = '1000';
        alertDiv.style.padding = '10px 20px';
        alertDiv.style.borderRadius = '5px';
        alertDiv.style.backgroundColor = type === 'success' ? '#d4edda' : '#f8d7da';
        alertDiv.style.color = type === 'success' ? '#155724' : '#721c24';
        alertDiv.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';

        document.body.appendChild(alertDiv);

        // Remove the alert after 5 seconds
        setTimeout(() => {
            alertDiv.remove();
        }, 5000);
    }
});


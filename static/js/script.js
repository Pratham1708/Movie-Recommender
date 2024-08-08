function getRecommendations() {
  const movieName = document.getElementById('movie-input').value.trim();

  fetch(`/recommend?movie_name=${encodeURIComponent(movieName)}`)
      .then(response => response.json())
      .then(data => {
          const top5Movies = data.top_5_movies;
          const bestRemainingMovie = data.best_remaining_movie;

          const top5MoviesList = document.getElementById('top-5-movies');
          top5MoviesList.innerHTML = '';
          top5Movies.forEach(movie => {
              const listItem = document.createElement('li');
              listItem.textContent = movie;
              top5MoviesList.appendChild(listItem);
          });

          const bestRemainingMovieElement = document.getElementById('best-remaining-movie');
          bestRemainingMovieElement.textContent = bestRemainingMovie;
      })
      .catch(error => console.error('Error:', error));
}

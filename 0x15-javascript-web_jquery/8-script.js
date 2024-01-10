$(document).ready(function () {
  // Fetch the movies data from the URL
  $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function (data) {
    // Iterate through each movie and add its title to the <ul> with id 'list_movies'
    data.results.forEach(function (movie) {
      $("#list_movies").append("<li>" + movie.title + "</li>");
    });
  });
});


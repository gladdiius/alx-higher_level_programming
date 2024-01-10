$(document).ready(function () {
  // Fetch the character data from the URL
  $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function (data) {
    // Display the character name in the <div> with id 'character'
    $("#character").text(data.name);
  });
});


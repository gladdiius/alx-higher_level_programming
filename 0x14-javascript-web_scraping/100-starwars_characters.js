#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const film = JSON.parse(body);

      // Print character names for the specified film
      film.characters.forEach(characterUrl => {
        request.get(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else {
            const character = JSON.parse(charBody);
            console.log(character.name);
          }
        });
      });
    } catch (parseError) {
      console.error(parseError);
    }
  }
});

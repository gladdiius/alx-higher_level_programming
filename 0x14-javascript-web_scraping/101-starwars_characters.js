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

      // Fetch character information for each character in the same order
      const fetchCharacters = async () => {
        for (const characterUrl of film.characters) {
          const characterResponse = await fetchCharacter(characterUrl);
          console.log(characterResponse.name);
        }
      };

      // Function to fetch character information
      const fetchCharacter = (characterUrl) => {
        return new Promise((resolve, reject) => {
          request.get(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
              reject(charError);
            } else {
              const character = JSON.parse(charBody);
              resolve(character);
            }
          });
        });
      };

      // Execute the function to fetch and print characters
      fetchCharacters();
    } catch (parseError) {
      console.error(parseError);
    }
  }
});

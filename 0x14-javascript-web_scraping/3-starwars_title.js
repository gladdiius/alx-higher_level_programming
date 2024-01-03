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
      console.log(film.title);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});

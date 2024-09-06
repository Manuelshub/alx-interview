#!/usr/bin/node

const request = require('request'); // Use the normal request module
const movieId = process.argv[2];

function getCharacterNames (movieId) {
  // Fetch the movie data
  request.get(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, { json: true }, (error, response, body) => {
    if (error) {
      return console.error('Error:', error.message);
    }

    const charactersUrls = body.characters;

    // Fetch each character's data
    charactersUrls.forEach(url => {
      request.get(url, { json: true }, (error, response, body) => {
        if (error) {
          return console.error('Error:', error.message);
        }
        console.log(body.name);
      });
    });
  });
}

getCharacterNames(movieId);

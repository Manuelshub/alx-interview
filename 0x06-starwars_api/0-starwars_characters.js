#!/usr/bin/node

const util = require('util');
const request = util.promisify(require('request')); // Use the normal request module
const movieId = process.argv[2];

async function getCharacterNames (movieId) {
  // Fetch the movie data
  let resp = await (await request(`https://swapi-api.alx-tools.com/api/films/${movieId}/`)).body;

  resp = JSON.parse(resp);
  const charactersUrls = resp.characters;

  // Fetch each character's data
  for (const url of charactersUrls) {
    let character = await (await request(url)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}

getCharacterNames(movieId);

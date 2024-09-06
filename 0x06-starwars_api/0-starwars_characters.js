#!/usr/bin/node

const axios = require('axios').default;
const movieId = process.argv[2];

async function getCharacterNames (movieId) {
  try {
    const resp = await axios.get(`https://swapi-api.alx-tools.com/api/films/${movieId}/`);
    const charactersUrls = resp.data.characters;

    for (const url of charactersUrls) {
      const characterResp = await axios.get(url);
      console.log(characterResp.data.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}
getCharacterNames(movieId);

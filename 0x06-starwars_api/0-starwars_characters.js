#!/usr/bin/node
// fecth all characters of Star Wars movie.

const rp = require('request-promise-native');

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function starWarMovieCharacters () {
  try {
    const body = await rp(movieUrl);
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;
    for (const url of characterUrls) {
      const body = await rp(url);
      const character = JSON.parse(body);
      console.log(character.name);
    }
  } catch (error) {
    console.log(error.message);
  }
}
starWarMovieCharacters();

#!/usr/bin/node

// fecth all characters of Star Wars movie.

const rp = require('request-promise-native');
if (process.argv.length < 3) {
  process.exit(1);
}

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function starWarMovieCharacters () {
  try {
    const body = await rp(movieUrl);
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;
    const characterPromises = characterUrls.map(async (url) => {
      const body = await rp(url);
      const character = JSON.parse(body);
      console.log(character.name);
    });
    await Promise.all(characterPromises);
  } catch (error) {
    console.log(error.message);
  }
}
starWarMovieCharacters();

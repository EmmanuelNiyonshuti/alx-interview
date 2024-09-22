#!/usr/bin/node
// fecth all characters of Star Wars movie.

const request = require('request');
const util = require('util');
const rp = util.promisify(request);

if (process.argv.length < 3) {
  process.exit(1);
}

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function fetchCharacter (url) {
  const resp = await rp(url);
  return JSON.parse(resp.body).name;
}
async function starWarMovieCharacters () {
  try {
    const movieResp = await rp(movieUrl);
    const movie = JSON.parse(movieResp.body);
    const characterUrls = movie.characters;
    for (const url of characterUrls) {
      const name = await fetchCharacter(url);
      console.log(name);
    }
  } catch (err) {
    console.error(err.message);
  }
}

starWarMovieCharacters();

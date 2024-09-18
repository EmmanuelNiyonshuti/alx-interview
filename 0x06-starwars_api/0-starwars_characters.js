#!/usr/bin/node
// fecth all characters of Star Wars movie.

const request = require("request")
if (process.argv.length < 3){
    process.exit(1)
}

const movieId = process.argv[2]
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`

function starwarsMovie(){
    request(movieUrl, (err, res, body) => {
    if (err){
        console.log(err)
    };
    if (res.statusCode == 200){
        const movie = JSON.parse(body)
        const charactersUrl = movie.characters;
        charactersUrl.forEach(url => {
            request(url, (err, resp, body) => {
                if (err){
                    console.log(err)
                }
                if (resp.statusCode == 200){
                    const characters = JSON.parse(body);
                    console.log(characters.name)
                }
            })
        })
    };
    });
}
starwarsMovie()

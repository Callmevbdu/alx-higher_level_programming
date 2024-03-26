#!/usr/bin/node
// a script that prints the number of movies where the character
// “Wedge Antilles” is present.

const request = require('request');
let count = 0;

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body).results;

    filmsData.forEach((film) => {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    });

    console.log(count);
  }
});

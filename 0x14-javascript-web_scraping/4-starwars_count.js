#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    return;
  }

  const films = JSON.parse(body).results;
  const wedgeAntillesMovies = films.filter(film =>
    film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
  );

  console.log(wedgeAntillesMovies.length);
});

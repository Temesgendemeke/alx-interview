#!/usr/bin/node
const process = require('process');
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, 'utf-8', async (err, resp, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const movie = JSON.parse(body);
  const characters = movie.characters;

  for (let i = 0; i < characters.length; i++) {
    await new Promise((resolve, reject) => {
      request(characters[i], 'utf-8', (err, resp, body) => {
        if (err) {
          console.error(err);
          reject(err);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
          resolve();
        }
      });
    });
  }
});
#!/usr/bin/node
// Script that reads a file and prints its content

const request = require('request');

const endpoint = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(endpoint, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});

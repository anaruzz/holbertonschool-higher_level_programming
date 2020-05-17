#!/usr/bin/node
// Script that reads a file and prints its content

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', response && response.statusCode);
  }
});

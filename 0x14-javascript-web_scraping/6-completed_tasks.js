#!/usr/bin/node
// Script that reads a file and prints its content

const request = require('request');

const endpoint = process.argv[2];

request.get(endpoint, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const dict = {};
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed) {
        if (dict[data[i].userId] === undefined) {
          dict[data[i].userId] = 1;
        } else {
          dict[data[i].userId] += 1;
        }
      }
    }
    console.log(dict);
  }
});

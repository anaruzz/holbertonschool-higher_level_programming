#!/usr/bin/node
// Script that reads a file and prints its content

const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, body, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});

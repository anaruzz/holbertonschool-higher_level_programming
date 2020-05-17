#!/usr/bin/node
// Script that reads a file and prints its content

const fs = require('fs');
const file = process.argv[2];
const encoding = 'utf-8';

fs.readFile(file, encoding, function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

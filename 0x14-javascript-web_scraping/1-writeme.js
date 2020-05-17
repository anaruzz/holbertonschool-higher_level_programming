#!/usr/bin/node
// Script that reads a file and prints its content

const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];
const encoding = 'utf-8';

fs.appendFile(file, content, encoding, function (err) {
  if (err) {
    console.log(err);
  }
});

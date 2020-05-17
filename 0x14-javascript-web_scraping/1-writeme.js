#!/usr/bin/node
// Script that writes content in a file

const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];
const encoding = 'utf-8';

fs.appendFile(file, content, encoding, function (err) {
  if (err) {
    console.log(err);
  }
});

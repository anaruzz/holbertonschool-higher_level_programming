#!/usr/bin/node
const fs = require('fs');

const file_1 = fs.readFileSync(process.argv[2], 'utf8');
const file_2 = fs.readFileSync(process.argv[3], 'utf8');

const all_content = file_1 + file_2;

fs.appendFileSync(process.argv[4], all_content);

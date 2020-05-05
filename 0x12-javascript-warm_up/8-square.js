#!/usr/bin/node
// a script that prints x times “C is fun”
if (process.argv.length < 3) {
  console.log('Missing size');
} else {
  const a = parseInt(process.argv[2]);
  if (isNaN(a)) {
    console.log('Missing size');
  } else {
    let i = 0;
    let j;
    let line;
    for (; i < a; i++) {
      line = '';
      for (j = 0; j < a; j++) {
        line = line + 'X';
      }
      console.log(line);
    }
  }
}

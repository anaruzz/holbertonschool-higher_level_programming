#!/usr/bin/node
// a script that prints x times “C is fun”
if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  const a = parseInt(process.argv[2]);
  if (isNaN(a)) {
    console.log('Missing number of occurrences');
  } else {
    let i = 0;
    for (; i < a; i++) {
      console.log('C is fun');
    }
  }
}

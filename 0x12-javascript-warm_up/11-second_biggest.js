#!/usr/bin/node
// a script that searches the second biggest integer in the arguments
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let args = process.argv.slice(2, process.argv.length);
  args = args.sort(function (a, b) { return a - b; });
  args.pop();
  args = args.slice(-1);
  console.log(args[0]);
}

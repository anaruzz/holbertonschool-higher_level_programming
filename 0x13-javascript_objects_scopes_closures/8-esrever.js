#!/usr/bin/node

exports.esrever = function (list) {
  const r = [];
  let c = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    r[c] = list[i];
    c++;
  }
  return r;
};

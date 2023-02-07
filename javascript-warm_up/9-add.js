#!/usr/bin/node
const user = process.argv.slice(2);
function add (a, b) {
  console.log(a, b);
}

add(Number(user[0]), Number(user[1]));

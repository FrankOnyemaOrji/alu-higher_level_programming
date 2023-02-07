#!/usr/bin/node
const user = process.argv.slice(2);
// converting first argument to an integer
if (isNaN(parseInt(user[0]))) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < user[0]) {
    console.log('X'.repeat(user[0]));
    i++;
  }
}

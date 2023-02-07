#!/usr/bin/node
const user = process.argv.slice(2);
if (isNaN(parseInt(user[0]))) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < user[0]) {
    console.log('C is fun');
    i++;
  }
}

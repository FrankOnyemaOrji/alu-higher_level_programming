#!/usr/bin/node
const user = process.argv.slice(2);
// Converting the string to an integer
if (isNaN(parseInt(user[0]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(user[0]));
}

#!/usr/bin/node
const user = process.argv.slice(2);
// Converting the string to an integer
if (parseInt(user[0])) {
  console.log('My number: ' + user[0]);
} else {
  console.log('My number: ' + Number(user[0]));
}

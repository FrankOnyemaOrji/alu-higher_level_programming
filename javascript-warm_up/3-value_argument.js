#!/usr/bin/node
const user = process.argv.slice(2);
if (user[0] == null) {
  console.log('No argument');
} else {
  console.log(user[0]);
}

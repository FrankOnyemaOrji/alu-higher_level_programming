#!/usr/bin/node
const user = process.argv.slice(2);

if (user.length === 0) {
  console.log('No argument');
} else if (user.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

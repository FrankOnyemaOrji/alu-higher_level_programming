#!/usr/bin/node
const user = process.argv[2];
const fs = require('fs');

try {
  const data = fs.readFileSync(user, 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}

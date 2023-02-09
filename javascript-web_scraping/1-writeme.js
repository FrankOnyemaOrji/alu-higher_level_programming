#!/usr/bin/node
const user = process.argv;
const f = user[2];
const s = user[3];
const fs = require('fs');

try {
  fs.writeFileSync(f, s, 'utf8');
} catch (err) {
  console.error(err);
}

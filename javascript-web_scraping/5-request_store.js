#!/usr/bin/node
const user = process.argv.slice(2);
const fs = require('fs');
const request = require('request');

request(user[0], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(user[1], body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});

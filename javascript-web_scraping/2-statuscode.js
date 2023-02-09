#!/usr/bin/node
const user = process.argv;
const request = require('request');

request.get(user[2]).on('response', function (response) {
  console.log('code: ' + response.statusCode);
});

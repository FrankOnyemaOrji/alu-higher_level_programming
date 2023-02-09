#!/usr/bin/node
const user = process.argv.slice(2);
const request = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${user[0]}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});

#!/usr/bin/node
const user = process.argv.slice(2)[0];
const request = require('request');

request(user, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const completed = {};
    for (const i in data) {
      if (data[i].completed === true) {
        if (completed[data[i].userId] === undefined) {
          completed[data[i].userId] = 1;
        } else {
          completed[data[i].userId] += 1;
        }
      }
    }
    console.log(completed);
  }
});

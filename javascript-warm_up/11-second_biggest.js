#!/usr/bin/node
const user = process.argv.length;
const a = [];
switch (user) {
  case 2:
  case 3:
    console.log(0);
    break;

  default:
    for (let i = 0; i < user.length; i++) {
      a.push(parseInt(user[i]));
    }
    a.sort((a, b) => b - a);
    console.log(a[1]);
    break;
}

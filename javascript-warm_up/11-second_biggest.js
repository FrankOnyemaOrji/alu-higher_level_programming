#!/usr/bin/node
const user = process.argv.length;
const a = [];
switch (user) {
  case 2:
  case 3:
    console.log(0);
    break;

  default:
    for (let i = 2; i < user; i++) {
      a.push(process.argv[i]);
    }
    a.sort((a, b) => b - a);
    console.log(a[1]);
    break;
}

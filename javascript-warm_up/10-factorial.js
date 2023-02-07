#!/usr/bin/node
const user = process.argv.slice(2);
function factorial (a) {
  if (a < 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

const a = parseInt(user[0]);
if (isNaN(a)) {
  console.log(1);
} else {
  console.log(factorial(a));
}

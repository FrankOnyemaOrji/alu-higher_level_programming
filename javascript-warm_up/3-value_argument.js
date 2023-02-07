#!/usr/bin/node
const user = process.argv.slice(2);
if (user.length === 0) {
    console.log('No argument');
    }else {
    console.log('Argument found');
    }
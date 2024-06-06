#!/usr/bin/node

const args = process.argv.slice(2);
const firstArg = args[0];
const secondArg = args[1];

if (firstArg && secondArg) {
  console.log(`${firstArg} is ${secondArg}`);
} else {
  console.log('undefined is undefined');
}

#!/usr/bin/node

const fs = require('fs');

const source1 = process.argv[2];
const source2 = process.argv[3];
const destination = process.argv[4];

const data1 = fs.readFileSync(source1, 'utf8');
const data2 = fs.readFileSync(source2, 'utf8');

fs.writeFileSync(destination, data1 + data2);

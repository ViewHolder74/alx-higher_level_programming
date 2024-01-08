#!/usr/bin/node

/*
 * script that prints two arguments passed to it,
 * int the folling format "is"
 */

const myVar1 = process.argv[2];
const myVar2 = process.argv[3];
console.log(myVar1 + ' is ' + myVar2);

#!/usr/bin/node

/*
 * Script that prints a message depending of the number of arguments
 * passed
 * if no arguments are passed to the script print "No argument"
 * if only one argument is passed to the script print "Argumeny found"
 * Otherwise, print "Arguments found"
 */

const args = process.argv.length;

if (args === 1)
{
	console.log('No argument');
}
else if (args === 2)
{
	console.log('Argument found');
}
else 
{
	console.log('Arguments found');
}

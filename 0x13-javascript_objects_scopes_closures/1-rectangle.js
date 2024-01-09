#!/usr/bin/node

/*
 * This script create a a class Rectangle that defines a rectangle:
 * The constructor must take 2 arguments w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 */

class Rectangle {
	constructor (w, h) {
		this.width = w;
		this.length = h;
	}
}
module.exports = Rectangle;

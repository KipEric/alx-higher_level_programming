#!/usr/bin/node

const fs = require('fs');

const path = process.argv[2];

const text = process.argv[3];

fs.writeFile(path, text, 'utf-8', function (err) {
	if (err) {
		console.log(err);
	}
});

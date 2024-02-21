#!/usr/bin/node

const fs = require('fs');

function readAndPrintFile(filePath) {
	fs.readFile(filePath, 'utf-8', (err, data) => {
		if (err) {
			console.error(err);
		} else {
			console.log(data);
		}
	});
}

// Check if the correct number of arguments is available
if (process.argv.length !== 3) {
	console.log('Usage: node 0-readme.js <file_path></file_path>');
	process.exit(1);
}

const filePath = process.argv[2];
readAndPrintFile(filePath);
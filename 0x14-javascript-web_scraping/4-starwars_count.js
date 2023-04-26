#!/usr/bin/node

const request = require('request');

const starWars = process.argv[2];

let t = 0;
request(starWars, function(error, response, body) {
	movies = JSON.parse(body).results;


	for (let i = 0; i < movies.length; i++) {
		const characters = movies[i].characters;

		for (let c = 0; c < characters.length; c++) {
			const character = characters[c];
			const characterID = character.split('/')[5];

			if (characterID ==='18') {
				t += 1;
			}
		}
	}

	console.log(t);
});

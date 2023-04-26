#!/usr/bin/node
const request = require('request');

const starWars = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

request(starWars, function (error, response, body) {
	if (error){
		console.error(error);
	} else {
		const movie = JSON.parse(body);
		console.log(movie.title);
	}
});

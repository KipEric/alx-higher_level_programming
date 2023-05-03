$(document).ready(function() {
	let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
	$.get(url, function(data) {
		let movies = data.results;
		let list = $('#list_movies');
		for (let i = 0; i < movies.length; i++) {
			let title = movies[i].title;
			let listItem = $('<li>').text(title);
			list.append(listItem);
		}
	});
});

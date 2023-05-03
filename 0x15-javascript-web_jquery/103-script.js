$(document).ready(function() {
	const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
	const helloDiv = $('#hello');
	const languageInput = $('#language_code');
	const translateBtn = $('#btn_translate');

	function getTranslation() {
		const languageCode = languageInput.val();
		if (langaugeCode) {
			$.getJSON(`${apiUrl}?lang=${languageCode}`, function (data) {
				helloDiv.text(data.hello);
			});
		}
	}

	translateBtn.click(getTranslation);
	languageInput.keyup(function (e) {
		if (e.keyCode === 13) {
			getTranslation();
		}
	});
});

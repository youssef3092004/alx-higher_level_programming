$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (charac) {
    $('DIV#character').text(charac.name)
})

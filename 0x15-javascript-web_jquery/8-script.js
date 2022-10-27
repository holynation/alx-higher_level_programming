$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
    if (status === 'success') {
      const films = data.results;
      for (let idx in films) {
        $('#list_movies').append('<li>' + films[idx].title + '</li>');
      }
    }
  });
});

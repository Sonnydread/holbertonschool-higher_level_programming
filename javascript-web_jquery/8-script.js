$(document).ready(function () {
    $.get("https://swapi-api.hbtn.io/api/films/?format=json",
    function (inf) {
      const films = inf.results;
      const $list = $("#list_movies");
      $.each(films, function (index, drama) {
        let $li = $("<li>").text(drama.title);
        $list.append($li);
      });
    });
});
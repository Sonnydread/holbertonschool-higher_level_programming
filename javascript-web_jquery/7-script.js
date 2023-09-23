$(document).ready(function () {
    $.get("https://swapi-api.hbtn.io/api/people/5/?format=json",
    function (inf) {
          let nombre = inf.name;
          $("#character").text(nombre);
        });
});
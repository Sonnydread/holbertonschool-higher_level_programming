$(document).ready(function () {
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr",
    function (inf) {
      const subtitulation = inf.hello;
      $("#hello").text(subtitulation);
    });
});
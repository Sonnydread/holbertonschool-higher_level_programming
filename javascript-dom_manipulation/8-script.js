const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

window.addEventListener('DOMContentLoaded', _ => {
  const $hello = document.querySelector('#hello');
  fetch(url)
    .then(response => response.json())
    .then(data => {
      const hello = data.hello;
      $hello.innerText = hello;
    });
});
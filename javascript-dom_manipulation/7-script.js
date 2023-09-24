const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

const $character = document.querySelector('#list_movies');

fetch(url)
  .then(response => response.json())
  .then(data => {
    const films = data.results;
    const container = document.createDocumentFragment();
    films.forEach(element => {
      const liElem = document.createElement('LI');
      liElem.innerText = element.title;
      container.appendChild(liElem);
    });
    $character.appendChild(container);
  });
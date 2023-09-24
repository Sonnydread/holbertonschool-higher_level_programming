const redHeader = document.getElementById('red_header');
const header = document.querySelector('header');

redHeader.addEventListener('click', () => {
  header.style.setProperty('color', '#FF0000');
});
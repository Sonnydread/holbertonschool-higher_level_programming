const redHeader = document.getElementById('red_header');
const header = document.querySelector('header');

redHeader.addEventListener('click', () => {
  header.className = 'red';
});
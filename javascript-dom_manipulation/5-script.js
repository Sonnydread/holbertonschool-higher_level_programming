updateHeader = document.getElementById('update_header');
header = document.querySelector('header');

updateHeader.addEventListener('click', () => {
  header.innerText = 'New Header!!!';
});
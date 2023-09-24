addItem = document.getElementById('add_item');
ulElement = document.querySelector('ul.my_list');

addItem.addEventListener('click', () => {
  ulElement.innerHTML += '<li>Item</li>';
});
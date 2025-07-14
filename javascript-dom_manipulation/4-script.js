// Get the element to be clicked
const clickItem = document.getElementById('add_item');
// Get the class where the element must be added
const classItem = document.querySelector('.my_list');
if (clickItem && classItem) {
  clickItem.addEventListener('click', () => {
    const addItem = document.createElement('li');
    addItem.textContent = 'Item';
    classItem.appendChild(addItem);
  });
}

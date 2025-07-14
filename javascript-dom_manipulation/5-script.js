// Get the element to be clicked
const clickHeader = document.getElementById('update_header');
// Get the element to be updated
const updatedHeader = document.querySelector('header');
if (clickHeader) {
  clickHeader.addEventListener('click', () => {
    updatedHeader.innerHTML = 'New Header!!!';
  });
}

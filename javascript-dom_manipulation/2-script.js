// Get the element to be clicked
const clickHeader = document.getElementById('red_header');
// Get the element to put the class into
const addedClass = document.querySelector('header');
// Check if both elements exist before manipulated them
if (clickHeader && addedClass) {
  clickHeader.addEventListener('click', () => {
    addedClass.classList.add('red');
  });
}

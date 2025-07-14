// Get the element to be clicked
const clickHeader = document.getElementById('toggle_header');
// Get the element to be toggled
const toggledClass = document.querySelector('header');
// Check if both elements exist
if (clickHeader && toggledClass) {
  clickHeader.addEventListener('click', () => {
    const isGreen = toggledClass.classList.contains('green');
    toggledClass.classList.toggle('green', !isGreen);
    toggledClass.classList.toggle('red', isGreen);
  });
}

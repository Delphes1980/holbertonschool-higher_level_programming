// Get the element to be clicked
const clickHeader = document.getElementById('toggle_header');
// Get the element to be toggled
const toggledClass = document.querySelector('header');
// Check if both elements exist
if (clickHeader && toggledClass) {
  clickHeader.addEventListener('click', () => {
    // Check if the element is currently 'green'
    const isGreen = toggledClass.classList.contains('green');
    // Toggle 'green': add it if it isn't present, remove it if it is
    toggledClass.classList.toggle('green', !isGreen);
    // Toggle 'red': add it only if 'green' is present, remove it otherwise
    toggledClass.classList.toggle('red', isGreen);
  });
}

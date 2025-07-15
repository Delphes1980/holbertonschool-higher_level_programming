/* Ensure the script runs only after the HTML structure is fully loaded */
document.addEventListener('DOMContentLoaded', () => {
  // Get the element to put the value into
  const fetchHello = document.querySelector('#hello');
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
      if (response.ok) {
        return response.json();
      }
    })
    .then(value => {
      fetchHello.textContent = value.hello;
    });
});

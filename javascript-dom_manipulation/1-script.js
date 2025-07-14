const updatedHeader = document.getElementById('red_header');
// CHeck if the element exists before manupulating it
if (updatedHeader) {
  updatedHeader.addEventListener('click', () => {
    updatedHeader.style.color = '#FF0000';
  });
}

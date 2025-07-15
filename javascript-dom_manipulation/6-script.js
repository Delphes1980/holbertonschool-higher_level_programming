// Get the element to put the 'name' into
const fetchName = document.querySelector('#character');
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    // Check if the respons succeed
    if (response.ok) {
      return response.json();
    }
  })
  .then(data => {
    fetchName.textContent = data.name;
  });

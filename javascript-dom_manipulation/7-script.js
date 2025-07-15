// Get the element to put the list into
const fetchList = document.querySelector('ul#list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    if (response.ok) {
      return response.json();
    }
  })
  .then(data => {
  // Get the array of films from the 'results' property of the data
    const films = data.results;
    // Loop through the array
    films.forEach(film => {
    // Create a 'li' element for each film
      const listItem = document.createElement('li');
      listItem.textContent = film.title;
      fetchList.appendChild(listItem);
    });
  });

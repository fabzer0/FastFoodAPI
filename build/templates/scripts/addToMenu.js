const addToMenu = document.getElementById('add-to-menu-form');
addToMenu.addEventListener('submit', event => {
  const token = localStorage.getItem('token');
  event.preventDefault();
  fetch(`https://fast-food-fast-v2-api.herokuapp.com/api/v2/menu`, {
    method: 'post',
    body: JSON.stringify({
      meal_id: document.getElementById('mealid').value,
    }),
    headers: { 'Content-Type': 'application/json; charset=utf-8', 'x-access-token': token }
  })
  .then(response => response.json())
  .then(response => {
    console.log(response.message)
    if (response.message === 'meal has been updated successfully') {
      window.location.href = './add-edit-delete.html';
    }
  })
})

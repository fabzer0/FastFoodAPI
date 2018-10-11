const mealForm = document.getElementById('meal-form');

mealForm.addEventListener('submit', event => {
  const token = localStorage.getItem('token');
  event.preventDefault();
  fetch('https://fast-food-fast-v2-api.herokuapp.com/api/v2/meals', {
    method: 'post',
    body: JSON.stringify({
      mealname: document.getElementById('mealname').value,
      price: document.getElementById('mealprice').value
    }),
    headers: { 'Content-Type': 'application/json; charset=utf-8', 'x-access-token': token }
  })
  .then(response => response.json())
  .then(response => {
    console.log(response.message)
    if (response.message === 'meal successfully created') {
      window.location.href = './add-edit-delete.html';
    }
  })
})

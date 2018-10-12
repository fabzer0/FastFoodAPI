const editMealForm = document.getElementById('edit-meal-form');
editMealForm.addEventListener('submit', event => {
  const token = localStorage.getItem('token');
  const meal_id = sessionStorage.getItem('id');
  event.preventDefault();
  fetch(`https://fast-food-fast-v2-api.herokuapp.com/api/v2/meals/${meal_id}`, {
    method: 'put',
    body: JSON.stringify({
      mealname: document.getElementById('editmealname').value,
      price: document.getElementById('editmealprice').value,
      image: document.getElementById('editmealimage').value
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

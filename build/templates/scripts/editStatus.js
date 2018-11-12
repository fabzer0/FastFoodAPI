const editStatus = document.getElementById('edit-status-form');
editStatus.addEventListener('submit', event => {
  const token = localStorage.getItem('token');
  const meal_id = sessionStorage.getItem('id');
  event.preventDefault();
  fetch(`https://fast-food-fast-v2-api.herokuapp.com/api/v2/orders/${meal_id}`, {
    method: 'put',
    body: JSON.stringify({
      status: document.getElementById('thestatus').value
    }),
    headers: { 'Content-Type': 'application/json; charset=utf-8', 'x-access-token': token }
  })
  .then(response => response.json())
  .then(response => {
    console.log(response.message)
    if (response.message === 'order successfully updated') {
      window.location.href = './admin-accept-decline-orders.html';
    }
  })
})

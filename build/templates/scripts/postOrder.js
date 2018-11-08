const orderForm = document.getElementById('order-form');

orderForm.addEventListener('submit', event => {
  const token = localStorage.getItem('token');
  event.preventDefault();
  fetch('https://fast-food-fast-v2-api.herokuapp.com/api/v2/user/orders', {
    method: 'post',
    body: JSON.stringify({
      item: document.getElementById('item').value,
      quantity: document.getElementById('quantity').value
    }),
    headers: { 'Content-Type': 'application/json; charset=utf-8', 'x-access-token': token }
  })
  .then(response => response.json())
  .then(response => {
    console.log(response.message)
    if (response.message === 'order has been successfully added') {
      window.location.href = './user-order-food.html';
    }
  })
})


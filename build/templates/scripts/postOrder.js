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
      const orderBar = document.getElementById('meal-right-bar');

      let div = document.createElement('div');
      div.setAttribute('id', 'meal-in-cart-one');
      let p = document.createElement('p');
      let spanOne = document.createElement('span');
      spanOne.setAttribute('id', 'one');
      let spanTwo = document.createElement('span');
      spanTwo.setAttribute('id', 'two');
      let br = document.createElement('br');
      let spanThree = document.createElement('span');
      spanThree.setAttribute('id', 'three');
    
      
      spanThree.textContent = 'New';
      spanTwo.textContent = 'Ksh. 500';
      spanOne.textContent = 'Chapati';

      p.appendChild(spanOne);
      p.appendChild(spanTwo);
      p.appendChild(br);
      p.appendChild(spanThree);
      div.appendChild(p);

      orderBar.appendChild(div);
      
      window.location.href = './user-order-food.html';
    }
  })
})


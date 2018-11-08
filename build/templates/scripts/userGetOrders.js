const orders = document.getElementById('orders');
let br = document.createElement('br');
const token = localStorage.getItem('token');

// Getting the orders
fetch('https://fast-food-fast-v2-api.herokuapp.com/api/v2/user/orders', {
  method: 'get',
  headers: { 'Content-Type': 'application/json; charset=utf-8', 'x-access-token': token }
})
  .then(response => response.json())
  .then(response => {
    if (true) {
      response.forEach(orderItem => {
        let cartHolder = document.getElementById('cartholder');
        

        let spanOne = document.createElement('span');
        spanOne.setAttribute('id', 'one');
        spanOne.textContent = orderItem.item;

        let spanTwo = document.createElement('span');
        spanTwo.setAttribute('id', 'two');
        spanTwo.textContent = orderItem.price;

        let spanThree = document.createElement('span');
        spanThree.setAttribute('id', 'three');
        spanThree.textContent = orderItem.status;

        let spanFour = document.createElement('span');
        spanFour.setAttribute('id', 'four');
        spanFour.textContent = orderItem.price;

        cartHolder.appendChild(br);
        cartHolder.appendChild(spanOne);
        cartHolder.appendChild(spanTwo);
        cartHolder.appendChild(spanThree);
        cartHolder.appendChild(spanFour);

        orders.appendChild(cartHolder);
        console.log(response.message);
        console.log(data.message);
      });
    } else {
      console.log(response.message)
      const errorMessage = document.createElement('div');
      errorMessage.setAttribute('id', 'menu-error');
      errorMessage.textContent = response.message;
      mealColumn.appendChild(errorMessage);
    }
  })


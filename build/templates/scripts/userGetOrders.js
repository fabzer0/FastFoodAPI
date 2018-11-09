const orders = document.getElementById('orders');
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
        let cartHolder = document.createElement('div');
        cartHolder.setAttribute('id', 'cartholder');
        
        let br = document.createElement('br');
        let spanOne = document.createElement('span');
        spanOne.setAttribute('id', 'one');
        spanOne.textContent = orderItem.item;

        let spanTwo = document.createElement('span');
        spanTwo.setAttribute('id', 'two');
        spanTwo.textContent = 'Status: ' + orderItem.status;

        let spanThree = document.createElement('span');
        spanThree.setAttribute('id', 'three');
        spanThree.textContent = 'Total: ' + 'Ksh. ' + orderItem.totalprice;

        cartHolder.appendChild(br);
        cartHolder.appendChild(spanOne);
        cartHolder.appendChild(spanTwo);
        cartHolder.appendChild(spanThree);

        orders.appendChild(cartHolder);
      
      });
    } 
  })


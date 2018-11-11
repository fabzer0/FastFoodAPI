const orders = document.getElementById('user-orders');
const token = localStorage.getItem('token');

// Getting the orders
fetch('https://fast-food-fast-v2-api.herokuapp.com/api/v2/orders', {
  method: 'get',
  headers: { 'Content-Type': 'application/json; charset=utf-8', 'x-access-token': token }
})
  .then(response => response.json())
  .then(response => {
    if (true) {
      response.forEach(order => {
        let div = document.createElement('div');
        div.setAttribute('id', 'all-users');

        let br = document.createElement('br');

        let spanOne = document.createElement('span');
        spanOne.setAttribute('id', 'one');
        spanOne.textContent = 'Order: ' + order.item;

        let spanTwo = document.createElement('span');
        spanTwo.setAttribute('id', 'two');
        spanTwo.textContent = 'Total Price: ' + order.totalprice;

        let spanThree = document.createElement('span');
        spanThree.setAttribute('id', 'three');
        spanThree.textContent = 'Status: ' + order.status;

        let spanFour = document.createElement('span');
        spanFour.setAttribute('id', 'four');
        spanFour.textContent = 'Ordered By User ID: ' + order.user_id;

        let spanFive = document.createElement('span');
        spanFive.setAttribute('id', 'five');
        let buttonOne = document.createElement('button');
        buttonOne.textContent = 'Accept';
        spanFive.appendChild(buttonOne);

        let spanSix = document.createElement('span');
        spanSix.setAttribute('id', 'six');
        let buttonTwo = document.createElement('button');
        buttonTwo.textContent = 'Decline'
        spanSix.appendChild(buttonTwo);

        let spanSeven = document.createElement('span');
        spanSeven.setAttribute('id', 'seven');
        let input = document.createElement('input');
        let spanEight = document.createElement('span');
        spanEight.textContent = 'Mark as Complete';
        spanEight.setAttribute('id', 'eight');
        input.type = 'radio';
        spanSeven.appendChild(input);
        spanSeven.appendChild(spanEight);

        div.appendChild(br);
        div.appendChild(spanOne);
        div.appendChild(spanTwo);
        div.appendChild(spanThree);
        div.appendChild(spanFour);
        div.appendChild(br);
        div.appendChild(br);
        div.appendChild(spanFive);
        div.appendChild(spanSix);
        div.appendChild(spanSeven);

        orders.appendChild(div);
      });
    } 
  })


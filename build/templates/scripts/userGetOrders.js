const orders = document.getElementById('orders');
var request = new XMLHttpRequest();

// Getting the menu
request.open('GET', 'https://fast-food-fast-v2-api.herokuapp.com/api/v2/user/orders', true);
request.onload = function () {
    var data = JSON.parse(this.response);
    if (request.status >= 200 && request.status < 400) {
        data.forEach(order => {
            let cartHolder = document.getElementById('cartholder');
            let br = document.createElement('br');

            let spanOne = document.createElement('span');
            spanOne.setAttribute('id', 'one');
            spanOne.textContent = order.mealname;

            let spanTwo = document.createElement('span');
            spanTwo.setAttribute('id', 'two');
            spanTwo.textContent = order.quantity;

            let spanThree = document.createElement('span');
            spanThree.setAttribute('id', 'three');
            spanThree.textContent = order.status;

            let spanFour = document.createElement('span');
            spanFour.setAttribute('id', 'four');
            spanFour.textContent = order.price;

            cartHolder.appendChild(br);
            cartHolder.appendChild(spanOne);
            cartHolder.appendChild(spanTwo);
            cartHolder.appendChild(spanThree);
            cartHolder.appendChild(spanThree);

            orders.appendChild(cartHolder);
        });
    } else {
      const errorMessage = document.createElement('div');
      errorMessage.setAttribute('id', 'menu-error');
      errorMessage.textContent = data.message;
      menuColumn.appendChild(errorMessage);
    }
}
request.send();

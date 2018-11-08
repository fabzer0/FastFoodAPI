const menuColumn = document.getElementById('meal-center-main-three');
var request = new XMLHttpRequest();

// Getting the menu
request.open('GET', 'https://fast-food-fast-v2-api.herokuapp.com/api/v2/menu', true);
request.onload = function () {
    var data = JSON.parse(this.response);
    if (request.status >= 200 && request.status < 400) {
        data.forEach(menuItem => {
            let menu = document.createElement('div');
            menu.setAttribute('id', 'meals');

            let menuImage = document.createElement('div');
            menuImage.setAttribute('class', 'meal-image');

            let img = document.createElement('img');
            img.src = menuItem.image;

            menu.appendChild(menuImage);
            menuImage.appendChild(img);

            let menuCreds = document.createElement('div');
            menuCreds.setAttribute('class', 'meal-creds');

            menu.appendChild(menuCreds);

            let lineBreaker = document.createElement('br');
            let p = document.createElement('p');
            let span = document.createElement('span');
            span.textContent = menuItem.mealname;
            let secondSpan = document.createElement('span');
            secondSpan.textContent = 'Ksh.' + ' ' + menuItem.price;
            let thirdSpan = document.createElement('span');
            thirdSpan.setAttribute('id', 'add-to-cart');
            let button = document.createElement('button');
            button.setAttribute('id', 'addcart')
            button.textContent = 'Add To Cart';
            button.setAttribute('onclick', "location.href = 'input-order.html';"
            )

            menuCreds.appendChild(lineBreaker);
            menuCreds.appendChild(p);
            p.appendChild(span);
            p.appendChild(lineBreaker);
            p.appendChild(secondSpan);
            p.appendChild(thirdSpan);
            thirdSpan.appendChild(button);

            menuColumn.appendChild(menu);
        });
    } else {
      const errorMessage = document.createElement('div');
      errorMessage.setAttribute('id', 'menu-error');
      errorMessage.textContent = data.message;
      menuColumn.appendChild(errorMessage);
    }
}
request.send();

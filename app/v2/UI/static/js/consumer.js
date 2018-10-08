const menu = document.getElementById('meals');
const menuImage = document.createElement('div');
menuImage.setAttribute('class', 'meal-image');

const img = document.createElement('img');
img.src = 'static/css/img/milk_tea.jpeg';

menu.appendChild(menuImage);
menuImage.appendChild(img);

const menuCreds = document.createElement('div');
menuCreds.setAttribute('class', 'meal-creds');

menu.appendChild(menuCreds);

var request = new XMLHttpRequest();
request.open('GET', 'localhost:5000/api/v2/menu', true);
request.onload = function () {
    var data = JSON.parse(this.response);
    if (request.status >= 200 && request.status < 400) {
        data.forEach(menuItem => {

            let lineBreaker = document.createElement('br');
            let p = document.createElement('p');
            let span = document.createElement('span');
            span.textContent = menuItem.mealname;
            let secondSpan = document.createElement('span');
            secondSpan.textContent = menuItem.price;
            let thirdSpan = document.createElement('span');
            thirdSpan.setAttribute('id', 'add-to-cart');
            let button = document.createElement('button');
            button.textContent = 'Add To Cart';

            menuCreds.appendChild(lineBreaker);
            menuCreds.appendChild(p);
            p.appendChild(span);
            p.appendChild(lineBreaker);
            p.appendChild(secondSpan);
            p.appendChild(thirdSpan);
            thirdSpan.appendChild(button);
        });
    }
}
request.send();

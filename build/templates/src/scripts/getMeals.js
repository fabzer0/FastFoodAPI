const mealColumn = document.getElementById('all-orders');
var request = new XMLHttpRequest();

// Getting the meals
request.open('GET', 'https://fast-food-fast-v2-api.herokuapp.com/api/v2/meals', true);
request.onload = function () {
    var data = JSON.parse(this.response);
    if (request.status >= 200 && request.status < 400) {
        data.forEach(mealItem => {
            let mealImage = document.createElement('div');
            mealImage.setAttribute('class', 'meal-a-img');
            let img = document.createElement('img');
            img.src = 'styles/img/chapati-chiken.jpg';

            mealImage.appendChild(img);
            mealColumn.appendChild(mealImage);

            let mealsCred = document.createElement('div');
            mealsCred.setAttribute('class', 'meal-a-cred');
            let p = document.createElement('p');
            let firstSpan = document.createElement('span');
            firstSpan.textContent = mealItem.mealname;
            let br = document.createElement('br');
            let secondSpan = document.createElement('span');
            secondSpan.textContent = mealItem.price;
            let thirdSpan = document.createElement('span');
            thirdSpan.setAttribute('id', 'accept');
            let buttonOne = document.createElement('button');
            let a = document.createElement('a');
            a.href = 'edit-meal-form.html';
            a.textContent = 'Edit';
            let fourthSpan = document.createElement('div');
            fourthSpan.setAttribute('id', 'decline');
            let buttonTwo = document.createElement('button');
            buttonTwo.textContent = 'Delete';
            let fifthSpan = document.createElement('div');
            fifthSpan.setAttribute('id', 'menu');
            let buttonThree = document.createElement('button');
            buttonThree.textContent = '+ Menu';

            fifthSpan.appendChild(buttonThree);
            fourthSpan.appendChild(buttonTwo);
            buttonOne.appendChild(a);
            thirdSpan.appendChild(buttonOne);

            p.appendChild(firstSpan);
            p.appendChild(br);
            p.appendChild(secondSpan);
            p.appendChild(br);
            p.appendChild(br);
            p.appendChild(thirdSpan);
            p.appendChild(fourthSpan);
            p.appendChild(fifthSpan);

            mealsCred.appendChild(p);
            mealColumn.appendChild(mealsCred);
              
        });
    } else {
      const errorMessage = document.createElement('div');
      errorMessage.setAttribute('id', 'menu-error');
      errorMessage.textContent = data.message;
      mealColumn.appendChild(errorMessage);
    }
}
request.send();

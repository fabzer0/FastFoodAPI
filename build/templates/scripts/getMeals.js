const mealColumn = document.getElementById('all-orders');
const token = localStorage.getItem('token');

// Getting the meals
fetch('https://fast-food-fast-v2-api.herokuapp.com/api/v2/meals', {
  method: 'get',
  headers: { 'Content-Type': 'application/json; charset=utf-8', 'x-access-token': token }
})
  .then(response => response.json())
  .then(response => {
    if (true) {
      response.forEach(mealItem => {
        let mealImage = document.createElement('div');
        mealImage.setAttribute('class', 'meal-a-img');
        let img = document.createElement('img');
        img.src = mealItem.image;

        mealImage.appendChild(img);
        mealColumn.appendChild(mealImage);

        let mealsCred = document.createElement('div');
        mealsCred.setAttribute('class', 'meal-a-cred');
        let p = document.createElement('p');
        let firstSpan = document.createElement('span');
        firstSpan.textContent = mealItem.mealname;
        let br = document.createElement('br');
        let secondSpan = document.createElement('span');
        secondSpan.textContent = ' Ksh.' + ' ' + mealItem.price;
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
        let a2 = document.createElement('a');
        a2.href = 'add-to-menu';
        a.textContent = 'Add To Menu';

        buttonThree.appendChild(a2);
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
      console.log(response.message)
      const errorMessage = document.createElement('div');
      errorMessage.setAttribute('id', 'menu-error');
      errorMessage.textContent = response.message;
      mealColumn.appendChild(errorMessage);
    }
  })

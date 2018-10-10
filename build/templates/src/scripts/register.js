const regForm = document.getElementById('register-form');

regForm.addEventListener('submit', event => {
  event.preventDefault();
  fetch('https://fast-food-fast-v2-api.herokuapp.com/api/v2/auth/signup', {
    method: 'post',
    body: JSON.stringify({
      username: document.getElementById('username').value,
      email: document.getElementById('email').value,
      password: document.getElementById('password').value,
      confirm_password: document.getElementById('confirm-password').value
    }),
    headers: { 'Content-Type': 'application/json; charset=utf-8' }
  })
    .then(response => response.json())
    .then(response => {
      alert(response.message);
      if (response.message === 'you are successfully registered') {
        window.location.href = './login.html';
      }
    });

})

const regForm = document.getElementById('register-form');
const hostSucess = document.getElementById('one');
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
      console.log(response.message)
      let resMessage = document.getElementById('reg-alert');
      resMessage.textContent = response.message;
      resMessage.style.display = 'block'; 
    });

})

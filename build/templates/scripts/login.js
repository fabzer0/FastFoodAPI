const loginForm = document.getElementById('login-form');
loginForm.addEventListener('submit', event => {
  event.preventDefault();
  fetch('https://fast-food-fast-v2-api.herokuapp.com/api/v2/auth/login', {
    method: 'post',
    body: JSON.stringify({
      email: document.getElementById('my-email').value,
      password: document.getElementById('my-password').value
    }),
    headers: { 'Content-Type': 'application/json; charset=utf-8' }
  })
    .then(response => response.json())
    .then(response => {
      console.log(response.message)
      if (response.token) {
        localStorage.setItem('token', response.token);
        if (response.message === 'login was successful') {
          window.location.href = './user-order-food.html';
        } else {
          let hiddenMessage = document.getElementById('log-alert');
          hiddenMessage.textContent = response.message;
          hiddenMessage.style.display = 'block';
        }   
      }
    });
})

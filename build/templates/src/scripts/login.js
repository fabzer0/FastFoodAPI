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
      if (response.token) {
        localStorage.setItem('token', response.token);
        window.location.href = './user-order-food.html';
      }
    });
})

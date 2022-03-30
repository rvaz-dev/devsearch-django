//handle token logic

let form = document.getElementById('login-form')
// add event listener
form.addEventListener('submit', (e) => {
    e.preventDefault()
    
    let formData = {
        'username': form.username.value,
        'password': form.password.value
    }
    
    fetch('http://127.0.0.1:8000/api/users/token/', {
        method: 'POST',
        headers: {
                'Content-Type': 'application/json',

        },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            console.log('DATA:', data.access)
            if (data.access) {
                localStorage.setItem('token', data.access)
                window.location = 'file:///D:/Python%20Django%202021/Django-2021-Meu/frontend/projects.html'
            } else {
                alert('Username Or Password did not work, Try again!')
            }
        })

})
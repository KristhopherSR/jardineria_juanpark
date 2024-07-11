document.getElementById('registerForm').addEventListener('submit', function(event) {
    let password1 = document.getElementById('password1').value;
    let password2 = document.getElementById('password2').value;

    if (password1 !== password2) {
        event.preventDefault();
        alert('Las contraseñas no coinciden');
    }
});

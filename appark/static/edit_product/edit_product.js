document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const nombreInput = document.getElementById('nombre');
    const descripcionTextarea = document.getElementById('descripcion');
    const precioInput = document.getElementById('precio');

    form.addEventListener('submit', function(event) {
        let isValid = true;
        let errorMessage = '';

        if (nombreInput.value.trim() === '') {
            isValid = false;
            errorMessage += 'El campo de nombre es obligatorio.\n';
        }

        if (descripcionTextarea.value.trim() === '') {
            isValid = false;
            errorMessage += 'El campo de descripción es obligatorio.\n';
        }

        if (precioInput.value.trim() === '' || parseFloat(precioInput.value) <= 0) {
            isValid = false;
            errorMessage += 'El campo de precio es obligatorio y debe ser un valor positivo.\n';
        }

        if (!isValid) {
            alert(errorMessage);
            event.preventDefault();
        }
    });
});

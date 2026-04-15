// La URL la obtendremos después de desplegar API Gateway con Terraform
const apiUrl = 'TU_URL_DE_API_GATEWAY_AQUI/visits';

async function getVisitCount() {
    try {
        const response = await fetch(apiUrl, {
            method: 'POST' // Usamos POST para que la Lambda incremente el contador
        });
        const data = await response.json();
        document.getElementById('counter').innerText = data.count;
    } catch (error) {
        console.error('Error al obtener el contador:', error);
        document.getElementById('counter').innerText = 'Error';
    }
}

// Llamamos a la función apenas cargue la página
getVisitCount();
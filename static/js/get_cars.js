const div = document.querySelector('#cars');
const table = div.querySelector('.table');
const tbody = table.querySelector('tbody');

document.addEventListener('DOMContentLoaded', async () => {

    let res;
    try {
        res = await fetch('/cars', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
    } catch {
        alert('An error happened');
        return;
    }

    const json = await res.json();

    if (res.status != 200) {
        alert(await json.message);
        return;
    }

    const carsList = await json.cars;
    carsList.forEach(car => {
        tbody.innerHTML += `
        <tr>
            <td>${car.id}</td>
            <td>${car.color}</td>
            <td>${car.model}</td>
            <td>${car.owner.name}</td>
            <td>${car.owner.email}</td>
            <td>${car.created_at}</td>
            <td>
                <a 
                href="/app/car/update/${car.id}"
                class="btn btn-primary" 
                id="update-car">Update</a>
            </td>
        </tr>
        `;
    });
    
});
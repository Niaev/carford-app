const div = document.querySelector('#owners');
const form = div.querySelector('form');
const ownerId = parseInt(window.location.href.split('/').at(-1));
const name = form.querySelector('#name');
const email = form.querySelector('#email');
const phone = form.querySelector('#phone');
const btn = form.querySelector('#btn-update');
const deleteBtn = form.querySelector('#btn-delete');
const table = div.querySelector('.table');
const tbody = table.querySelector('tbody');

document.addEventListener('DOMContentLoaded', async () => {

    let res;
    try {
        res = await fetch(`/owners/${ownerId}`, {
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
        window.location = '/app/owners';
        return;
    }

    const owner = await json.owner;
    name.value = owner.name;
    email.value = owner.email;
    phone.value = owner.phone;

    owner.cars.forEach(car => {
        tbody.innerHTML += `
        <tr>
            <td>${car.id}</td>
            <td>${car.color}</td>
            <td>${car.model}</td>
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

btn.addEventListener('click', async (e) => {

    e.preventDefault();

    let res
    try {
        res = await fetch('/owners/update', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: ownerId,
                name: name.value,
                email: email.value,
                phone: phone.value
            })
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

    window.location = '/app/owners';

});


deleteBtn.addEventListener('click', async (e) => {

    e.preventDefault();

    const confirmation = confirm('Are you sure you want to delete this owner?');

    if (!confirmation) return;

    let res;
    try {
        res = await fetch('/owners/delete', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: ownerId
            })
        })
    } catch {
        alert('An error happened');
        return;
    }

    const json = await res.json();

    if (res.status != 200) {
        alert(await json.message);
        return;
    }

    window.location = '/app/owners';

});
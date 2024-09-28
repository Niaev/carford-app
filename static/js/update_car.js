const div = document.querySelector('#cars');
const form = div.querySelector('form');
const carId = parseInt(window.location.href.split('/').at(-1));
const color = form.querySelector('#color');
const model = form.querySelector('#model');
const ownerId = form.querySelector('#owner_id');
const btn = form.querySelector('#btn-update');
const deleteBtn = form.querySelector('#btn-delete');

document.addEventListener('DOMContentLoaded', async () => {

    let res;
    try {
        res = await fetch(`/cars/${carId}`, {
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
        window.location = '/app/cars';
        return;
    }

    const car = await json.car;
    color.value = car.color;
    model.value = car.model;
    ownerId.value = car.owner.id;
});

btn.addEventListener('click', async (e) => {

    e.preventDefault();

    let res
    try {
        res = await fetch('/cars/update', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: carId,
                color: color.value,
                model: model.value,
                owner_id: parseInt(ownerId.value)
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

    window.location = '/app/cars';

});


deleteBtn.addEventListener('click', async (e) => {

    e.preventDefault();

    const confirmation = confirm('Are you sure you want to delete this car?');

    if (!confirmation) return;

    let res;
    try {
        res = await fetch('/cars/delete', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: carId
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

    window.location = '/app/cars';

});
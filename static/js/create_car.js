const div = document.querySelector('#cars');
const form = div.querySelector('form');
const color = form.querySelector('#color');
const model = form.querySelector('#model');
const ownerId = form.querySelector('#owner_id');
const btn = form.querySelector('#btn-create');

btn.addEventListener('click', async (e) => {

    e.preventDefault();

    let res
    try {
        res = await fetch('/cars/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
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

const div = document.querySelector('#owners');
const form = div.querySelector('form');
const name = form.querySelector('#name');
const email = form.querySelector('#email');
const phone = form.querySelector('#phone');
const btn = form.querySelector('#btn-create');

btn.addEventListener('click', async (e) => {

    e.preventDefault();

    let res
    try {
        res = await fetch('/owners/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
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

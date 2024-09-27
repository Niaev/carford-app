const div = document.querySelector('#signup');
const form = div.querySelector('form');
const name = form.querySelector('#name');
const email = form.querySelector('#email');
const pwd = form.querySelector('#pwd');
const cpwd = form.querySelector('#cpwd');
const btn = form.querySelector('#btn-signup');

btn.addEventListener('click', async (e) => {

    e.preventDefault();

    if (pwd.value != cpwd.value) {
        alert('Password don\'t match!');
    }

    const hash = sha256(pwd.value);

    const res = await fetch('/users/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: name.value,
            email: email.value,
            password: hash,
            confirm_password: hash
        })
    });

    /*let res;
    try {
        res = await fetch('/users/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: name.value,
                email: email.value,
                password: hash,
                confirm_password: hash
            })
        });
    } catch {
        alert('An error happened');
        return;
    }*/

    const json = await res.json()

    if (res.status != 200) {
        alert(json.message);
        return;
    }

    window.location = '/app/login';

});

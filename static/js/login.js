const div = document.querySelector('#login');
const form = div.querySelector('form');
const email = form.querySelector('#email');
const pwd = form.querySelector('#pwd');
const btn = form.querySelector('#btn-login');

btn.addEventListener('click', async (e) => {

    e.preventDefault();

    const hash = sha256(pwd.value);

    let res
    try {
        res = await fetch('/users/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email.value,
                password: hash
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

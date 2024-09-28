const div = document.querySelector('#owners');
const table = div.querySelector('.table');
const tbody = table.querySelector('tbody');

document.addEventListener('DOMContentLoaded', async () => {

    let res;
    try {
        res = await fetch('/owners', {
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

    const ownersList = await json.owners;
    ownersList.forEach(owner => {
        let nCarsCell = `${owner.number_of_cars}`;
        if (owner.number_of_cars == 0) {
            nCarsCell = '<span class="badge text-bg-success">Sale opportunity!</span>';
        }

        tbody.innerHTML += `
        <tr>
            <td>${owner.id}</td>
            <td>${owner.name}</td>
            <td>${owner.email}</td>
            <td>${owner.phone}</td>
            <td>${nCarsCell}</td>
            <td>${owner.created_at}</td>
            <td>
                <a 
                href="/app/owner/update/${owner.id}"
                class="btn btn-primary" 
                id="update-owner">Update</a>
            </td>
        </tr>
        `;
    });
    
});
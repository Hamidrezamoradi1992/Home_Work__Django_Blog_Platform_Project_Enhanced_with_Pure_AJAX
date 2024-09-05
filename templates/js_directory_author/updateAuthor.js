function update_author(value) {
    fetch(`api/author/${value.value}`, {
        method: "GET",
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
        .then(async request => {
            const r = await request.json()
            console.log(r)
            updateEL.innerHTML = `<form action="" id="forms_update" class="grid grid-row3 flex align-center justify-center ">
                         <input
                                type="text"
                                 placeholder=""
                                 name="name"
                                 value="${r.name}""
                                 class="input input-bordered input-primary w-full max-w-xs"/>
                         <textarea class="textarea" name="bio" placeholder="Description">${r.bio}</textarea>
                         <input class="input input-bordered input-primary w-full max-w-xs" type="email" value="${r.email}" name="email">
                         <input class="input input-bordered input-primary w-full max-w-xs"  disabled name="created_at" value="${r.created_at}">
                         <button onclick="update_au(this)" value="${r.id}" class="btn btn-success">update</button>
                     </form>`
            formEL.classList.toggle("!hidden");
            updateEL.classList.toggle("!hidden");
        }).catch((error) => {
        alert(error)
    })
}

function update_au(value) {
    let formUpdateEL = document.querySelector('#forms_update');
    formUpdateEL.addEventListener('submit', (event) => {
        event.preventDefault()
        if (confirm("Are you sure about this?")) {
            let form = event.target;
            console.log(form.title)
            console.log(form.description)
            let data = new FormData(form);
            console.log()
            fetch(`api/author/${value.value}`, {
                method: "PUT",
                body: data,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': '{{ csrf_token }}'
                },
            }).then(async result => {
                await result
            }).finally(() => {
                updateEL.classList.toggle("!hidden");
                diveFormPostEl.classList.toggle('!hidden')
                loaded();
            })
        } else {
            updateEL.classList.toggle("!hidden");
            diveFormPostEl.classList.toggle('!hidden')
            formEL.classList.toggle('!hidden');
        }
    })
}



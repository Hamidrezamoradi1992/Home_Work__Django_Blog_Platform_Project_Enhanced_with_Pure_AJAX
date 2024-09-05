formEL.addEventListener('submit', function (event) {
    event.preventDefault();
    let form = event.target;
    let data = new FormData(form)
    console.log(form.name)
    console.log(form.email)
    if ((!(form.name.value === "")) && (!(form.email.value === ""))) {

        fetch(`{% url "create_author"%}`, {
            method: "POST",
            body: data,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': '{{ csrf_token }}'
            },
        }).then(async result => {
            await result
        }).finally(() => {
            formEL.classList.toggle("!hidden")
            diveFormPostEl.classList.toggle('!hidden')
            loaded();

        })
    }
});
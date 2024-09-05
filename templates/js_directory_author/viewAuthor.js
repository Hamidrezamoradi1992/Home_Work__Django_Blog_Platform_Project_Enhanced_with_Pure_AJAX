function viewAuthorDetail(value) {
    formEL.classList.toggle('!hidden');
    fetch(`api/author/${value.value}`, {
        method: "GET",
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': '{{ csrf_token }}'
        }
    }).then(async response => {
        const data = await response.json();
        mainView.innerHTML = ""
        console.log(data)
        viewDetailEL.innerHTML = `
                  <div class="pr-10 pl-10 ">
                      <h1 class="text-5xl m-auto justify-center text-center">${data.name}</h1>

                      <p class="mt-4">${data.bio}</p>
                      <p class="mt-4">${data.email}</p>
                      <p class="mt-4">${data.created_at}</p>
                  <div/>
                  <div class="flex justify-center aline-center mt-40">
                       <button onclick="loaded()" class="btn btn-active btn-secondary">back</button>
                  <div/>
              `

    })
}
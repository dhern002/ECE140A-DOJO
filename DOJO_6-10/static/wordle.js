document.addEventListener("DOMContentLoaded", (event) => {
    let create_account_form = document.querySelector('form[action="/create-account"]');
    let log_in_form = document.querySelector('form[action="/log-in"]');
    let create_account_button = document.querySelector('#create');
    let log_in_button = document.querySelector('#login');
    let aForm = false;
    console.log(event, "We are ready to plaY!");
    create_account_button.addEventListener("click", (event) => {
        aForm = true;
       console.log("Create account");
       create_account_form.style.display = 'block';
       event.target.style.display = 'none';
       log_in_button.style.display = 'none';
    });

    log_in_button.addEventListener("click", (event) => {
        aForm = true;
       console.log("log in");
       log_in_form.style.display = 'block';
       event.target.style.display = 'none';
       create_account_button.style.display = 'none';
    });

    create_account_form.addEventListener("submit", (event) => {
       event.preventDefault();
        const data = Object.fromEntries(new FormData(event.target).entries());
        fetch('/users', {
            method: "POST",
            body: JSON.stringify(data),
            headers: {'Content-Type': 'application/json'}
        }).then((response) => {
            if(response.status === 418) {
                alert("Username or Email is already in use! (I'm a teapot!)");
            }
        });
    });

    log_in_form.addEventListener("submit", (event) => {
        event.preventDefault();
        const data = Object.fromEntries(new FormData(event.target).entries());
        fetch('/login', {
            method: "POST",
            headers: {
                'X-sent-by': 'My wordle game',
                'Content-type': 'application/json'
            },
            body: JSON.stringify(data)
        }).then((response) => {
            if(response.status === 401) {
                event.target.reset();
                alert("Username or password incorrect!");
            }
        });
    });

    document.addEventListener("keydown", (event) => {
        if(event.key === "Escape" && aForm === true) {
            create_account_form.style.display = 'none';
            log_in_form.style.display = 'none';
            log_in_button.style.display = 'block';
            create_account_button.style.display = 'block';
            aForm = false;
        }
    })
})
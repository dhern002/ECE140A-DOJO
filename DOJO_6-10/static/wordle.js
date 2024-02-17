document.addEventListener("DOMContentLoaded", (event) => {
    let create_account_form = document.querySelector('form[action="/create-account"]');
    let log_in_form = document.querySelector('form[action="/log-in"]');
    let create_account_button = document.querySelector('#create');
    let log_in_button = document.querySelector('#login');
    console.log(event, "We are ready to plaY!");
    create_account_button.addEventListener("click", (event) => {
       console.log("Create account");
       create_account_form.style.display = 'block';
       event.target.style.display = 'none';
       log_in_button.style.display = 'none';
    });

    log_in_button.addEventListener("click", (event) => {
       console.log("log in");
       log_in_form.style.display = 'block';
       event.target.style.display = 'none';
       create_account_button.style.display = 'none';
    });

    create_account_form.addEventListener("submit", (event) => {
       event.preventDefault();
       console.log(event.target);
       let username = event.target.querySelector('input[type="text"]').value;
       let password = event.target.querySelector('input[type="password"]').value;
        let data = {'username': username, 'password': password};
        fetch('/create-user', {
            method: "POST",
            body: JSON.stringify(data)
        }).then((response) => response.json())
        .then((data) => {
            console.log(data);
        });
       console.log(username.value);
       console.log(password.value);
    });

    log_in_form.addEventListener("submit", (event) => {
        event.preventDefault();
        console.log(event.target);
        let username = event.target.querySelector('input[type="text"]').value;
        let password = event.target.querySelector('input[type="password"]').value;
        let data = {'username': username, 'password': password};
        localStorage.setItem("WordleAuth", "hi123123123123");
        fetch('/login', {
            method: "POST",
            headers: {
                "Authorization": localStorage.getItem("WordleAuth"),
                "X-sent-by": "My wordle game"
            },
            body: JSON.stringify({"hi": "hi"})
        });
    });
})
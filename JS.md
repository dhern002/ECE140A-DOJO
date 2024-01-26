# DOJO

## Javascript:
Wouldn't it be nice if we could add interactivity to our website? Well we can! We will be using javascript to add 
interactivity to our website. We will be using javascript to make requests to our backend dynamically update our website.

### Fetch:
Fetch is a way to make requests in javascript. It is a function that takes in a url and returns a promise.
```javascript
fetch("http://localhost:8000/notes")
.then(response => response.json()) //promise chaining then happens when the previous promise is resolved
.then(data => console.log(data))
.catch(error => console.log(error))
```

### Promises:
Promises are a way to handle asynchronous code. They are a way to handle code that takes a long time to run. You define
what happens when the promise is resolved and what happens when the promise is rejected. 
```javascript
const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Hello World")
    }, 1000)
})
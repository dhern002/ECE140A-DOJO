# DOJO

## Javascript:
Wouldn't it be nice if we could add functionality to our website? Well we can! We will be using javascript to add 
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
    }, 1000) // This promise will resolve after 1 second
})
```

### Await:
Await is a way of handling promises. It is used to block the current scope until the promise is resolved. An example can be
seen below: While we wait for the promise to resolve, we can't do anything else. This is why we need to use async functions
if we want to continue execution while we wait for the promise to resolve.
```javascript
const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Hello World")
    }, 1000) // This promise will resolve after 1 second
})

const result = await promise // This will block the current scope until the promise is resolved
```

### Async:
Async is a way to define a function that will be executed asynchronously. This means that the function will be executed
in the background, perhaps when a certain event happens. This is useful when we want to continue execution while we wait.
You define what you would like to happen when the promise is resolved inside the then block.
```javascript
async function main() {
    const promise = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Hello World")
        }, 1000) // This promise will resolve after 1 second
    })
    
    promise.then(result => console.log(result)) //this will be executed after the promise is resolved
}
```

### Event Listeners:
Event listeners are a way to define what happens when an event happens. An event can be a click, a key press, or a mouse
movement. You can define what happens when an event happens by using event listeners. 
```javascript
const button = document.getElementById("button") // This gets the button element from the html
button.addEventListener("click", () => { // This adds an event listener to the button that listens for a click
    console.log("Hello World")
})
```

Important one is the DOMContentLoaded event. This event is fired when the DOM is loaded. This is useful when you want to
run some code after the DOM is loaded. You would need elements to be loaded before you can query them and manipulate them.
DOMContentLoaded is a way to ensure that the DOM is loaded before you run your code.
```javascript
document.addEventListener("DOMContentLoaded", () => {
    console.log("Hello World")
})
```

### DOM Manipulation:
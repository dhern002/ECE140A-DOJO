# DOJO 1

## Web Serving:
How does websites work? Let's find out!
### Routing:
To reach a website, you need to know the ip address of the server. This is 0.0.0.0 for a server that is running on 
your local machine. But what about other websites?
```bash
ping google.com
```
After google.com you will see an ip address. This is the ip address of the server that is hosting google.com. For 
a server to be accessible from the internet, it needs to have a public ip address. Which is one of the reasons why
google.com is accessible from us but your local server is not.
### Ports:
What is that number after the up address? That is the port number. A port is a communication endpoint. A number that is
associated with a process. It is the final layer of the address to reach something on a network. Imagine your apartment
number in your apartment building. The building is the ip address, the apartment number is the port number.

80 is the default port for http. 8000, 6543, 5000 are common ports for web servers.

#### Port Accessibility:
Ports are not accessible from the internet by default. You need to open them up. This is done by configuring your router
to forward traffic from a port to a specific ip address. This is called port forwarding. This is another reason
why you can't access your local server from the internet. Your router is not configured to forward traffic from port 
8000 to your local ip

### Request and Response:
When you type in a url in your browser and hit enter, you are sending a request to the server. The server will then
send a response back to you. This is the request and response cycle. There is a lot of requests and responses happening
in modern web applications. You can observe these requests in the network tab of your browser's developer tools.

You can make your very own requests using curl. 
```bash
curl www.google.com
```

### Making our own server:
We talked about how does the internet work, now lets discuss how to connect our own python code to the internet. We will
be using fast api to create our own server. Fast api allows you to define what happens when a request is made to a specific
url. A lot of the complicated stuff is handled for you by uvicorn and fast api. 
#### Uvicorn:
Uvicorn handles the port forwarding and the request and response cycle. It is a web server that is written in python. It
opens up a port and listens for requests. When a request is made, it will send the request to the fast api application.
#### Fast API:
Fast api is a python framework for creating web servers. It allows you to define what happens when a request is made to a
specific url. It also allows you to define what the response will be. It is a very powerful framework that is easy to use.
##### Decorators:
Decorators are a way to modify the behavior of a function. They are a way to wrap a function with another function. Fast 
api uses decorators to define which requests will be handled by which functions. 
```python
@app.get("/") # This is a decorator forwards the get request to the root url to the root function
def root():
    return {"message": "Hello World"}
```
##### Side Note:
You need to install fast api and uvicorn to run the server. You can do this by running the following command:
```bash
pip install fastapi uvicorn
```





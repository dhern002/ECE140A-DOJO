# DOJO 1

## Fast API:
We talked about basics of python, web serving, and fast api. Now lets put it all together and create our own server.
Goal is to create a website that will show people how to create a website themselves. Tune in next week for more info
to add to the website, and eventually we will deploy it to the internet but for now lets start with the basics. 
### Creating a Fast API application:
We will provide a skeleton for you to start with. You can find this in main.py. Routes to build:
* [get] /: This will be the home page. This page should have a navigation bar with links to the other pages and a brief description of the website.
* [get] /basics: This page will include information from basics.md
* [get] /web_serving: This page will include information from web_serving.md
* [get] /web_development: This page will include information from web_development.md
* [get] /view_notes: This page will include a text box to add notes
* [get] /notes: This will return all the notes that have been created.
* [post] /notes: This will send a new note to the backend.

### Serving static files:
We will be serving 2 static files, a css file and a js file. These files will be in the static directory. 
CSS file will be used to style the website. JS file will be used to add functionality to the website.
* static/css/style.css
* static/js/script.js

### Templates:
The html files will be in the templates' directory. We will serve these files using fast api.
* templates/index.html
* templates/basics.html
* templates/web_serving.html
* templates/fast_api.html
* templates/web_development.html
* templates/notes.html

### Notes:
We are going to use javascrit to add functionality to the website. We will be using fetch to make a post request to send
our notes and a get request to get our notes. Notes will be stored in a file called notes.txt.


### Fast API decorators:
We have included the decorators for the / and /notes routes. You will need to add the other routes. Create 3 more functions
for basics page, web serving page, and web development page. Add the apporiate decorators to these functions. 


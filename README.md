## Overview

Working through the series here: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Everything in this specific section has come from the aforementioned tutorials built by Miguel Grinberg (he also has a great book: 


## General set-up

- Working on ubuntu 16.04, specificlally with Python 3.6.8 so I can use Heroku later

- Working in virtual environment called `venv`: `virtualenv -p python3 venv`

- requirements.txt file includes all dependencies 


## Overview of Files: 

### app/__init__.py:

- Our init file is going to create the application object as an instance of class `Flask`
- 


### app/routes.py: 

- This is going to help us orchestrate the different URLs that our application implements 
- Handlers for application routes are written as python functions, called `view functions`. These are mapped to one or more route URLs so Flask knows the logic to execute when a client requests a given URL. 
- understanding `@app.route`:
    - this is a decorator modifying the function following it. 
    - this decorator specifically is going to create an association between the URL given as an argument and the function provided. 
    - so when a web browser requests the associated URL (like `/index`) Flask is going to invoke a function & pass the return value back to the browser as a response. 

#### /login

- This is where we generate out WTForm for logging in
- Methods included are: 
    - GET: This tends to return information to the client (web browser in our case)
    - POST: Submits form data to the server, which is what should happen when the user clicks "Submit" Failure to do this will send a "Method Not Allowed" error since browser tries sending a POST request when our application was not configured to actually accept this. 


### microblog.py: 

- Main application

- Need the following environmental variable: 

    - `export FLASK_APP=microblog.py`

- Running our application: 
    - `flask run`

### app/templates/:

#### template inheritance: base.html
- `block` is a control statement to define where other templates are able to be inserted 

- we can inherit this into other templates, which means we can simplify a lot of our other HTML templates. 

#### index.html: 

- this is just a basic HTML template 
- `{{...}}` indicates we canpull in a variable during runtime, so when we see `{{user.username}}` this means that there will be a corresponding python object wit this info. In this case, we are dealing with a python dictionary
- We can also use `render_template` from flask to read this specific .html file in for a specific URL.
-The `render_template()` function invokes the Jinja2 template engine that comes bundled with the Flask framework. Jinja2 substitutes `{{ ... }}` blocks with the corresponding values, given by the arguments provided in the `render_template()` call.

#### index_for_loops.html: 

- We increase the complexity slightly, allowing for a few more objects to be passed in as well as loops

- We use some control logic such as `{% if title %}` which is going let us check if a `title` object has been specified; if not ewe move to the else which just has a default value not expecting a specific `title` object. 

- We can also add in some for loops: we just loop over a list of dictionaries

#### index_inherit.html: 

- this is an example where we inherit the `base.html` file providing the general welcome, but we then add in novel content for this specific file (specifically the for loop which outputs some of our general blog text)

- the content being added is marked in between the `{%block content %}` and `{% endblock%}`

#### login.html: 

- we inherit the base.html file to start things out

- utilizing the `form` for a location for our form element. 

- security: The form.hidden_tag() template argument generates a hidden field that includes a token that is used to protect the form against CSRF attacks. All you need to do to have the form protected is include this hidden field and have the SECRET_KEY variable defined in the Flask configuration. If you take care of these two things, Flask-WTF does the rest for you.

- we also add a for loop after username & password; these are going to render the specific error messages in red. " As a general rule, any fields that have validators attached will have error messages added under `form.<field_name>.errors`"

#### base_flash.html: 

- the `with` constructor is going to assign results of the `get_flashed_messages()` function (from Flask); in our case we should be getting flashed messages warning that userna,es need to be included.

- the `if messages` is our logic check - if a message exists, then we will print it out with the `<ul>` (unordered list tag) and each item will be separated using `<li>`

- `get_flashed_messages()`: any message in these disappears after requested once (kind of like the output of a zip in Python)

- `url_for()` allows for dyanmic updates to links.All I have to add is the endpoint name (name of the view function in the `routes.py` file)


### flask extensions: 

#### flask-wtf: 

This is a thin wrapper around the WTForms package that integrates well with flask. This allows your form field HTML to be generated for you, but also provides for some basic customization. 


### forms.py: 

The Flask-WTF extension uses Python classes to represent web forms. 

The first class is `LoginForm` which is going to inherit from FlaskForm. We also need to import specific data types from the wtforms (general package installed when we added the flask-wtf extension). 


### Databases in Flask

Miguel mentions these are not natively supported, so we can use whatever we want (to an extent) 

### Connecting with Heroku: 

Okay, this was a bit of a pain for me. There are some very helpful resources, but here are the steps I took: 

- Make sure you are working in a git repo; also need to have the heroku CLI working (info here: )

- create heroku app: `heroku create djw-microblog`

- then need to add a git remote: `git:remote -a djw-microblog`

- should see info on heroku when you run `git remote -v`

### config.py

I still don't fully follow what is going on here, but the `SECRET_KEY` is important in order tolimit who can access web forms. 


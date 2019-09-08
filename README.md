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

- This is also where we pull in our config information

- Our `db` object is also read in here, as is the `migrate` object. 

- models is where we wiill be pulling in database structures

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

#### SQLAlchemy

The tutorial proposes using the SQLAlchemy which will allow us to use SQLite, which does not require a server for early work (and for my purposes will be more than sufficient)

SQLAlchemy can also work with PostgresSQL and MySQL, maybe better for production. 

#### Database Migrations: 

Flask-migrate (created by the author of these tutorials - cool!) allows a database to get shifted in the future without much headache. 

- We were able to establish automatic migrations with `flask db migrate -m "users table"`

- In order to accept an update to our DB change we use `flask db upgrade`, and to roll back a change we can use `flask db downgrade` 

    - Cool note from author: "Because this application uses SQLite, the upgrade command will detect that a database does not exist and will create it (you will notice a file named app.db is added after this command finishes, that is the SQLite database)"

#### app/models.py: 

- this is where we build the various database classes 

- why don't we store passwords here? 
    - "The problem with storing passwords is that if the database ever becomes compromised, the attackers will have access to the passwords, and that could be devastating for users."

##### user class: 

- The user class inherits from `db.Model`
- We define a few different fields, specifically as instances of `db.Column` class.
- The `__repr__` method tells Python how to print objects of this class, which is going to be useful for debugging
- There is a spot for the `password_hash` as well as a location to connect to the post database
- `posts`: 
    - "This is not an actual database field, but a high-level view of the relationship between users and posts, and for that reason it isn't in the database diagram. For a one-to-many relationship, a db.relationship field is normally defined on the "one" side, and is used as a convenient way to get access to the "many". So for example, if I have a user stored in u, the expression u.posts will run a database query that returns all the posts written by that user."
    - "The first argument to db.relationship is the model class that represents the "many" side of the relationship. This argument can be provided as a string with the class name if the model is defined later in the module. The backref argument defines the name of a field that will be added to the objects of the "many" class that points back at the "one" object. This will add a post.author expression that will return the user given a post. The lazy argument defines how the database query for the relationship will be issued"

##### post class: 

- `timestamp` is going to be automatically set
- `id` is just a primary key for the table
- `body` should be input by the user 
- `user_id` is a foreign key, allowing us to link back to the `id` in the users table. 


### Connecting with Heroku: This one took me awhile

Okay, this was a bit of a pain for me because I am using Ubuntu 16.04 through WSL (Info: https://docs.microsoft.com/en-us/windows/wsl/install-manual). There are some very helpful resources, but here are the steps I took: 

- Make sure you are working in a git repo for your flask app; also need to have the heroku CLI working (info here: https://devcenter.heroku.com/articles/heroku-cli)

- your flask app (the .py) needs to be in the root of your directory (otherise Heroku can't find your build type). I think you can also just provide a `.txt` file with versioning info as well (`runtime.txt`). Much better info on general set-up is here: https://github.com/heroku/python-getting-started

- create heroku app: `heroku create djw-microblog`

- then need to add a git remote: `heroku git:remote -a djw-microblog`

- should see info on heroku when you run `git remote -v`

- Push updates to heroku: `git push heroku master`

- A few other things we need: 
    - Add a `Procfile` -  this is going to tell Heroku how to execute the application. For this simple application we just provide info on web stuff, run db update, flask translate, then start the server (gunicorn microblog:app)

    - THe folllowing needs to happen for the flask command to work: `heroku config:set FLASK_APP=microblog.py`

- Anytime we make an update and want to redeploy we just run `git push heroku master`

- Where can I view the site? https://djw-microblog.herokuapp.com/

### config.py

I still don't fully follow what is going on here, but the `SECRET_KEY` is important in order tolimit who can access web forms. 

We also add some database info: 
- "The Flask-SQLAlchemy extension takes the location of the application's database from the SQLALCHEMY_DATABASE_URI configuration variable"
    - We take the database by looking for a specific DB URL, but if that fails then we just build one with the basedir command. (`basedir.py` shows an example of checking where this will place the db, short answer is it just gets added to root)
- "The SQLALCHEMY_TRACK_MODIFICATIONS configuration option is set to False to disable a feature of Flask-SQLAlchemy that I do not need, which is to signal the application every time a change is about to be made in the database."



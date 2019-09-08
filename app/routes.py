from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/index')
def index():
    user = {'username': 'David'}
    return render_template('index.html', title='Home', user=user)

@app.route('/index_for')
def index_for():
    user = {'username': 'David'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index_for_loop.html', title='Home', user=user, posts=posts)

@app.route('/')
@app.route('/index_inherit')
def index_inherit():
    user = {'username': 'David'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index_inherit.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index_inherit'))
    return render_template('login.html', title='Sign In', form=form)
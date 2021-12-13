#Enables the registration and login pages to work
import functools

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from .db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
#Registration
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method =='POST':
        #Gets the username, password, charity and email from register.html
        username = request.form['username']
        password = request.form['password']
        charity = request.form['charity']
        email = request.form['email']

        db = get_db()
        error = None

        #Verification that a username and password is entered
        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'

        if error is None:
            try:
                #Using SQL inserts the information into the table user
                db.execute(
                    "INSERT INTO user (username, password, charity, email) VALUES (?,?,?,?)",
                    (username, generate_password_hash(password), charity, email),
                )
                db.commit()
            #Verifies the user hasn't already registered
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                #Creates a new table called whatever the user has entered as their username.
                db.execute("CREATE TABLE IF NOT EXISTS " + username + "(id INTEGER PRIMARY KEY autoincrement)")
                return redirect(url_for("auth.login"))

        flash(error)
    return render_template('auth/register.html')

#login
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method =='POST':
        #retrieves the username and password entered by the user
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        #Selects all user information for the record where the username field matches what the user entered
        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        #Checks entered unsername exists in the database
        if user is None:
            error = 'Incorrect username.'
        #Checks the entered password with that of the one entered
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect Password.'

        #if there is no error then sets up the session variables to be used in other python files
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            session['username'] = username
            return redirect(url_for("home.home"))

        flash (error)
    return render_template('auth/login.html')

#logout - clears session
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash
from .db import get_db

bp = Blueprint('database_queries', __name__, url_prefix='/database_queries')

@bp.route('/add_data', methods=('GET', 'POST'))
def add_data():
    if request.method=='POST':
        newcolumn = request.form['newcolumn']
        datatype = request.form['datatype']

        db = get_db()
        error = None

        if newcolumn != '' :
            db.execute("ALTER TABLE " + session['username'] + " ADD " + newcolumn +" "+ datatype + ";")
            db.commit()
    return render_template('/database_queries/add_data.html')

@bp.route('/get_data')
def get_data():
    return render_template('/database_queries/get_data.html')

@bp.route('/change_info', methods=('GET', 'POST'))
def change_info():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        charity = request.form['charity']
        email = request.form['email']

        db = get_db()
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'

        if error is None:
            try:
                db.execute(
                    "UPDATE user SET password = ?, charity = ?, email = ? WHERE username = ?;",
                    (generate_password_hash(password), charity, email, username),
                )
                db.commit()
            except db.IntegrityError:
                error = "error in changing info"
            else:
                return redirect(url_for("home.home"))


        flash(error)
    return render_template('/database_queries/change_info.html')
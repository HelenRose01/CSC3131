#Python file ehich allows the user to add and get data from the database

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash
from .db import get_db

bp = Blueprint('database_queries', __name__, url_prefix='/database_queries')

#add to database
@bp.route('/add_data', methods=('GET', 'POST'))
def add_data():
    cols=[]
    db = get_db()
    #retrieves columns from database where the table equals their username
    columns = db.execute("PRAGMA table_info( " +
                              session['username'] + ");").fetchall()
    if request.method=='POST':
        #Gets name of column and datatype from the HTML file
        newcolumn = request.form['newcolumn']
        datatype = request.form['datatype']

        #gets the the data entered in the HTML file to be added to the table
        record = []
        r = 0
        for i in columns:
             record.append(request.form[i[1]])
             r=r+1

        if newcolumn != '' and datatype != '':

            if newcolumn != '' :
                #Adds the column to the database
                db.execute("ALTER TABLE " + session['username'] + " ADD " + newcolumn +" "+ datatype + ";")
                db.commit()
                db.close()
        else:
            #If no new column entered then all the data entered by the user to be entered into the database if inserted
            for j in columns:
                cols.append(j[1])
            db.execute("INSERT INTO " + session['username'] + "(" + cols[1] + ", "+cols[2]+ "," + cols[3]+ ","+ cols[4]+
                       ") VALUES (?,?,?,?)", (record[1], record[2], record[3], record[4]))
            db.commit()
            db.close()
    return render_template('/database_queries/add_data.html', columns=columns)

@bp.route('/get_data')
def get_data():
    #Gets all data from database where the table name is the user's username
    db = get_db()
    table = db.execute("SELECT * FROM " + session['username']+";").fetchall()
    return render_template('/database_queries/get_data.html', table=table)

@bp.route('/change_info', methods=('GET', 'POST'))
def change_info():
    if request.method =='POST':
        #gets the username, password, charity and email from the HTML file
        username = request.form['username']
        password = request.form['password']
        charity = request.form['charity']
        email = request.form['email']

        db = get_db()
        error = None

        #makes sure a username and password was entered by the user
        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'

        if error is None:
            try:
                #updates where the username = the user's username, the new information
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
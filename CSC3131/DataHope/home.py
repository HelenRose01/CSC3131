#Home page - renders the home.html file
from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('home', __name__)

@bp.route('/home')
def home():
    return render_template('/home.html')
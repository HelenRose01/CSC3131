from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('database_queries', __name__, url_prefix='/database_queries')

@bp.route('/add_data')
def add_data():
    return render_template('/database_queries/add_data.html')

@bp.route('/get_data')
def get_data():
    return render_template('/database_queries/get_data.html')

@bp.route('/change_info')
def change_info():
    return render_template('/database_queries/change_info.html')
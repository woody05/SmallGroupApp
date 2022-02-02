"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from small_group_app import app, db
from ..models.users import User
from ..models import users
from sqlalchemy.sql import text

@app.route('/directory')
@login_required
def directory_view_all():
    users = User.query.filter(User.is_active).all()

    return render_template(
        'directory.html',
        title='Directory',
        year=datetime.now().year,
        users = users
    ) 

@app.route('/directory_info')
@login_required
def directory_info():
    if request.method == 'GET':
        results = db.session.query(User.first_name,User.last_name,User.phone_number,User.email_address).all()

        response = {"data":None}

        user_schema = users.user_schema( many=True)
        foo  = user_schema.jsonify(results)
        response["data"] = foo.json
        return response
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

@app.route('/user_settings')
@login_required
def user_settings():
    user = current_user

    return render_template(
        'user_settings.html',
        title='Settings',
        year=datetime.now().year,
        user = user
    ) 
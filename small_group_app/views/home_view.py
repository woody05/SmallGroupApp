"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from small_group_app import app, db
from small_group_app import dashboards
from small_group_app.dashboards import HomeDashboard
from ..models import prayer_request, category, comment
from ..models.users import User
from sqlalchemy.sql import text

@app.route('/')
@app.route('/home',methods = ['POST', 'GET'])
@login_required
def home():

    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/unanswered_prayers',methods = ['POST', 'GET'])
@login_required
def unanswered_prayers():

    if request.method == "GET":
        h = HomeDashboard()
        return h._get_unanswered_prayers()
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, url_for, request, jsonify,session
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from small_group_app import app, db
from .models import prayer_request, category, comment
from .models.users import User
from sqlalchemy.sql import text


@app.login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return redirect(url_for('login'))

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        form = request.form

        username = form.get('username')
        password = form.get('password')

        user = User.query.filter_by(user_name=username).first()
        if user is None or not user.check_password(password):
            return redirect(url_for('login'))

        # TODO set this to pull from Database
        session['small_group_name'] = "Pastor Bob's ABF"

        login_user(user, remember=True)
        return redirect(url_for('home'))
    else:
        return render_template(
            'login.html',
            title='Small Group',
            header='Login',
            year=datetime.now().year,
        )

# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/create_account',methods = ['POST', 'GET'])
def create_account():
    password_match = None

    if request.method == 'POST':

        if request.form['password1'] != request.form['password2']:
            password_match = 'Passwords do not match'

            return jsonify({"error":"Passwords do not match"}), 400

        newUser = User()
        newUser.email_address = request.form.get('email')
        newUser.user_name = request.form.get('user_name')
        newUser.first_name = request.form.get('first_name')
        newUser.last_name = request.form.get('last_name')
        newUser.set_password(request.form.get('password1'))
        newUser.is_active = 0
        newUser.age = request.form.get('age')
        newUser.gender = request.form.get('gender')
        newUser.recieve_email = request.form.get('recieve_email')
        newUser.phone_number = request.form.get('phone_number')

        if not User.query.filter_by(email_address=newUser.email_address).first():
            db.session.add(newUser)
            db.session.commit()

        return redirect(url_for('home'))
    else:
        return render_template(
            'createAccount.html',
            title='Create Account',
            header='Create Account',
            year=datetime.now().year,
            password_match=password_match
        )

@app.route('/dashboard')
def dashboard():
    return render_template(
        'dashboard.html',
        title='Dash Board',
        year=datetime.now().year,
    )



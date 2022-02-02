"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from small_group_app import app, db
from ..models import prayer_request, category, comment
from ..models.users import User
from sqlalchemy.sql import text

@app.route('/prayer_request',methods = ['POST', 'GET'])
@login_required
def prayer_request_all_view():
    _prayer_request = prayer_request.all_prayer_request()
    categories = category.all_categories().all()

    if request.method == "POST":
        search = request.form['search']
        searchDesc = request.form['searchDesc']
        category_id = request.form['category']
        
        if  request.form['status'] == "1":
            _prayer_request = prayer_request.all_prayer_request().filter(prayer_request.prayer_request.title.contains(search)).filter(prayer_request.prayer_request.description.contains(searchDesc)).filter(prayer_request.prayer_request.category_id.contains(category_id))
        elif request.form['status'] == "2":
            _prayer_request = prayer_request.answered_prayer_request().filter(prayer_request.prayer_request.title.contains(search)).filter(prayer_request.prayer_request.description.contains(searchDesc)).filter(prayer_request.prayer_request.category_id.contains(category_id))
        elif request.form['status'] == "3":
            _prayer_request = prayer_request.unanswered_prayer_request().filter(prayer_request.prayer_request.title.contains(search)).filter(prayer_request.prayer_request.description.contains(searchDesc)).filter(prayer_request.prayer_request.category_id.contains(category_id))

    _prayer_request = _prayer_request.order_by(prayer_request.prayer_request.date_added.desc())

    return render_template(
        'prayer_request_all.html',
        title='Prayer Request',
        header='Prayer Request',
        year=datetime.now().year,
        prayer_requests = _prayer_request,
        categories = categories,
    )

@app.route('/addPrayerRequest',methods = ['POST', 'GET'])
@login_required
def addPrayerRequest():
    if request.method == 'POST':
        newRequest = prayer_request.prayer_request()

        newRequest.title = request.form['title']
        newRequest.description = request.form['description']
        newRequest.is_answered = 0
        newRequest.added_by = current_user.user_name
        newRequest.category_id = request.form['category_id']
        newRequest.date_added = datetime.now()
        newRequest.date_answered = None

        newRequest._added_by_user = current_user

        db.session.add(newRequest)
        db.session.commit()
        
        return redirect(url_for('prayer_request_all_view'))
    else:
        categories = category.all_categories().all()
        return render_template(
            'addPrayerRequest.html',
            title='Add New Prayer Request',
            year=datetime.now().year,
            categories = categories
        )  


@app.route('/verifyDeletePrayerRequest/<id>')
@login_required
def verifyDeletePrayerRequest(id):
      if request.method == "GET":
        p_request = prayer_request.prayer_request_by_id(id).first()
        return render_template(
            'deletePrayerRequest.html',
            title='Are you sure you want to delete ',
            year=datetime.now().year,
            url=url_for('removePrayerRequest'),
            p_request = p_request
        ) 


@app.route('/editPrayerRequest/<id>',methods = ['POST', 'GET'])
@login_required
def editPrayerRequest(id):
    if request.method == "GET":
      p_request = prayer_request.prayer_request_by_id(id).first_or_404()
      categories = category.all_categories().all()
      users = User.query.filter(User.is_active).all()

      return render_template(
            'editPrayerRequest.html',
            title='Edit',
            year=datetime.now().year,
            p_request = p_request,
            categories = categories,
            users=users
        )
    else:
        return redirect(url_for('prayer_request_all_view'))

@app.route('/updatePrayerRequest',methods = ['POST', 'GET'])
@login_required
def updatePrayerRequest():
      if request.method == "POST":
          form = request.form
          result = prayer_request.prayer_request.query.filter_by(prayer_request_id=form.get('id')).first_or_404()
          user = User.query.filter_by(id=form.get('addedby')).first_or_404()

          result.title = request.form['title']
          result.description = request.form['description']
          result.added_by = request.form['addedby']
          result.date_added = request.form['dateadded']
          result.is_answered = request.form['status']
          result.date_answered = request.form['dateAnswered'] if form.get('dateAnswered') else None
          result.category_id = request.form['category_id']

          result._added_by_user = user

          db.session.commit()

          return redirect(url_for('prayer_request_all_view'))
      else:
          return redirect(url_for('prayer_request_all_view'))


@app.route('/removePrayerRequest',methods = ['POST', 'GET'])
@login_required
def removePrayerRequest():
    if request.method == 'POST':
        id = request.form['id']
        #KAW - removing comments for prayer request first. 
        #      foreign key contraint
        comment.remove_comments(id)
        prayer_request.remove_prayer_request(id)
        return redirect(url_for('prayer_request_all_view'))
    else:
        return redirect(url_for('prayer_request_all_view'))

@app.route('/unansweredPrayerRequest')
@login_required
def unansweredPrayerRequest():
    result = prayer_request.unanswered_prayer_request()
    return render_template(
        'unansweredPrayerRequest.html',
        title='Unanswered Prayers',
        header='Unanswered Prayers',
        year=datetime.now().year,
        prayer_requests = result,
    )

@app.route('/addPrayerRequestComment',methods = ['POST', 'GET'])
@login_required
def addPrayerRequestComment():
    if request.method == 'POST':
        newComment = comment.comments()
        newComment.date_added = datetime.now()
        newComment._comment = request.form['comment']
        newComment.user_id = 1
        newComment.prayer_request_id = request.form['prayer_request_id']

        comment.add_comment(newComment)

        return redirect(url_for('prayer_request_all_view'))

@app.route('/api/unansweredPrayerRequest',methods = ['POST', 'GET'])
@login_required
def apiUnansweredPrayerRequest():
    response = {"data":None}
    result = prayer_request.unanswered_prayer_request().all()
    prayer_request_schema = prayer_request.prayer_request_schema( many=True)
    foo  = prayer_request_schema.jsonify(result)
    response["data"] = foo.json
    return response

@app.route('/api/recentlyAddedPrayerRequest',methods = ['POST', 'GET'])
@login_required
def apiRecentlyAddedPrayerRequest():
    result = prayer_request.recently_added_prayer_request()
    prayer_request_schema = prayer_request.prayer_request_schema(many=True)
    return prayer_request_schema.dumps(result)

@app.route('/api/answeredThisWeek',methods = ['POST', 'GET'])
@login_required
def answeredThisWeek():
    result = prayer_request.answered_this_week().all()
    prayer_request_schema = prayer_request.prayer_request_schema(many=True)
    return prayer_request_schema.dumps(result)


@app.route('/api/categories',methods = ['POST', 'GET'])
@login_required
def apiCategories():
    result = category.all_categories().all()
    category_schema = category.category_schema(many=True)
    return category_schema.dumps(result)

@app.route('/api/allPrayerRequest',methods = ['POST', 'GET'])
@login_required
def apiAllPrayerRequest():
    response = {"data":None}
    result = prayer_request.all_prayer_request().all()
    prayer_request_schema = prayer_request.prayer_request_schema( many=True)
    foo  = prayer_request_schema.jsonify(result)
    response["data"] = foo.json
    return response

@app.route('/api/PrayerRequestDetails/',methods = ['POST', 'GET'])
@login_required
def apiPrayerRequestDetails():
    if request.method == 'GET':
        response = {"data":None}
        result = prayer_request.prayer_request_by_id(request.values.get('id')).all()
        prayer_request_schema = prayer_request.prayer_request_schema( many=True)
        foo  = prayer_request_schema.jsonify(result)
        response["data"] = foo.json
        return response
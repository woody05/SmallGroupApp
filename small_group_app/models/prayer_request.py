from small_group_app import app, db, ma
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey ,and_, func
from . import comment, category
from marshmallow import fields
from datetime import datetime, timedelta
#from datatables import ColumnDT, DataTables
from dateutil.relativedelta import relativedelta

Base = declarative_base()

class prayer_request(db.Model):
    prayer_request_id = db.Column('Prayer_Request_id', db.Integer, primary_key = True)
    title = db.Column("Title", db.Text, nullable=False)
    description = db.Column("Description",db.VARCHAR, nullable=False)
    is_answered = db.Column("IsAnswered", db.Integer, nullable=False)
    #added_by = db.Column("Add_By",db.Text, nullable=False)
    date_added = db.Column("Date_Added",db.Date, nullable=False)
    date_answered = db.Column("Date_Answered",db.Date, nullable=False)
    
    category_id = db.Column("Category_id", db.Integer, ForeignKey("category.Category_id"))
    _category = relationship("category")

    added_by_user_id = db.Column("added_by_user_id", db.Integer, ForeignKey("users.id"))
    _added_by_user = relationship("User")

    comments = relationship("comments", back_populates="prayer_request")


class prayer_request_schema(ma.Schema):
    class Meta:
        model = prayer_request
        #load_instance = True

    prayer_request_id =  fields.Int()
    title =  fields.String()
    description =  fields.String()
    is_answered =  fields.Int()
    added_by =  fields.String()
    date_added =  fields.DateTime()
    date_answered =  fields.DateTime()
    _category = fields.Nested(category.category_schema)


def all_prayer_request():
    result = prayer_request.query
    return result

def unanswered_prayer_request():
    data = prayer_request.query.filter_by(is_answered=0).order_by(prayer_request.date_added.asc())
    return data

def recently_added_prayer_request():
    unanswered = unanswered_prayer_request()
    
    now = datetime.now().date()
    one_month_back = now - relativedelta(months=1)

    data = unanswered.filter(db.func.date(prayer_request.date_added) >= one_month_back)

    return data

def answered_prayer_request():
    data = prayer_request.query.filter_by(is_answered=1)
    return data

def answered_this_week():
    now = datetime.now().date()
    startDate = now - timedelta(days=now.weekday())
    endDate = startDate + timedelta(days=6)
    data = prayer_request.query.filter(
                    db.func.date(prayer_request.date_answered)<=endDate, 
                    db.func.date(prayer_request.date_answered)>=startDate)
    return data


def prayer_request_by_id(id):
    result = prayer_request.query.filter_by(prayer_request_id=id)
    return result


def remove_prayer_request(id):
    result = prayer_request.query.filter_by(prayer_request_id=id).first()
    db.session.delete(result)
    db.session.commit()


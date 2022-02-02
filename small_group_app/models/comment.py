
from small_group_app import db, ma
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from marshmallow import fields

Base = declarative_base()

class comments(db.Model):
    comment_id = db.Column('Comment_id', db.Integer, primary_key = True)
    _comment = db.Column("Comment", db.Text)
    date_added = db.Column("Date_added", db.DateTime)

    #user_id = db.Column("User_id", db.Integer, ForeignKey("users.User_id"))
    #users = relationship("users")

    prayer_request_id = db.Column("Prayer_request_id", db.Integer, ForeignKey("prayer_request.Prayer_Request_id"))
    prayer_request = relationship("prayer_request", back_populates="comments")

class comments_schema(ma.Schema):
    class Meta:
        model = comments
        load_instance = True

    comment_id = fields.Int()
    _comment = fields.String()
    date_added = fields.DateTime()
    prayer_request_id = fields.Int()


def comments_for_request(id):
    result = comments.query.order_by(comment.date_added.desc())
    return result


def add_comment(newComment):
   commentToAdd = newComment

   db.session.add(commentToAdd)
   db.session.commit()

def remove_comments(id):
    result = comments.query.filter_by(prayer_request_id=id).all()
    for comment in result:
        db.session.delete(comment)
    db.session.commit()
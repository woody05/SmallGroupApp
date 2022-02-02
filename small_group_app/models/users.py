
from marshmallow import fields
from enum import Enum
from small_group_app import db, ma
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from small_group_app.models.prayer_request import prayer_request, prayer_request_schema

Base = declarative_base()

class UserRole(Enum):
    SUPER_ADMIN = 0
    ADMIN = 1
    LEADER = 2
    BASIC = 3

class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column('id', db.Integer, primary_key = True)
    user_name = db.Column("User_name", db.Text)
    email_address = db.Column("Email_address", db.Text)
    first_name = db.Column("First_name", db.Text)
    last_name = db.Column("Last_Name", db.Text)
    password = db.Column("password", db.String(200))
    salt = db.Column("salt", db.String(50))
    is_active = db.Column('is_active',db.Boolean)
    phone_number = db.Column('phone_number',db.String(20))
    profile_picture = db.Column('profile_picture',db.String(100))
    age = db.Column('age',db.Integer)
    gender = db.Column('gender',db.Enum(Gender))
    recieve_email = db.Column('gender',db.Boolean)

    prayer_requests = relationship('prayer_request', back_populates="_added_by_user")
    #comments = relationship("comments", back_populates="users")

    def __repr__(self):
        return 'User.query.get({})'.format(self.id)

    def set_password(self, password):
       """Create hashed password."""
       self.password = generate_password_hash(
           password,
           method='sha256'
       )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def get_users_prayer_request(self):
        return prayer_request.query.filter_by(added_by_user_id=self.id)

class user_schema(ma.Schema):
        class Meta:
            model = prayer_request
            #load_instance = True

        id =  fields.Int()
        user_name =  fields.String()
        email_address =  fields.String()
        first_name =  fields.String()
        last_name =  fields.String()
        phone_number =  fields.String()
        profile_picture = fields.String()

        _prayer_request = fields.Nested(prayer_request_schema)
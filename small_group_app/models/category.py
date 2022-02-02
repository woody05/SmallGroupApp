from small_group_app import db, ma
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from marshmallow import fields

Base = declarative_base()

class category(db.Model):
    category_id = db.Column('Category_id', db.Integer, primary_key = True)
    title = db.Column("Title", db.String(50))


class category_schema(ma.Schema):
    class Meta:
        model = category
        load_instance = True
    category_id = fields.String()
    title = fields.String()


def all_categories():
    result = category.query.order_by(category.title.asc())
    return result
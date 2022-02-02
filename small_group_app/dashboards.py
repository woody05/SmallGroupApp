import imp
from small_group_app import app, db
from datetime import datetime
from .models.users import User
from .models import users, prayer_request
from sqlalchemy.sql import text

class DashboardBase():
    def __init__(self):
        self._active_users = User.query.all()

class HomeDashboard(DashboardBase):
    def __init__(self):
        super().__init__()

    def _get_unanswered_prayers(sefl):
        results = prayer_request.prayer_request.query.filter_by(is_answered=0).limit(5).all()

        response = {"data":None}

        prayer_request_schema = prayer_request.prayer_request_schema(many=True) 
        json_results  = prayer_request_schema.jsonify(results)
        response["data"] = json_results.json

        return response
    

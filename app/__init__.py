from datetime import timedelta
from flask import Flask

app = Flask(__name__)
app.secret_key = "RTR10Rtnttrrwrttri76#"
app.config["SECRET_KEY"] = "RTR10Rtnttrrwrttri76#"
app.permanent_session_lifetime = timedelta(days = 2)

from app import views
from app import api

print("App __init__")

import log
from flask import Flask, flash, render_template, request, url_for, redirect, send_from_directory
from flask_socketio import SocketIO, emit
from ledbox import LedBox
from viewmodel import ViewModel
from datetime import timedelta
#from static.static_routes import static_routes
import logging
import config
import threading
import time
import json

app = None
ledbox = None
socketio = None

#logging.config.fileConfig('logging.ini', disable_existing_loggers = False)
logger = logging.getLogger(__name__)
logger.info("Starting server")

logger.info("Initializing Flask")
app = Flask(__name__)
app.secret_key = "RTR10Rtnttrrwrttri76#"
app.config["SECRET_KEY"] = "RTR10Rtnttrrwrttri76#"
app.permanent_session_lifetime = timedelta(days = 2)
#app.register_blueprint(static_routes, url_prefix = "/static")

logger.info("Initializing SocketIO")
socketio = SocketIO(app)

@socketio.on("connect")
def connected():
    emit("Connected", {"data": "LED Box"})
    logger.info("SocketIO Client connected")
    ledbox.emit_ledbox_state()

def message_received(methods = ["GET", "POST"]):
    print("message was received!!!")

@socketio.on("SpecialEvent")
def handle_special_event(json_data, methods = ["GET", "POST"]):
    # print("Received Menu event: " + str(json_data))
    if json_data["data"] == "off":
        ledbox.off()
    elif json_data["data"] == "shutdown":
        ledbox.stop()
    elif json_data["data"] == "random":
        ledbox.random()
    else:
        abort(404, "Unsuppored data")
    # socketio.emit("Response", json_data, callback = message_received)

@socketio.on("ArrowEvent")
def handle_arrow_event(json_data, methods = ["GET", "POST"]):
    # print("Received Arrow event: " + str(json_data))
    ledbox.arrow_pressed(json_data["data"])
    # socketio.emit("Response", json_data, callback = message_received)

@socketio.on("ActionEvent")
def handle_action_event(json_data, methods = ["GET", "POST"]):
    # print("Received Action event: " + str(json_data))
    ledbox.start_plugin(json_data["data"])
    # socketio.emit("Response", json_data, callback = message_received)

@app.route("/about")
def about():
    model = { "intro": "This is about ...." }
    return render_template("about.html", model = model)

@app.route("/")
def index():
    logger.info("GET /")
    model = ViewModel()

    for p in ledbox.get_plugins():
        if p.options["show_button"] == False:
            continue
        model.plugins.append((p.name, p.options["display_name"], p.options["button_text"], p.options["button_type"]))

    model.current_action = "(not connected)"

    return render_template("index.html", model = model)

#@app.route("/logout")
#def logout():
#    session.pop("user", None)
#    return redirect(url_for("login"))
#@app.route("/")
#def index():
#    if "user" in session:
#        pass
#    else:
#        redirect(url_for("login")) 
# @app.route("/login", methods = ["POST", "GET"])
# def login():
#     model = LoginModel()
#
#     if request.method == "POST":
#         model.username = request.form["username"]
#         model.password = request.form["password"]
#         if model.username == "admin" and model.password == "admin":
#             session.permanent = True
#             session["user"] = model.username
#             return redirect(url_for("index"))
#         else:
#             return render_template("login.html", model = model)
#     else:
#         return render_template("login.html", model = model)


#@app.route("/api/ledbox")
#def api_ledbox():
    # books = []
    # return render_template("books.json", model = books), 201, {"Content-Type" : "application/json"}
    # return "LDJQLKDJQSLD"

def ledbox_event(data):
    # print(data)
    socketio.emit("LedBox", data, callback = message_received)

def main():
    global ledbox
    global app
    global socketio

    try:
        logger.info("Starting LedBox")
        ledbox = LedBox(ledbox_event)
        x = threading.Thread(target = ledbox.loop_plugin)
        logger.info("Starting main loop")
        x.start()
        logger.info("Starting SocketIO")
        logger.info(f"Listening on port {config.PORT}")
        socketio.run(app, config.HOST, config.PORT, debug = config.DEBUG, use_reloader = False)
    except Exception as e:
        raise
    else:
        pass
    finally:
        logger.info("Stopping")
        ledbox.stop()
        time.sleep(2)

if __name__ == "__main__":
    main()

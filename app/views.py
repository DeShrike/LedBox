from app import app
from flask import render_template, send_from_directory
from ledbox import LedBox
import logging
from .viewmodel import ViewModel

logger = logging.getLogger(__name__)

@app.route("/favicon.ico")
def send_favicon():
    return send_from_directory("img", "favicon.ico")

@app.route("/about")
def about():
    model = ViewModel()
    model.title = "About"
    model.intro = "The is the 'about' text"

    return render_template("about.html", model = model)

@app.route("/")
def index():
    logger.info("GET /")
    model = ViewModel()
    ledbox = LedBox.current()

    for p in ledbox.get_plugins():
        if p.options["show_button"] == False:
            continue
        model.plugins.append((p.name, p.options["display_name"], p.options["button_text"], p.options["button_type"]))

    model.current_action = "(not connected)"

    return render_template("index.html", model = model)

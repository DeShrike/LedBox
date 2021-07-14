from flask import Blueprint, send_from_directory, render_template
from viewmodel import ViewModel
import logging

handlers = Blueprint("handlers", __name__)
logger = logging.getLogger(__name__)

@handlers.route("/favicon.ico")
def send_favicon():
    return send_from_directory("img", "favicon.ico")

@handlers.route("/about")
def about():
    model = ViewModel()
    model.title = "About"
    model.intro = "The is the 'about' text"
    return render_template("about.html", model = model)

@handlers.route("/")
def index():
    logger.info("GET /")
    model = ViewModel()

    for p in ledbox.get_plugins():
        if p.options["show_button"] == False:
            continue
        model.plugins.append((p.name, p.options["display_name"], p.options["button_text"], p.options["button_type"]))

    model.current_action = "(not connected)"

    return render_template("index.html", model = model)

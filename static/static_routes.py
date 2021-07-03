from flask import Blueprint, send_from_directory

static_routes = Blueprint("static_routes", __name__)

@static_routes.route("/js/<path:path>")
def send_js(path):
    return send_from_directory("js", path)

@static_routes.route("/css/<path:path>")
def send_css(path):
    return send_from_directory("css", path)

@static_routes.route("/img/<path:path>")
def send_img(path):
    return send_from_directory("img", path)

@static_routes.route("/favicon.ico")
def send_favicon():
    return send_from_directory("img", "favicon.ico")

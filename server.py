import log
from flask_socketio import SocketIO, emit
from ledbox import LedBox
import logging
import config
import threading
import time
import json

ledbox = None

logger = logging.getLogger(__name__)
logger.info("Starting server")
logger.info("Initializing Flask")

from app import app

logger.info("Initializing SocketIO")
socketio = SocketIO(app)

@socketio.on_error()
def error_handler(e):
    print("SocketIO error")
    pass

@socketio.on("connect")
def connected():
    emit("Connected", {"data": "LED Box"})
    logger.info("SocketIO Client connected")
    ledbox.emit_ledbox_state()

@socketio.on("disconnect")
def disconnected():
    #emit("Connected", {"data": "LED Box"})
    logger.info("SocketIO Client disconnected")
    #ledbox.emit_ledbox_state()

def message_received(methods = ["GET", "POST"]):
    print("message was received!!!")
    # send("x", broadcast = True)

@socketio.on("SpecialEvent")
def handle_special_event(json_data, methods = ["GET", "POST"]):
    logger.info("Received Special Event: " + str(json_data))
    ledbox.stop_random()
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
    logger.info("Received Arrow Event: " + str(json_data))
    ledbox.arrow_pressed(json_data["data"])
    # socketio.emit("Response", json_data, callback = message_received)

@socketio.on("ActionEvent")
def handle_action_event(json_data, methods = ["GET", "POST"]):
    logger.info("Received Action Event: " + str(json_data))
    ledbox.stop_random()
    ledbox.start_plugin(json_data["data"])
    # socketio.emit("Response", json_data, callback = message_received)

def ledbox_event(data):
    # print(data)
    socketio.emit("LedBox", data, callback = message_received)

def main():
    global ledbox

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
        print(e)
        raise
    else:
        pass
    finally:
        logger.info("Stopping")
        ledbox.stop()
        time.sleep(2)

if __name__ == "__main__":
    main()

from flask_socketio import Namespace, emit

class Sio(Namespace):

    def __init__(self):
        pass

    def on_connet(self):
        pass

    def on_disconnect(self):
        pass

    def on_my_event(self, data):
        emil("my_response", data)

socketio.on_namespace(Sio("/test"))



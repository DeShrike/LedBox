from grid import Grid
import plugins
import time

class LedBox():
    width = 15
    height = 10

    def __init__(self, callback):
        self.grid = Grid(self.width, self.height)
        self.callback = callback
        self.cancel = False
        self.plugins = []
        self.active_plugin = None

        print("LedBox INIT")

        for plugin in plugins.PLUGINS:
            self.plugins.append(plugin(self, self.grid))

        self.plugins.sort(key = lambda x: x.order, reverse = False)

    def start(self):
        self.active_plugin = self.plugins[0]
        self.active_plugin.start()

    def start_plugin(self, name: str):
        self.stop_plugin()
        if self.cancel:
            return
        # print("Trying to start plugin", name)
        for p in self.plugins:
            if p.name == name:
                self.active_plugin = p
                self.active_plugin.start()
                break

        self.emit_ledbox_state()

    def stop_plugin(self):
        # print("Stopping active plugin")
        if self.active_plugin is None:
            return
        self.active_plugin.stop()
        self.active_plugin = None
        self.emit_ledbox_state()

    def emit_ledbox_state(self):
        state = {}
        state["active_plugin"] = "" if self.active_plugin is None else self.active_plugin.display_name
        state["running"] = not self.cancel
        state["need_arrows"] = False if self.active_plugin is None else self.active_plugin.need_arrows

        self.callback(state)

    def loop_plugin(self):
        self.start_plugin(self.plugins[0].name)

        while self.cancel == False  :
            if self.active_plugin is None:
                pass
            else:
                # print("Loop", self.active_plugin.display_name)
                self.active_plugin.step()

            time.sleep(2)

    def stop(self):
        print("Stopping LedBox")
        self.stop_plugin()
        self.cancel = True
        self.emit_ledbox_state()

    def off(self):
        print("Turning off Leds")
        self.stop_plugin()
        self.emit_ledbox_state()

    def arrow_pressed(self, arrow):
        if self.active_plugin is None:
            return
        self.active_plugin.arrow_pressed(arrow)

    def get_plugins(self):
        for plugin in self.plugins:
            yield plugin

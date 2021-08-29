from abc import ABCMeta, abstractstaticmethod
from grid import Grid
import logging
import config
import plugins
import time
import random

logger = logging.getLogger(__name__)

class LedBox():
    width = config.WIDTH
    height = config.HEIGHT

    __instance = None

    @staticmethod
    def current():
        return LedBox.__instance

    def __init__(self, callback):
        self.grid = Grid(self.width, self.height)
        self.callback = callback
        self.cancel = False
        self.plugins = []
        self.active_plugin = None
        self.random_loop = False

        logger.info("LedBox Initializing")

        for plugin in plugins.PLUGINS:
            self.plugins.append(plugin(self, self.grid))

        self.plugins.sort(key = lambda x: x.options["order"], reverse = False)
        LedBox.__instance = self

    def start(self):
        self.active_plugin = self.plugins[0]
        self.active_plugin.start()

    def start_plugin(self, name: str):
        self.stop_plugin()
        if self.cancel:
            return
        logger.info(f"Trying to start plugin [{name}]")
        for p in self.plugins:
            if p.name == name:
                self.active_plugin = p
                self.active_plugin.start()
                break

        self.emit_ledbox_state()

    def stop_plugin(self):
        if self.active_plugin is None:
            return
        logger.info(f"Stopping active plugin [{self.active_plugin.name}]")
        self.active_plugin.stop()
        self.active_plugin = None
        self.emit_ledbox_state()

    def emit_ledbox_state(self):
        state = {}
        state["active_plugin"] = "" if self.active_plugin is None else self.active_plugin.options["display_name"]
        state["running"] = not self.cancel
        state["random_loop"] = self.random_loop
        state["need_arrows"] = False if self.active_plugin is None else self.active_plugin.options["need_arrows"]

        self.callback(state)

    def loop_plugin(self):
        self.start_plugin(self.plugins[0].name)

        sleeptime = None
        while self.cancel == False:
            if self.active_plugin is None:
                pass
            else:
                # print("Loop", self.active_plugin.display_name)
                sleeptime = self.active_plugin.step()

            time.sleep(1 if sleeptime == None else sleeptime)

    def stop(self):
        logger.info("Stopping LedBox")
        self.random_loop = False
        self.stop_plugin()
        self.cancel = True
        self.emit_ledbox_state()
        # Exit program ? of Shutdown Pi ?

    def off(self):
        logger.info("Turning off Leds")
        self.random_loop = False
        self.stop_plugin()
        self.emit_ledbox_state()
        self.grid.clear()
        self.grid.refresh()

    def stop_random(self):
        self.random_loop = False

    def random(self):
        logger.info("Starting Random Loop")
        self.stop_plugin()
        self.random_loop = True
        self.emit_ledbox_state()

        # select a random plugin
        while True:
            p = random.choice(self.plugins)
            if p.options["in_random"] == True:
                self.start_plugin(p.name)
                break

    def arrow_pressed(self, arrow):
        if self.active_plugin is None:
            return
        self.active_plugin.arrow_pressed(arrow)

    def get_plugins(self):
        for plugin in self.plugins:
            yield plugin

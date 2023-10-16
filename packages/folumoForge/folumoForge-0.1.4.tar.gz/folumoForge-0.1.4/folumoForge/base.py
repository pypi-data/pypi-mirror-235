import pygame

from threading import Thread
from .Forge import Screen, Forge


class modBase:
    def __init__(self, root: Forge, name, threadFunc):
        self.name = name
        if name not in root.modThreads:
            t = Thread(target=threadFunc)
            t.start()
            root.modThreads[name] = t

    def preRender(self, data):
        ...

    def postRender(self, data):
        ...

    def Fail(self, data, error):
        print(f"[ERROR-{self.name}]  : This item has failed to finish loading due to {error}; data PKG: {data}")

    def Success(self, data):
        print(f"[INFO-{self.name}]   : This item has successfully finished loading; data PKG: {data}")


class itemBase:
    mods = {}
    rect = pygame.Rect((0, 0), (0, 0))
    screen: Screen = None
    xy = (0, 0)
    wh = ()
    color = "blue"

    def delete(self):
        for item in self.screen.Items:
            if item == self:
                self.screen.Items.remove(self)

    def addMod(self, mod: modBase):
        if mod.name not in self.mods:
            self.mods[mod.name] = mod

    def update(self):
        pass

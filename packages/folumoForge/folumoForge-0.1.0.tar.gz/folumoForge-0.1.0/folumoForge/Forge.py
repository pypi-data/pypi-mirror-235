from os import environ

from pygame import Surface
from pygame.event import Event


if "PYGAME_HIDE_SUPPORT_PROMPT" in environ:
    import pygame
else:
    environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
    import pygame

del environ


class Screen:
    def __init__(self, root, name, size, title, fullScreen):
        self.title = title
        self.press = {}
        self.fullScreen = fullScreen
        self.root: Forge = root
        self.name = name
        self.size = size
        self.EventAble = []
        self.Items = []
        self.OnF = {}

    def SwitchScreen(self):
        if self.fullScreen:
            self.root.MainRoot = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        else:
            self.root.MainRoot = pygame.display.set_mode(self.size)

        pygame.display.set_caption(self.title)

        self.root.Screen = self.name

    def BindKey(self, unicodeID, func):
        self.press[unicodeID] = func

    def DeleteScreen(self):
        self.root.Screens.discard(self)

    def OnFrame(self, _id, func):
        self.OnF[_id] = func

    def render(self, event=None):
        if event:
            if event.type == pygame.QUIT:
                self.root.Running = False

            elif event.type == pygame.KEYUP:
                unicodeID = event.key
                for code in self.press:
                    if unicodeID == code:
                        self.press[code](self, event)

            for item in self.EventAble:
                item.update(event)
        else:
            for fr in self.OnF:
                self.OnF[fr]()

            for item in self.Items:
                item.update()

            for item in self.EventAble:
                item.update()


class Forge:
    def __init__(self, title, wh, icon=None, defaultScreen="start", fullScreen=False):
        pygame.init()
        pygame.font.init()

        self.Screens = {}
        self.Running = True
        self.modThreads = {}

        self.NewEventList: list[Event] = []
        self.InEvent = False

        self.delta_time = 0

        self.wh = wh
        self.MainRoot = Surface((0, 0))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(title)

        self.Screens[defaultScreen] = Screen(self, defaultScreen, wh, title, fullScreen)

        self.Screen = defaultScreen

        self.Screens[self.Screen].SwitchScreen()

        if icon:
            pygame.display.set_icon(pygame.image.load(icon))

    def GetScreen(self, name):
        return self.Screens.get(name)

    def NewScreen(self, screen):
        self.Screens[screen.name] = screen

    def Run(self):
        while True:
            try:
                self._run()
                break
            except RuntimeError:
                pass

    def _run(self):
        while self.Running:
            self.delta_time = self.clock.tick(60)
            self.MainRoot.fill((0, 0, 0))
            self.Screens[self.Screen].render()

            for event in pygame.event.get():
                self.Screens[self.Screen].render(event)

            pygame.display.update()

        pygame.quit()
        pygame.font.quit()

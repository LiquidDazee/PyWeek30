from kivy.graphics import Rectangle
from settings import TILESIZE, WIDTH, HEIGHT




class Camera:
    def __init__(self, width, height):
        self.camera = Rectangle(pos = (0,0), size = (width, height))
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - 1024), x)  # right
        y = max(-(self.height - 768), y)  # bottom
        self.camera =  Rectangle(pos = (x,y), size = (self.width, self.height))
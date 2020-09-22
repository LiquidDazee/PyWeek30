# import os
# os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
#from kivy.uix.label import CoreLabel



class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._keyboard = Window.request_keyboard(
        self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

    
        self.register_event_type("on_frame")

        with self.canvas:
            Rectangle(source = "assets/bg.png", pos=(0, 0),
                      size=(Window.width, Window.height))
            
    
        self.keysPressed = set()
        self._entities = set()

        Clock.schedule_interval(self._on_frame, 0)
        

    def _on_frame(self, dt):
        self.dispatch("on_frame", dt)

    def on_frame(self, dt):
        pass


    def add_entity(self, entity):
        self._entities.add(entity)
        self.canvas.add(entity._instruction)

    def remove_entity(self, entity):
        if entity in self._entities:
            self._entities.remove(entity)
            self.canvas.remove(entity._instruction)


    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.keysPressed.add(keycode[1])

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)



class Entity():
    def __init__(self):
        self._pos = (0, 0)
        self._size = (50, 50)
        self._source = ""
        self._instruction = Rectangle(
            pos=self._pos, size=self._size, source=self._source) 

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value
        self._instruction.pos = self._pos

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        self._instruction.size = self._size

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
        self._instruction.source = self._source

    


class Wall(Entity):
    def __init__(self):
        super().__init__()
        self.source = "assets/sprite.png"
        

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.source = "assets/sprite.png"
        game.bind(on_frame=self.move_step)

    def collision(self, Entity):
        r1x = self.pos[0]
        r1y = self.pos[1]
        r2x = Entity.pos[0]
        r2y = Entity.pos[1]
        r1w = self.size[0]
        r1h = self.size[1]
        r2w = Entity.size[0]
        r2h = Entity.size[1]
        if(r1x<r2x+r2w and r1x+r1w>r2x and r1y<r2y+r2h and r1y+r1h>r2y):
            return True
        else:
            return False

    def move_step(self, sender, dt):
        currentx = self.pos[0]
        currenty = self.pos[1]
        oldpos = (currentx, currenty)
        newx = currentx
        newy = currenty

        step_size = 300*dt



        if "w" in game.keysPressed and newy<game.height - 50:
            newy += step_size
        if "s" in game.keysPressed and newy>0:
            newy -= step_size
        if "a" in game.keysPressed and newx>0:
            newx -= step_size
        if "d" in game.keysPressed and newx<game.width - 50:
            newx += step_size
        # self.player.pos = (newx, newy)
        newpos = (newx, newy)
        # if "w" in self.keysPressed or "d" in self.keysPressed or "a" in self.keysPressed or "s" in self.keysPressed:
        if newx != currentx or newy != currenty:
            for i in game.wall:
                if self.collision(i):
                    self.pos = oldpos
                    break
                else:
                    self.pos = newpos


game = GameWidget()
game.wall = []
for i in range(0,100):
    game.newwall=Wall()
    game.wall.append(game.newwall)
    game.wall[i].pos = (50, i * 30)
    game.add_entity(game.wall[i])
    print(game.wall[i].pos)
game.player = Player()
game.player.pos = (Window.width/2  , Window.height/2)
game.add_entity(game.player)



class MyApp(App):
    def build(self):
        return game

if __name__ == "__main__":
    app = MyApp()
    app.run()

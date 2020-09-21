# import os
# os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock

def collides(rect1, rect2):
    r1x = rect1[0][0]
    r1y = rect1[0][1]
    r2x = rect2[0][0]
    r2y = rect2[0][1]
    r1w = rect1[1][0]
    r1h = rect1[1][1]
    r2w = rect2[1][0]
    r2h = rect2[1][1]

    if(r1x<r2x+r2w and r1x+r1w>r2x and r1y<r2y+r2h and r1y+r1h>r2y):
        return True
    else:
        return False


class GameWidget(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self.width = Window.width
        self.height = Window.height

        # self.player.speed_modifier = 1
        with self.canvas:
            self.player = Rectangle(pos =(self.width/2-50,self.height/2-50), size=(100,100))
            self.enemy = Rectangle(pos = (400,400), size = (30, 30))

        self.keysPressed = set()
        Clock.schedule_interval(self.move_step, 0)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self,keyboard, keycode, text, modifiers):
        self.keysPressed.add(text)

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)

    def move_step(self, dt):
        currentx = self.player.pos[0]
        currenty = self.player.pos[1]
        oldpos = (currentx, currenty)
        newx = currentx
        newy = currenty

        step_size = 100*dt

        if "w" in self.keysPressed and newy<self.height-100:
            newy += step_size
        if "s" in self.keysPressed and newy>0:
            newy -= step_size
        if "a" in self.keysPressed and newx>0:
            newx -= step_size
        if "d" in self.keysPressed and newx<self.width-100:
            newx += step_size
        # self.player.pos = (newx, newy)
        newpos = (newx, newy)
        # if "w" in self.keysPressed or "d" in self.keysPressed or "a" in self.keysPressed or "s" in self.keysPressed:
        if newx != currentx or newy != currenty:
            if collides((newpos,self.player.size), (self.enemy.pos, self.enemy.size)):
                self.player.pos = oldpos
            else:
                self.player.pos = newpos

class MyApp(App):
    def build(self):
        return GameWidget()

if __name__ == "__main__":
    app = MyApp()
    app.run()

import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *


class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500,100)
        self.introduced = False
        self.load_data()

    def draw_text(self, text, font_name, size, color, x, y, align = "nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (round(x), round(y))
        self.screen.blit(text_surface, text_rect)

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.pause_font = path.join(game_folder, 'Rixel.otf')
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0, 0, 0, 100))
        self.map = TiledMap(path.join(game_folder, 'map.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()

        # lighting
        self.fog = pg.Surface((WIDTH, HEIGHT))
        self.fog.fill(NIGHT_COLOR)
        self.light_mask_img = pg.image.load(path.join(img_folder, LIGHT_MASK)).convert_alpha()
        self.light_mask = pg.transform.scale(self.light_mask_img, LIGHT_RADIUS)
        self.light_rect = self.light_mask.get_rect()
        self.item_images = {}
        for item in ITEM_IMAGES:
            self.item_images[item] = pg.image.load(path.join(img_folder, ITEM_IMAGES[item])).convert_alpha()
        self.path1 = ['','','','']
        self.path2 = ['','','','']
        self.path3 = ['','','','']



    def new(self):
        # init all var and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.boats = pg.sprite.Group()
        self.items = pg.sprite.Group()

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                self.player = Player(self,tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'win':
                Boat(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'enemy path 11':
                self.path1[0] = (tile_object.x, tile_object.y)
            if tile_object.name == 'enemy path 12':
                self.path1[1] = (tile_object.x, tile_object.y)
            if tile_object.name == 'enemy path 13':
                self.path1[2] = (tile_object.x, tile_object.y)
            if tile_object.name == 'enemy path 14':
                self.path1[3] = (tile_object.x, tile_object.y)
            if tile_object.name == 'enemy path 21':
                self.path2[0] = (tile_object.x, tile_object.y)
            if tile_object.name == 'enemy path 22':
                self.path2[1] = (tile_object.x, tile_object.y)
            if tile_object.name == 'enemy path 23':
                self.path2[2] = (tile_object.x, tile_object.y)
            if tile_object.name == 'enemy path 24':
                self.path2[3] = (tile_object.x, tile_object.y)
            if tile_object.name == 'enemy path 31':
                self.path3[0] = (tile_object.x, tile_object.y)
            if tile_object.name == 'enemy path 32':
                self.path3[1] = (tile_object.x, tile_object.y)
            if tile_object.name == 'enemy path 33':
                self.path3[2] = (tile_object.x, tile_object.y)
            if tile_object.name == 'enemy path 34':
                self.path3[3] = (tile_object.x, tile_object.y)

            if tile_object.name in ['torch']:
                Item(self,(tile_object.x, tile_object.y), tile_object.name)

            if tile_object.name in ['feather']:
                Item(self,(tile_object.x, tile_object.y), tile_object.name)

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'enemy 1':
                Mob(self, tile_object.x, tile_object.y, self.path1)
                # print("Mob1 added")
            if tile_object.name == 'enemy 2':
                Mob(self, tile_object.x, tile_object.y, self.path2)
                # print("Mob2 added")
            if tile_object.name == 'enemy 3':
                Mob(self, tile_object.x, tile_object.y, self.path3)
                # print("Mob3 added")

        self.camera = Camera(self.map.width, self.map.height)
        self.night = True
        self.torch = False
        self.paused = False
        self.winner = False
        self.start = False
        self.feather = False


    def intro(self):
        if not self.introduced:
            self.start =  True
            self.introduced = True
        else:
            print("I feel dizzy...")


    def run(self):

        # game loop - set self.playing = False to end the game
        self.playing = True
        self.intro()
        while self.playing:
            self.dt = self.clock.tick(FPS)/1000
            if not self.paused:
                if not self.winner:
                   self.update()
            self.events()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # Enemy hits player
        hits = pg.sprite.spritecollide(self.player, self.mobs, False)
        if (hits):
            print("hit")
            pg.time.wait(1000)
            self.playing = False

        #win condition
        win = pg.sprite.spritecollide(self.player, self.boats, False)
        if(win):
            print("you win")
            self.winner = True

        hits = pg.sprite.spritecollide(self.player, self.items, True)
        for hit in hits:
            if (hit.type == 'torch'):
                self.torch = True
            if (hit.type == 'feather'):
                self.feather = True
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        if self.feather:
            self.player.player_speed = 600
        print(self.feather)

    def draw_grid(self):
        for x in range(0,WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x,0), (x, HEIGHT))
        for y in range(0,HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0,y), (WIDTH, y))

    def render_fog(self, light_depth):
        # draw the light mask (gradient) onto fog image
        self.fog.fill(NIGHT_COLOR)
        self.light_mask = pg.transform.scale(self.light_mask_img, light_depth)
        self.light_rect = self.light_mask.get_rect()
        self.light_rect.center = self.camera.apply(self.player).center
        self.fog.blit(self.light_mask, self.light_rect)
        self.screen.blit(self.fog, (0,0), special_flags = pg.BLEND_MULT)

    def draw(self):
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        # self.screen.fill(BGCOLOR)
        # self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        # if self.night:
        #     self.render_fog()
        if self.torch:
            self.render_fog(TORCH_RADIUS)
        else:
            self.render_fog(LIGHT_RADIUS)

        if self.paused:
            self.screen.blit(self.dim_screen, (0, 0))
            self.draw_text("Paused", self.pause_font, 90, WHITE, WIDTH/2, HEIGHT/4, align = "center")

        if self.start:
            self.screen.blit(self.dim_screen, (0, 0))
            self.draw_text("Press any key to start", self.pause_font, 70, WHITE, WIDTH/2, HEIGHT/4, align = "center")

        if self.winner:
            self.screen.blit(self.dim_screen,(0,0))
            self.draw_text("You Win!", self.pause_font, 90, WHITE, WIDTH/2, HEIGHT/4, align = "center")
            self.draw_text("Press R to reset", self.pause_font, 45, WHITE, WIDTH/2, HEIGHT/2, align="center")

        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                self.start = False
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_n:
                    self.night = not self.night
                if event.key == pg.K_t:
                    self.torch = not self.torch
                if event.key == pg.K_p and self.winner != True:
                    self.paused = not self.paused
                if event.key == pg.K_r and self.winner == True:
                    self.playing = False
                if event.key == pg.K_f:
                    self.feather = not self.feather

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()

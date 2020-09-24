import pygame as pg
from settings import *
from collections import deque
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        # self.image = game.player_img
        self.image = pg.transform.scale(game.player_img, (TILESIZE, TILESIZE)) #increase sprite size to tilesize
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.pos = vec(x,y) * TILESIZE

    def get_keys(self):
        self.vel = vec(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
        if self.vel.x!=0 and self.vel.y!=0:
            self.vel *= 0.7071

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self,self.game.walls, False)
            if hits:
                if self.vel.x>0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x<0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self,self.game.walls, False)
            if hits:
                if self.vel.y>0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y<0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y

    def update(self):
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')


class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.path = deque([vec(200,200), vec(200,600),vec(600,600),vec(600,200)])
        self.nextpos = self.path.popleft()
        # self.nextpos = (300,300)
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.transform.scale(game.mob_img, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(-MOB_SPEED, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0
        self.target = game.player


    def update(self):
        target_dist = self.target.pos - self.pos
        if target_dist.length_squared() < DETECT_RADIUS**2:
            self.rot = target_dist.angle_to(vec(1, 0))
            self.image = pg.transform.rotate(pg.transform.scale(self.game.mob_img, (TILESIZE, TILESIZE)), 0)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            self.acc = vec(MOB_SPEED).rotate(-self.rot)
            self.acc += self.vel * -1
            self.vel += self.acc * self.game.dt
            self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
            self.rect.center = self.pos
        else:
            self.dist = self.nextpos - self.pos
            if not (-5<self.dist.x<5 and -5<self.dist.y<5):
                # move_dist = self.nextpos - self.pos
                # self.rot = move_dist.angle_to(vec(1, 0))
                # self.image = pg.transform.rotate(pg.transform.scale(self.game.mob_img, (TILESIZE, TILESIZE)), self.rot)
                # self.rect = self.image.get_rect()
                # self.rect.center = self.pos
                # self.acc = vec(MOB_SPEED).rotate(-self.rot)
                # self.acc += self.vel * -1
                # self.vel += self.acc * self.game.dt
                # self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
                # self.rect.center = self.pos
                # self.dist = self.nextpos - self.pos
                #print("Entered")
                # print(self.dist.length_squared())
                #print(self.dist)
                if (self.dist.x) < -5 :
                    self.vel.x = -MOB_SPEED
                    # print("1")
                elif (self.dist.x) > 5:
                    self.vel.x = MOB_SPEED
                    # print("2")
                else:
                    self.vel.x = 0

                if (self.dist.y) < -5 :
                    self.vel.y = -MOB_SPEED
                    # print(self.dist.y)
                elif (self.dist.y) > 5:
                    self.vel.y = MOB_SPEED
                    # print(self.dist.y)
                else:
                    self.vel.y = 0
                #print(self.dist.y)
                self.vel *= 0.7071
                self.pos += self.vel * self.game.dt
                self.rect.center = self.pos
            else:
                print("Else")
                self.path.append(self.nextpos)
                self.nextpos = self.path.popleft()



class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

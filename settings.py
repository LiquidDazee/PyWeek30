# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "The Loast Coast"
BGCOLOR = DARKGREY

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# player settings
PLAYER_SPEED = 500
PLAYER_IMG = 'manBlue.png'

# mob settings
MOB_IMG = 'manBlue.png'
MOB_SPEED = 400
DETECT_RADIUS = 200

# effects
NIGHT_COLOR = (10,10,10)
LIGHT_RADIUS = (420, 420)
TORCH_RADIUS = (900,900)
LIGHT_MASK = "light_350_soft.png"

# items
ITEM_IMAGES={'torch':'torch.png'}

# define some colors (R, G, B)
WHITE = (229, 229, 229)
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
PLAYER_SPEED_MODIFIER = 1
PLAYER_SPEED = 400
PLAYER_IMG = 'manBlue.png'

# mob settings
MOB_IMG = 'enemy.png'
MOB_SPEED = 400
DETECT_RADIUS = 300

# effects
NIGHT_COLOR = (20,20,20)
LIGHT_RADIUS = (450, 450)
TORCH_RADIUS = (900,900)
LIGHT_MASK = "light_350_soft.png"

# items
ITEM_IMAGES={'torch':'torch.png', 'feather':'feather.png'}
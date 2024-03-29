
import pygame as pg
vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
CYAN = (0, 255, 255)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
# WIDTH = 20   # 16 * 64 or 32 * 32 or 64 * 16
# HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 280
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'jugador_pistola.png'
PLAYER_SHOTGUN = 'Jugador_shotgun_1.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# Weapon settings
BULLET_IMG = 'bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {'bullet_speed': 500,
                     'bullet_lifetime': 1000,
                     'rate': 250,
                     'kickback': 200,
                     'spread': 5,
                     'damage': 10,
                     'bullet_size': 'lg',
                     'bullet_count': 1}
WEAPONS['shotgun'] = {'bullet_speed': 400,
                      'bullet_lifetime': 500,
                      'rate': 900,
                      'kickback': 300,
                      'spread': 20,
                      'damage': 30,
                      'bullet_size': 'sm',
                      'bullet_count': 12}

# Mob settings
ZOMBIE_IMG = ['tile004.png', 'tile005.png', 'tile006.png', 'tile007.png']
MOB_SPEEDS = [150, 100, 75, 125]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 400

# Zombie explosivo settings
ZOMBIE_EXPLO = ['Zombie_1.png', 'Zombie_2.png', 'Zombie_3.png']
MOB_SPEEDS_EXPLO = [150, 100, 75, 125]
MOB_HIT_RECT_EXPLO = pg.Rect(0, 0, 30, 30)
MOB_HEALTH_EXPLO = 200
MOB_DAMAGE_EXPLO = 20
MOB_KNOCKBACK_EXPLO = 20
AVOID_RADIUS_EXPLO = 50
DETECT_RADIUS_EXPLO = 400

# Boss settings
BOSS_IMG = ['boss.png', 'boss2.png', 'boss3.png', 'boss4.png']
BOSS_SPEEDS = [200, 150, 100, 150]
BOSS_HIT_RECT = pg.Rect(0, 0, 30, 30)
BOSS_HEALTH = 500
BOSS_DAMAGE = 50
BOSS_KNOCKBACK = 20
AVOID_RADIUS_BOSS = 40
DETECT_RADIUS_BOSS = 400

# Boss flaco settings
BOSS_FLACO_IMG = ['boss_gordo.png', 'boss_gordo.png']
BOSS_FLACO_SPEEDS = [500, 350, 250, 260]
BOSS_FLACO_HIT_RECT = pg.Rect(0, 0, 30, 30)
BOSS_FLACO_HEALTH = 600
BOSS_FLACO_DAMAGE = 40
BOSS_FLACO_KNOCKBACK = 20
AVOID_RADIUS_BOSS_FLACO = 50
DETECT_RADIUS_BOSS_FLACO = 400


# Effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png',
                  'whitePuff18.png']
SPLAT = 'splat green.png'
FLASH_DURATION = 50
DAMAGE_ALPHA = [i for i in range(0, 255, 55)]
NIGHT_COLOR = (20, 20, 20)
LIGHT_RADIUS = (500, 500)
LIGHT_MASK = "light_350_soft.png"

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
BOSS_LAYER = 2
BOSS_FLACO_LAYER = 2
MOB_EXPLO_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# Items
ITEM_IMAGES = {'health': 'health_pack.png',
               'shotgun': 'obj_shotgun.png'}
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 10
BOB_SPEED = 0.3

# Sounds
BG_MUSIC = 'bg_music.ogg'
BG_MUSIC_2 = 'bg_music2.mp3'
PLAYER_HIT_SOUNDS = ['pain/8.wav', 'pain/9.wav', 'pain/10.wav', 'pain/11.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav',
                      'zombie-roar-3.wav', 'zombie-roar-5.wav', 'zombie-roar-6.wav', 'zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
WEAPON_SOUNDS = {'pistol': ['pistol.wav'],
                 'shotgun': ['shotgun.wav']}
EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                  'health_up': 'health_pack.wav',
                  'gun_pickup': 'gun_pickup.wav'}

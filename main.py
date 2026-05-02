def on_up_pressed():
    global projectionX, projectionY
    projectionX = 0
    projectionY = -200
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_a_pressed():
    global projectile2
    projectile2 = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . b d b . . . . . .
            . . . . . . . b d b c . . . . .
            . . . . b b c 5 5 5 c b b . . .
            . . . . b 5 5 5 1 5 5 5 b . . .
            . . . c c 5 5 5 1 5 5 5 c c . .
            . . b b 5 5 5 1 1 1 5 5 5 b b .
            . . d d 5 1 1 1 1 1 1 1 5 d d .
            . . b b 5 5 5 1 1 1 5 5 5 b b .
            . . . c c 5 5 5 1 5 5 5 c c . .
            . . . . b 5 5 5 1 5 5 5 b . . .
            . . . . b b c 5 5 5 c b b . . .
            . . . . . . c b d b c . . . . .
            . . . . . . . b d b . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        mySprite,
        50,
        50)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    global projectionX, projectionY
    projectionX = -200
    projectionY = 0
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def scorePoint():
    global colectible1
    value: tiles.Location = None
    for value2 in tiles.get_tiles_by_type(sprites.dungeon.green_outer_west2):
        colectible1 = sprites.create(img("""
                ....................
                ....................
                ....................
                ....................
                ....................
                ....................
                .......22...22......
                ......2322.2222.....
                ......232222222.....
                ......222222222.....
                .......22222b2......
                ........222b2.......
                .........222........
                ..........2.........
                ....................
                ....................
                ....................
                ....................
                ....................
                ....................
                """),
            SpriteKind.food)
    tiles.place_on_tile(colectible1, value)
    tiles.set_tile_at(value, assets.tile("""
        transparency16
        """))

def on_overlap_tile(sprite, location):
    global current_level
    current_level += 1
    changelevel(current_level)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile)

def changelevel(level_number: number):
    if level_number == 1:
        tiles.set_current_tilemap(tilemap("""
            level2
            """))
    elif level_number == 2:
        tiles.set_current_tilemap(tilemap("""
            level4
            """))
    elif level_number == 3:
        tiles.set_current_tilemap(tilemap("""
            level6
            """))
    elif level_number == 4:
        tiles.set_current_tilemap(tilemap("""
            level1
            """))
    elif level_number == 5:
        tiles.set_current_tilemap(tilemap("""
            level0
            """))
    spawnEnemies()
    tiles.place_on_random_tile(mySprite, sprites.dungeon.stair_ladder)

def on_right_pressed():
    global projectionX, projectionY
    projectionX = 200
    projectionY = 0
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def spawnEnemies():
    global enemy1
    for value3 in tiles.get_tiles_by_type(sprites.builtin.forest_tiles0):
        enemy1 = sprites.create(img("""
                ........................
                ........................
                ........................
                ........................
                ..........ffff..........
                ........ff1111ff........
                .......fb111111bf.......
                .......f11111111f.......
                ......fd11111111df......
                ......fd11111111df......
                ......fddd1111dddf......
                ......fbdbfddfbdbf......
                ......fcdcf11fcdcf......
                .......fb111111bf.......
                ......fffcdb1bdffff.....
                ....fc111cbfbfc111cf....
                ....f1b1b1ffff1b1b1f....
                ....fbfbffffffbfbfbf....
                .........ffffff.........
                ...........fff..........
                ........................
                ........................
                ........................
                ........................
                """),
            SpriteKind.enemy)
        tiles.place_on_random_tile(enemy1, sprites.builtin.forest_tiles0)
        enemy1.follow(mySprite, 30)

def on_down_pressed():
    global projectionX, projectionY
    projectionX = 0
    projectionY = 200
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_overlap(sprite2, otherSprite):
    sprites.destroy(mySprite, effects.confetti, 500)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_overlap_tile2(sprite3, location2):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.green_outer_west2,
    on_overlap_tile2)

def on_on_overlap2(sprite4, otherSprite2):
    sprites.destroy(mySprite, effects.fire, 500)
    sprites.destroy(mySprite)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

def on_on_overlap3(sprite5, otherSprite3):
    sprites.destroy(otherSprite3)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

enemy1: Sprite = None
colectible1: Sprite = None
projectile2: Sprite = None
projectionY = 0
projectionX = 0
current_level = 0
mySprite: Sprite = None
scene.set_background_color(3)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . f f f f f f . . . . .
        . . . . f 5 4 5 5 4 5 f . . . .
        . . . f e 4 5 5 5 5 4 e f . . .
        . . f b 3 e 4 4 4 4 e 3 b f . .
        . f e 3 3 3 3 3 3 3 3 3 3 e f .
        . f 3 3 e b 3 e e 3 b e 3 3 f .
        . f b 3 f f e e e e f f 3 b f .
        . f b b f b f e e f b f b b f .
        . f b b e 1 f 4 4 f 1 e b b f .
        . f b b e e 4 4 4 4 4 f b b f .
        . . f 4 4 4 e d d d b f e f . .
        . . f e 4 4 e d d d d c 4 e . .
        . . . f e e d d b d b b f e . .
        . . . f f 1 d 1 d 1 1 f f . . .
        . . . . . f f f f f f . . . . .
        """),
    SpriteKind.player)
enemy2 = sprites.create_projectile_from_side(img("""
        ........................
        ........................
        ........................
        ........................
        ..........ffff..........
        ........ff1111ff........
        .......fb111111bf.......
        .......f11111111f.......
        ......fd11111111df......
        ......fd11111111df......
        ......fddd1111dddf......
        ......fbdbfddfbdbf......
        ......fcdcf11fcdcf......
        .......fb111111bf.......
        ......fffcdb1bdffff.....
        ....fc111cbfbfc111cf....
        ....f1b1b1ffff1b1b1f....
        ....fbfbffffffbfbfbf....
        .........ffffff.........
        ...........fff..........
        ........................
        ........................
        ........................
        ........................
        """),
    -80,
    0)
enemy2.set_kind(SpriteKind.enemy)
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
current_level = 1
changelevel(1)
info.set_life(3)
info.start_countdown(90)
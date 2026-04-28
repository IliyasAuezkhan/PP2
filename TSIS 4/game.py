import json
import random
import sys
import pygame
from pygame.locals import *
import db

def load_settings():
    try:
        with open('settings.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"snake_color": [46, 204, 113], "grid_on": True, "sound_on": True}

settings = load_settings()

FPS = 10 
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)


WHITE      = (255, 255, 255)
BLACK      = ( 23,  32,  42)
PURE_BLACK = (  0,   0,   0)
RED        = (231,  76,  60)
DARKGREEN  = ( 39, 174,  96)
DARKGRAY   = ( 52,  73,  94)
YELLOW     = (241, 196,  15)
BLUE       = ( 52, 152, 219)
PURPLE     = (155,  89, 182)
CYAN       = ( 26, 188, 156)
GRAY_TEXT  = (127, 140, 141)

SNAKE_COLOR = tuple(settings["snake_color"])
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
HEAD = 0 

def draw_button(text, x, y, w, h, inactive_color, active_color):
    mouse = pygame.mouse.get_pos()
    rect = pygame.Rect(x, y, w, h)
    is_hovered = rect.collidepoint(mouse)
    
    color = active_color if is_hovered else inactive_color
    pygame.draw.rect(DISPLAYSURF, color, rect, border_radius=5)
    pygame.draw.rect(DISPLAYSURF, WHITE, rect, 2, border_radius=5)
    
    font = pygame.font.Font('freesansbold.ttf', 18)
    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect()
    text_rect.center = rect.center
    DISPLAYSURF.blit(text_surf, text_rect)
    
    return is_hovered

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, USERNAME, PERSONAL_BEST
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snake Game - Advanced Pro')

    USERNAME = "Player1"
    PERSONAL_BEST = 0

    while True:
        action = showMainMenu()
        if action == 'play':
            PERSONAL_BEST = db.get_personal_best(USERNAME)
            score, level = runGame()
            db.save_result(USERNAME, score, level)
            showGameOverScreen(score, level)
        elif action == 'leaderboard':
            showLeaderboardScreen()
        elif action == 'settings':
            showSettingsScreen()

def runGame():
    global SNAKE_COLOR
    COUNT = 10
    growth_pending = 0
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    wormCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT

    score = 0
    level = 1
    current_fps = FPS
    
    obstacles = []
    apple = getRandomLocation_properties(wormCoords, obstacles, None, None)
    poison = getPoisonLocation(wormCoords, apple, obstacles, None)
    
    powerup = None
    powerup_spawn_time = pygame.time.get_ticks() + random.randint(5000, 10000)
    
    active_powerup = None
    powerup_end_time = 0
    has_shield = False

    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN

        now = pygame.time.get_ticks()
        game_speed = current_fps
        if active_powerup:
            if now > powerup_end_time:
                active_powerup = None
            elif active_powerup == 'speed':
                game_speed = current_fps + 10
            elif active_powerup == 'slow':
                game_speed = max(3, current_fps - 5)

        if now > apple['lifetime']:
            apple = getRandomLocation_properties(wormCoords, obstacles, poison, powerup)
            
        if not powerup and now > powerup_spawn_time:
            powerup = getPowerupLocation(wormCoords, apple, poison, obstacles)
            
        if powerup and now > powerup['lifetime']:
            powerup = None
            powerup_spawn_time = now + random.randint(10000, 15000)

        hit_obstacle = False
        if (wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or 
            wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT):
            hit_obstacle = True
            
        for obs in obstacles:
            if wormCoords[HEAD]['x'] == obs['x'] and wormCoords[HEAD]['y'] == obs['y']:
                hit_obstacle = True

        if hit_obstacle:
            if has_shield:
                has_shield = False
            else:
                return score, level 

        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                if has_shield:
                    has_shield = False
                else:
                    return score, level

        ate_apple = False
        
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            if settings.get('sound_on', True):
                pygame.mixer.Sound("eating_apple.wav").play()
            score += apple['weight']
            growth_pending += apple['weight'] - 1
            ate_apple = True
            
            if score >= COUNT:
                COUNT += 10
                current_fps += 2
                level += 1
                obstacles = generateObstacles(level, wormCoords)
            
            apple = getRandomLocation_properties(wormCoords, obstacles, poison, powerup)
            poison = getPoisonLocation(wormCoords, apple, obstacles, powerup)
            
        
        elif wormCoords[HEAD]['x'] == poison['x'] and wormCoords[HEAD]['y'] == poison['y']:
            if len(wormCoords) <= 3:
                return score, level 
            
            for _ in range(2):
                if len(wormCoords) > 1:
                    del wormCoords[-1]
            
            poison = getPoisonLocation(wormCoords, apple, obstacles, powerup)
            
        
        if powerup and wormCoords[HEAD]['x'] == powerup['x'] and wormCoords[HEAD]['y'] == powerup['y']:
            if powerup['type'] == 'shield':
                has_shield = True
            else:
                active_powerup = powerup['type']
                powerup_end_time = now + 5000 
            
            powerup = None
            powerup_spawn_time = now + random.randint(10000, 15000)

        
        if not ate_apple:
            if growth_pending > 0:
                growth_pending -= 1
            else:
                if len(wormCoords) > 1:
                    del wormCoords[-1]

        
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        
        wormCoords.insert(0, newHead)
        
        DISPLAYSURF.fill(BGCOLOR)
        if settings["grid_on"]:
            drawGrid()
        drawWorm(wormCoords, has_shield)
        drawApple(apple)
        drawPoison(poison)
        if powerup:
            drawPowerup(powerup)
        drawObstacles(obstacles)
        
        drawStatus(score, level, apple['lifetime'], active_powerup)
        
        pygame.display.update()
        FPSCLOCK.tick(game_speed)

def showMainMenu():
    global USERNAME
    titleFont = pygame.font.Font('freesansbold.ttf', 60)
    input_active = True
    
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        titleSurf = titleFont.render('Wormy Plus!', True, CYAN)
        titleRect = titleSurf.get_rect()
        titleRect.center = (WINDOWWIDTH / 2, 80)
        DISPLAYSURF.blit(titleSurf, titleRect)

        nameLabel = BASICFONT.render('Username: ', True, WHITE)
        DISPLAYSURF.blit(nameLabel, (150, 160))
        
        nameSurf = BASICFONT.render(USERNAME + ('|' if input_active else ''), True, YELLOW)
        DISPLAYSURF.blit(nameSurf, (270, 160))

        msg_text = 'Press [ENTER] to lock name' if input_active else 'Click a button to start'
        msgSurf = BASICFONT.render(msg_text, True, GRAY_TEXT)
        DISPLAYSURF.blit(msgSurf, (WINDOWWIDTH / 2 - 110, 200))

        play_hover = draw_button("Play Game", 220, 250, 200, 40, DARKGRAY, CYAN)
        lead_hover = draw_button("Leaderboard", 220, 300, 200, 40, DARKGRAY, CYAN)
        sett_hover = draw_button("Settings", 220, 350, 200, 40, DARKGRAY, CYAN)
        quit_hover = draw_button("Quit", 220, 400, 200, 40, DARKGRAY, RED)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if input_active:
                    if event.key == K_RETURN:
                        input_active = False
                    elif event.key == K_BACKSPACE:
                        USERNAME = USERNAME[:-1]
                    else:
                        if len(USERNAME) < 12 and event.unicode.isalnum():
                            USERNAME += event.unicode
                else:
                    if event.key == K_i: 
                        input_active = True
                        
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if not input_active and play_hover:
                        pygame.time.wait(150)
                        return 'play'
                    elif lead_hover:
                        pygame.time.wait(150)
                        return 'leaderboard'
                    elif sett_hover:
                        pygame.time.wait(150)
                        return 'settings'
                    elif quit_hover:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(30)

def showLeaderboardScreen():
    scores = db.get_top_scores(10)
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        titleSurf = BASICFONT.render('LEADERBOARD (TOP 10)', True, YELLOW)
        DISPLAYSURF.blit(titleSurf, (WINDOWWIDTH / 2 - 100, 40))
        
        y_offset = 100
        headers = ["Rank", "Player", "Score", "Level"]
        col_positions = [50, 150, 350, 500]
        
        for i, header in enumerate(headers):
            h_surf = BASICFONT.render(header, True, CYAN)
            DISPLAYSURF.blit(h_surf, (col_positions[i], y_offset))
            
        y_offset += 20
        pygame.draw.line(DISPLAYSURF, GRAY_TEXT, (50, y_offset), (590, y_offset))
        
        for i, row in enumerate(scores):
            y_offset += 25
            rank = f"#{i+1}"
            player = str(row[0]) if len(row) > 0 else "N/A"
            score = str(row[1]) if len(row) > 1 else "0"
            level = str(row[2]) if len(row) > 2 else "1"
            
            DISPLAYSURF.blit(BASICFONT.render(rank, True, YELLOW), (col_positions[0], y_offset))
            DISPLAYSURF.blit(BASICFONT.render(player, True, WHITE), (col_positions[1], y_offset))
            DISPLAYSURF.blit(BASICFONT.render(score, True, WHITE), (col_positions[2], y_offset))
            DISPLAYSURF.blit(BASICFONT.render(level, True, WHITE), (col_positions[3], y_offset))
            
        back_hover = draw_button("Back to Menu", 220, 410, 200, 40, DARKGRAY, CYAN)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and back_hover:
                    pygame.time.wait(150)
                    return 

        pygame.display.update()
        FPSCLOCK.tick(30)

def showSettingsScreen():
    global settings, SNAKE_COLOR
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        titleSurf = BASICFONT.render('SETTINGS', True, YELLOW)
        DISPLAYSURF.blit(titleSurf, (WINDOWWIDTH / 2 - 40, 40))
        
        grid_text = f"Grid Overlay: {'ON' if settings['grid_on'] else 'OFF'}"
        gridSurf = BASICFONT.render(grid_text, True, WHITE)
        DISPLAYSURF.blit(gridSurf, (100, 120))
        
        grid_hover = draw_button("Toggle Grid", 350, 110, 150, 35, DARKGRAY, CYAN)
        
        sound_text = f"Game Sound: {'ON' if settings.get('sound_on', True) else 'OFF'}"
        soundSurf = BASICFONT.render(sound_text, True, WHITE)
        DISPLAYSURF.blit(soundSurf, (100, 180))
        
        sound_hover = draw_button("Toggle Sound", 350, 170, 150, 35, DARKGRAY, CYAN)
        
        colorSurf = BASICFONT.render("Snake Color:", True, WHITE)
        DISPLAYSURF.blit(colorSurf, (100, 240))
        
        color_options = [
            {"rgb": [46, 204, 113], "name": "Emerald"},
            {"rgb": [52, 152, 219], "name": "Sky Blue"},
            {"rgb": [241, 196, 15], "name": "Yellow"}
        ]
        
        color_hovers = []
        for idx, col in enumerate(color_options):
            x_pos = 250 + (idx * 110)
            is_active = list(settings['snake_color']) == col["rgb"]
            btn_col = CYAN if is_active else DARKGRAY
            color_hovers.append(draw_button(col["name"], x_pos, 230, 100, 35, btn_col, tuple(col["rgb"])))

        save_hover = draw_button("Save & Back", 220, 350, 200, 40, DARKGRAY, CYAN)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if grid_hover:
                        settings['grid_on'] = not settings['grid_on']
                    if sound_hover:
                        settings['sound_on'] = not settings.get('sound_on', True)
                    for idx, hover in enumerate(color_hovers):
                        if hover:
                            settings['snake_color'] = color_options[idx]["rgb"]
                            SNAKE_COLOR = tuple(color_options[idx]["rgb"])
                    if save_hover:
                        with open('settings.json', 'w') as f:
                            json.dump(settings, f)
                        pygame.time.wait(150)
                        return

        pygame.display.update()
        FPSCLOCK.tick(30)

def showGameOverScreen(score, level):
    gameOverFont = pygame.font.Font('freesansbold.ttf', 50)
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        gameSurf = gameOverFont.render('Game Over', True, RED)
        gameRect = gameSurf.get_rect()
        gameRect.center = (WINDOWWIDTH / 2, 100)
        DISPLAYSURF.blit(gameSurf, gameRect)

        scoreSurf = BASICFONT.render(f'Final Score: {score} | Level: {level}', True, YELLOW)
        DISPLAYSURF.blit(scoreSurf, (WINDOWWIDTH / 2 - 120, 200))

        bestSurf = BASICFONT.render(f'Personal Best: {max(score, PERSONAL_BEST)}', True, CYAN)
        DISPLAYSURF.blit(bestSurf, (WINDOWWIDTH / 2 - 80, 240))

        back_hover = draw_button("Back to Menu", 220, 330, 200, 40, DARKGRAY, CYAN)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and back_hover:
                    pygame.time.wait(150)
                    return

        pygame.display.update()
        FPSCLOCK.tick(30)

def getRandomLocation_properties(wormCoords, obstacles, poison, powerup):
    occupied = list(wormCoords) + obstacles
    if poison:
        occupied.append({'x': poison['x'], 'y': poison['y']})
    if powerup:
        occupied.append({'x': powerup['x'], 'y': powerup['y']})
        
    while True:
        x = random.randint(0, CELLWIDTH - 1)
        y = random.randint(0, CELLHEIGHT - 1)
        if {'x': x, 'y': y} not in occupied:
            break
            
    chance = random.random()
    if chance < 0.2:
        return {'x' : x, 'y' : y, 'weight' : 3, 'color' : BLUE, 'lifetime' : 5000 + pygame.time.get_ticks()}
    elif chance < 0.45:
        return {'x' : x, 'y' : y, 'weight' : 2, 'color' : YELLOW, 'lifetime' : 8000 + pygame.time.get_ticks()}
    else:
        return {'x' : x, 'y' : y, 'weight' : 1, 'color' : RED, 'lifetime' : 10000 + pygame.time.get_ticks()}

def getPoisonLocation(wormCoords, apple, obstacles, powerup):
    occupied = list(wormCoords) + obstacles
    if apple:
        occupied.append({'x': apple['x'], 'y': apple['y']})
    if powerup:
        occupied.append({'x': powerup['x'], 'y': powerup['y']})
        
    while True:
        x = random.randint(0, CELLWIDTH - 1)
        y = random.randint(0, CELLHEIGHT - 1)
        if {'x': x, 'y': y} not in occupied:
            return {'x': x, 'y': y}

def getPowerupLocation(wormCoords, apple, poison, obstacles):
    occupied = list(wormCoords) + obstacles
    if apple:
        occupied.append({'x': apple['x'], 'y': apple['y']})
    if poison:
        occupied.append({'x': poison['x'], 'y': poison['y']})
        
    while True:
        x = random.randint(0, CELLWIDTH - 1)
        y = random.randint(0, CELLHEIGHT - 1)
        if {'x': x, 'y': y} not in occupied:
            break
            
    p_type = random.choice(['speed', 'slow', 'shield'])
    
    if p_type == 'speed':
        color = (255, 255, 255)
    elif p_type == 'slow':
        color = (0, 0, 0)
    else:
        color = (255, 105, 180)
        
    return {'x': x, 'y': y, 'type': p_type, 'color': color, 'lifetime': pygame.time.get_ticks() + 8000}

def generateObstacles(level, wormCoords):
    obstacles = []
    if level < 3:
        return obstacles
    num_obstacles = (level - 2) * 3
    for _ in range(num_obstacles):
        while True:
            x = random.randint(1, CELLWIDTH - 2)
            y = random.randint(1, CELLHEIGHT - 2)
            target = {'x': x, 'y': y}
            
            head_x = wormCoords[HEAD]['x']
            head_y = wormCoords[HEAD]['y']
            is_near_head = abs(x - head_x) <= 2 and abs(y - head_y) <= 2
            
            if target not in wormCoords and target not in obstacles and not is_near_head:
                obstacles.append(target)
                break
    return obstacles

def drawStatus(score, level, lifetime, powerup_type):
    scoreSurf = BASICFONT.render(f'Score: {score}', True, WHITE)
    levelSurf = BASICFONT.render(f'Level: {level}', True, YELLOW)
    bestSurf = BASICFONT.render(f'PB: {PERSONAL_BEST}', True, CYAN)
    
    DISPLAYSURF.blit(scoreSurf, (10, 10))
    DISPLAYSURF.blit(levelSurf, (120, 10))
    DISPLAYSURF.blit(bestSurf, (220, 10))

    t_left = max(0, ((lifetime - pygame.time.get_ticks()) // 1000))
    time_left = BASICFONT.render(f'Food: {t_left}s', True, RED)
    DISPLAYSURF.blit(time_left, (WINDOWWIDTH - 100, 10))
    
    if powerup_type:
        p_surf = BASICFONT.render(f'Buff: {powerup_type.upper()}', True, CYAN)
        DISPLAYSURF.blit(p_surf, (WINDOWWIDTH / 2 - 40, 10))

def drawWorm(wormCoords, has_shield):
    for i, coord in enumerate(wormCoords):
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, PURE_BLACK, wormSegmentRect, border_radius=3)
        
        inner_color = (255, 105, 180) if (i == 0 and has_shield) else SNAKE_COLOR
        wormInnerSegmentRect = pygame.Rect(x + 3, y + 3, CELLSIZE - 6, CELLSIZE - 6)
        pygame.draw.rect(DISPLAYSURF, inner_color, wormInnerSegmentRect, border_radius=2)

def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, coord['color'], appleRect, border_radius=10)

def drawPoison(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    poisonRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, PURPLE, poisonRect, border_radius=10)

def drawPowerup(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    powerRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, coord['color'], powerRect, border_radius=5)
   
    pygame.draw.rect(DISPLAYSURF, (127, 140, 141), powerRect, 1, border_radius=5)

def drawObstacles(obstacles):
    for obs in obstacles:
        x = obs['x'] * CELLSIZE
        y = obs['y'] * CELLSIZE
        obsRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, DARKGRAY, obsRect, border_radius=2)

def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, (33, 47, 61), (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, (33, 47, 61), (0, y), (WINDOWWIDTH, y))

main()
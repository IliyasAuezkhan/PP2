import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    current_color = (255, 0, 0) 
    mode = 'pen' 
    
    
    points = []
    
    drawing = False
    start_pos = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: current_color = (255, 0, 0)
                if event.key == pygame.K_g: current_color = (0, 255, 0)
                if event.key == pygame.K_b: current_color = (0, 0, 255)
                if event.key == pygame.K_w: current_color = (255, 255, 255)
                
                if event.key == pygame.K_1: mode = 'pen'
                if event.key == pygame.K_2: mode = 'rect'
                if event.key == pygame.K_3: mode = 'circle'
                if event.key == pygame.K_4: mode = 'eraser'

           
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                if mode == 'pen' or mode == 'eraser':
                    color = (0, 0, 0) if mode == 'eraser' else current_color
                    points.append(('point', color, event.pos, radius))
            
            if event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    end_pos = event.pos
                    if mode == 'rect':
                        points.append(('rect', current_color, (start_pos, end_pos)))
                    elif mode == 'circle':
                        points.append(('circle', current_color, (start_pos, end_pos)))
                drawing = False

            if event.type == pygame.MOUSEMOTION and drawing:
                if mode == 'pen' or mode == 'eraser':
                    color = (0, 0, 0) if mode == 'eraser' else current_color
                    points.append(('point', color, event.pos, radius))

        screen.fill((0, 0, 0))
        
        
        for shape in points:
            if shape[0] == 'point':
                pygame.draw.circle(screen, shape[1], shape[2], shape[3])
            elif shape[0] == 'rect':
                s, e = shape[2]
                rect = pygame.Rect(min(s[0], e[0]), min(s[1], e[1]), 
                                 abs(s[0] - e[0]), abs(s[1] - e[1]))
                pygame.draw.rect(screen, shape[1], rect, 2)
            elif shape[0] == 'circle':
                s, e = shape[2]
                r = int(((s[0]-e[0])**2 + (s[1]-e[1])**2)**0.5)
                pygame.draw.circle(screen, shape[1], s, r, 2)

        
        if drawing and start_pos:
            curr_pos = pygame.mouse.get_pos()
            if mode == 'rect':
                temp_rect = pygame.Rect(min(start_pos[0], curr_pos[0]), min(start_pos[1], curr_pos[1]), 
                                      abs(start_pos[0] - curr_pos[0]), abs(start_pos[1] - curr_pos[1]))
                pygame.draw.rect(screen, current_color, temp_rect, 1)
            elif mode == 'circle':
                temp_r = int(((start_pos[0]-curr_pos[0])**2 + (start_pos[1]-curr_pos[1])**2)**0.5)
                pygame.draw.circle(screen, current_color, start_pos, temp_r, 1)

        pygame.display.flip()
        clock.tick(60)

main()

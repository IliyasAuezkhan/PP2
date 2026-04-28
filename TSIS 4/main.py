import pygame
import db
import game

def main():
    
    db.init_db()
    
    
    pygame.init()
    pygame.mixer.init()
    
    
    game.main()

main()

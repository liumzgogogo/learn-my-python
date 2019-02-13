#-*- coding:utf8 -*-
import sys
import pygame
from settings import Settings
from ship import Ship
import game_funcs as gf
from pygame.sprite import Group
from alien import Alien
def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("异形进攻")

    ship = Ship(ai_settings,screen)
    
    #创建一个用于存储子弹的编组
    bullets = Group()

    #创建一个外星人
    #alien = Alien(ai_settings,screen)
    #创建外星人群
    aliens=Group()
    gf.create_fleet(ai_settings,screen,aliens)
    

    while True:

        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        gf.update_aliens(ai_settings,ship,aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
       
#-------------------------------------------

if __name__=="__main__":
    run_game()

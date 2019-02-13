#-*- coding:utf8 -*-
import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
         if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
         elif event.type == pygame.KEYDOWN:
             check_keydown_events(event,ai_settings,screen,ship,bullets)
         elif event.type == pygame.KEYUP:
             check_keyup_events(event,ship)
        
                  

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
         ship.moving_right = True
    elif event.key == pygame.K_LEFT:
         ship.moving_left = True
    elif event.key == pygame.K_SPACE:
         fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
         pygame.quit()
         sys.exit()
        

def check_keyup_events(event,ship):
    
    if event.key == pygame.K_RIGHT:
         ship.moving_right = False
    elif event.key == pygame.K_LEFT:
         ship.moving_left = False

def update_screen(ai_settings,screen,ship,aliens,bullets):
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets):
    #更新子弹位置
     bullets.update()
    #删除消失的子弹
     for bullet in bullets.copy():
         if bullet.rect.bottom <=0:
             bullets.remove(bullet)
     check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):   
     #检查是否有子弹击中外星人，有就删除外星人和子弹"""
     collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

     if len(aliens) == 0:
         bullets.empty()
         create_fleet(ai_settings,screen,ship,aliens)

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings,screen,aliens):
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    # 创建第一行外星人
    for alien_number in range(number_aliens_x):
    # 创建一个外星人并将其加入当前行
        create_alien(ai_settings,screen,aliens,alien_number)
def get_number_aliens_x(ai_settings,alien_width):
    '''计算每行可容纳多少个外星人'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
def create_alien(ai_settings,screen,aliens,alien_number):
     alien = Alien(ai_settings, screen)
     alien_width = alien.rect.width
     alien.x = alien_width + 2 * alien_width * alien_number
     alien.rect.x = alien.x
     aliens.add(alien)

def update_aliens(ai_settings,ship,aliens):
    """更新外星人群众所有外星人的位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #监测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        print("Ship hit!!!")
    

def check_fleet_edges(ai_settings,aliens):
    '''有外星人到达边缘采取相应措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

    

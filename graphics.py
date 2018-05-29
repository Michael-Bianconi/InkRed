"""graphics"""

import pygame, sys
from settings import SCREEN_HEIGHT, SCREEN_WIDTH
from player_class import Player
from barrier_class import Barrier
from laser_class import Laser, laser_create
from center_text_class import CenterText
from repeated_timer import RepeatedTimer

pygame.display.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
exit_condition = False
death = False
victory = False

victory_text = CenterText('You won!',(0,0,0))
death_text = CenterText('You died!',(255,0,0))

lasers = []
laser_speed = 1
laser_interval = 1.5
laser_timer = RepeatedTimer(laser_interval, laser_create, lasers, laser_speed)

player = Player()
bottom_barrier = Barrier('bottom')
right_barrier = Barrier('right')
left_barrier = Barrier('left')
top_barrier = Barrier('top')



while not exit_condition:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit_condition = True
		if event.type == pygame.KEYDOWN:
			player.key_pressed(event.key)
		elif event.type == pygame.KEYUP:
			player.key_depressed(event.key)
			
	screen.fill((255,255,255))
	player.tick()
	
	bottom_barrier.draw(screen) #draw cyan barrier at bottom
	top_barrier.draw(screen)
	left_barrier.draw(screen)
	right_barrier.draw(screen)		
	
	
	for i, l in enumerate(lasers):
		if l.end_of_life(): del lasers[i]
		l.tick()
		l.draw(screen)
		if player.collision(l):
			death = True
	
	if player.victory(): victory = True
	
	if victory:
		victory_text.draw(screen)
	elif death:
		death_text.draw(screen)
	else:
		player.draw(screen) #draw player

	pygame.display.flip()
	clock.tick(60)
	
pygame.display.quit()
laser_timer.stop()
sys.exit()

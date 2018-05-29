"""Player"""

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from barrier_class import BOTTOM,TOP,LEFT,RIGHT

BLACK = (0,0,0)

class Player(object):
	
	size = 10
	#			X,Y
	location = [int(SCREEN_WIDTH / 2),BOTTOM-size]
	
	gravity = 2
	
	v_speed = gravity
	h_speed = 0
	
	h_velocity = 4
	v_velocity = 3
	
	def draw(self,screen):
		pygame.draw.rect(screen,BLACK,[self.location[0],
									   self.location[1],
									   self.size,self.size])
	
	def teleport(location):
		self.location = location
		
	def collision(self,laser):
		height = [self.location[1],self.location[1]+self.size]
		
		#correct height
		if height[0] <= laser.left_start[1] <= height[1]:
			width = [self.location[0],self.location[0]+self.size]
			
			if width[1] <= laser.gap[0] or width[0] >= laser.gap[1]:
				return True
		
		return False
		
	
	def victory(self):
		return self.location[1] <= TOP

		
	def tick(self):
		#check for bottom bound
		if self.location[1] + self.size >= BOTTOM:
			self.location[1] = BOTTOM - self.size
			
		#check for top
		elif self.location[1] < TOP:
			self.location[1] = TOP
			
		#left
		if self.location[0] < LEFT:
			self.location[0] = LEFT
		
		#right
		elif self.location[0] + self.size >= RIGHT:
			self.location [0] = RIGHT - self.size
	
		self.location[0] += self.h_speed
		self.location[1] += self.v_speed
		
	def key_pressed(self,key):
		if key == pygame.K_LEFT:
			self.h_speed -= self.h_velocity
		elif key == pygame.K_RIGHT:
			self.h_speed += self.h_velocity
		if key == pygame.K_UP:
			self.v_speed -= self.v_velocity
			
	def key_depressed(self,key):
		if key == pygame.K_LEFT:
			self.h_speed += self.h_velocity
		elif key == pygame.K_RIGHT:
			self.h_speed -= self.h_velocity
		elif key == pygame.K_UP:
			self.v_speed = self.gravity
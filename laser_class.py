"""laser destroys player on contact"""

import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH
from barrier_class import LEFT,RIGHT
import random

RED = (255,0,0)
GAP_SIZE = 40

def laser_create(lasers,speed):
	gap_start = random.randint(LEFT,SCREEN_WIDTH - GAP_SIZE)
	l = Laser(speed,[gap_start,gap_start+GAP_SIZE])
	lasers.append(l)

class Laser(object):

	gap = [0,0]
	speed = 0
	
	def __init__(self,speed,gap):
		self.speed = speed
		self.gap = gap
		self.left_start = [0,0]
		self.left_end = [gap[0],0]
		self.right_start = [gap[1],0]
		self.right_end = [SCREEN_WIDTH,0]
	
	def tick(self):
		self.left_start[1] += self.speed
		self.left_end[1] += self.speed
		self.right_start[1] += self.speed
		self.right_end[1] += self.speed
	
	def draw(self,screen):
		pygame.draw.line(screen,RED,self.left_start,self.left_end)
		pygame.draw.line(screen,RED,self.right_start,self.right_end)
		
	def end_of_life(self):
		return self.left_start[1] >= SCREEN_HEIGHT
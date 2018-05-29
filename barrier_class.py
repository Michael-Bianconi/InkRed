"""Barrier Class"""
import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

CYAN = (0,255,255)

TOP = 25
BOTTOM = SCREEN_HEIGHT - 25
LEFT = 25
RIGHT = SCREEN_WIDTH - 25

class Barrier(object):

	def __init__(self,side):
		if side == 'bottom':
			self.start = [LEFT,BOTTOM]
			self.end = [RIGHT,BOTTOM]
		elif side == 'top':
			self.start = [LEFT,TOP]
			self.end = [RIGHT,TOP]
		elif side == 'left':
			self.start = [LEFT,TOP]
			self.end = [LEFT,BOTTOM]
		elif side == 'right':
			self.start = [RIGHT,TOP]
			self.end = [RIGHT,BOTTOM]
	
	def draw(self,screen):
		pygame.draw.line(screen,CYAN,self.start,self.end,3)
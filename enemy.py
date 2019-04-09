import pygame, sys, random

class enemy(object):
	
	def __init__(self, game, lt, rb, colour = (0,0,0)):
		self.game = game
		self.lt = lt
		self.rb = rb
		self.colour = colour
		
	def give_size(self):
		s = (self.rb[0]-self.lt[0], self.rb[1]-self.lt[1])
		return s
	
	def box(self):
		r = pygame.Rect(self.lt[0], self.lt[1], self.give_size()[0], self.give_size()[1])
		return r
	
	def move_rand(self):
		pass
		
	def delete(self):
		pass


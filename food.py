import pygame, sys, random

class food(object):
	def __init__(self, game):
		self.game = game
		self.colour = self.game.br
		self.size = 10
		self.bufor_x = (self.game.board_size[1][0]-self.game.board_size[0][0])*0.1
		self.bufor_y	= (self.game.board_size[1][1]-self.game.board_size[0][1])*0.1
		self.x = random.randint(self.game.board_size[0][0]+self.bufor_x,self.game.board_size[1][0]-self.bufor_x)
		self.y = random.randint(self.game.board_size[0][1]+self.bufor_y,self.game.board_size[1][1]-self.bufor_y)
		self.how_nutr = 1
		

	def box(self):
		b = pygame.Rect(self.x, self.y, self.size, self.size)
		return b
	
	def move_rand(self):
		self.x = random.randint(self.game.board_size[0][0]+self.bufor_x,self.game.board_size[1][0]-self.bufor_x)
		self.y = random.randint(self.game.board_size[0][1]+self.bufor_y,self.game.board_size[1][1]-self.bufor_y)
		self.how_nutr = random.randint(10,20)
		self.size = 5 + self.how_nutr * 1
		if self.collision(self.game.wonsz.list_of_boxes):
			self.move_rand()											#moze byc problem jak za duzo razy trafi na weza
		
	def collision(self, wrog = []):				#kolizje z wezem
		if len(wrog) > 0:
			for i in wrog:
				dx = i[0][0]-self.x
				dy = i[0][1]-self.y	
				part_width = i[1][0]-i[0][0]
				part_height = i[1][1]-i[0][1]
				if dx > (-1)*part_width and dx < self.size and dy > (-1)*part_height and dy < self.size:
					return True
					
		return False
			
							
		

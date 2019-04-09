import pygame, sys, random, time
from pyton import pyton
from food import food
from enemy import enemy

class Game(object):
	
	def __init__(self):
		
		#parametry
		if True:
			self.max_tps = 20.0
			self.res = (1200, 700)
			self.infobox_height = 60
			self.infobox_colour = (0,0,0)
			self.infobox = pygame.Rect(0,0,self.res[0],self.infobox_height)
			self.board_size = ((0, self.infobox_height), self.res)
			self.bg = (124,252,0)
			self.snake_colour = (0,100,0)
			self.br = (128,128,0)
			self.d = 10
			self.text_colour = (255,255,255)
			
			self.LICZNIK = 0 		#debug!
			
			#inicjalizacja
			
			pygame.init()
			self.screen = pygame.display.set_mode(self.res, pygame.FULLSCREEN)
			self.clock = pygame.time.Clock()
			self.time_from_start = 0.0
			self.font = pygame.font.SysFont("monospace", 40)
			self.wonsz = pyton(self)
			self.jedzenie = food(self)	
			self.jedzenie.move_rand()			
			self.czesci_weza = []
		#przebieg
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit(0)
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
						sys.exit(0)
						
			
			self.time_from_start += self.clock.tick() / 1000.0
			while self.time_from_start > 1/self.max_tps:
				self.time_from_start-= 1/self.max_tps
				self.tick()
			
			self.screen.fill(self.bg)
			self.draw(self.czesci_weza)
			pygame.display.flip()
			
	def is_snake_eating(self, snak, sth_to_eat):
		dx = sth_to_eat.x - snak.x
		dy = sth_to_eat.y - snak.y 
		if dx > (-1)*sth_to_eat.size and dx < snak.how_big and dy > (-1)*sth_to_eat.size and dy < snak.how_big:
			snak.eat(sth_to_eat.how_nutr)
			sth_to_eat.move_rand()
			snak.to_grow+=sth_to_eat.how_nutr

	
	def collision(self, snak, wrog = []):
		if len(wrog) <= 2:						
			pass
		else:
			t = len(wrog)
			for i in range(t-2):
				dx = wrog[i][0][0]-snak.x
				dy = wrog[i][0][1]-snak.y	
				part_width = wrog[i][1][0]-wrog[i][0][0]
				part_height = wrog[i][1][1]-wrog[i][0][1]
				if dx > (-1)*part_width and dx < snak.how_big and dy > (-1)*part_height and dy < snak.how_big:
					self.end()
		
	def tick(self):
		self.keys = pygame.key.get_pressed()
		if self.keys[pygame.K_DOWN]:
			self.wonsz.t_down()
		if self.keys[pygame.K_UP]:
			self.wonsz.t_up()
		if self.keys[pygame.K_LEFT]:
			self.wonsz.t_left()
		if self.keys[pygame.K_RIGHT]:
			self.wonsz.t_right()
		
		self.collision(self.wonsz, self.wonsz.list_of_boxes)
		self.is_snake_eating(self.wonsz, self.jedzenie)
		self.wonsz.move()
	
	def make_box(self, T):
		Box = pygame.Rect(T[0][0], T[0][1], T[1][0]-T[0][0], T[1][1]-T[0][1])
		return Box	
		
	def draw(self, cz_w = []):
		if len(cz_w) == 0:
			cz_w = self.wonsz.list_of_boxes
		
		pygame.draw.rect(self.screen, self.infobox_colour, self.infobox)
		label = self.font.render(str(self.wonsz.length), 1, self.text_colour)
		logo = self.font. render("PYTON", 1, self.text_colour)
		self.screen.blit(logo, (10, 10))
		self.screen.blit(label, (self.res[0]-100, 10))
		
		
		if len(cz_w)>0:
			for i in cz_w:
				b = self.make_box(i)
				pygame.draw.rect(self.screen, self.snake_colour, b)
		
		b = pygame.Rect(self.wonsz.end[0],self.wonsz.end[1],self.wonsz.how_big,self.wonsz.how_big)
		pygame.draw.rect(self.screen, self.snake_colour, b)
		pygame.draw.rect(self.screen, self.br, self.jedzenie.box())
		pygame.draw.rect(self.screen, self.snake_colour, self.wonsz.box())
		
	def end(self):
		self.screen.fill(self.infobox_colour)
		text = self.font.render("THE END", 1, self.text_colour)
		score = self.font.render("YOUR SCORE IS " + str(self.wonsz.length), 1, self.text_colour)
		self.screen.blit(text, (100,100))
		self.screen.blit(score, (100,150))
		pygame.display.flip()
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit(0)
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
						sys.exit(0)

if __name__ == "__main__":
	Game()



	
		

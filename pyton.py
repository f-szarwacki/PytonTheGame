import pygame, sys, random


class pyton(object):
	u'''dodajemy historie miejsc gdzie skrecal i koniec, w kazdym ruchu koniec sie porusza, chyba, ze zjadl
			zdaje sie ze trzeba tylko aktualizowac liste, a nie za kazdym razem przesylac nowa bo nie dziala wtedy
	
	'''
	def __init__(self, game, colour = (255, 0, 0), direction = 'r'):
		self.game = game
		self.colour = colour
		self.direction = direction
		self.length = 0
		self.x = self.game.board_size[0][0]+200
		self.y = self.game.board_size[0][1]+200
		self.how_big = 20
		self.head = [self.x, self.y, direction]	
		self.end = [self.x-50, self.y, direction]
		self.track = []			#tablica krotek gdzie skret i w ktora strone								
		self.to_grow = 0
		self.list_of_boxes = [((self.end[0],self.end[1]),(self.head[0]+self.how_big,self.head[1]+self.how_big))]
	
	def t_up(self):															#jeszcze skrecanie trzeba ogarnac
		if self.direction == 'r' or self.direction == 'l':
			self.direction = 'u'
			self.track.append((self.x, self.y, self.direction))
			self.list_of_boxes[-1] = self.part(-3)
			self.list_of_boxes.append(self.part(-2))						#!
		
	def t_down(self):
		if self.direction == 'r' or self.direction == 'l':
			self.direction = 'd'
			self.track.append((self.x, self.y, self.direction))
			self.list_of_boxes[-1] = self.part(-3)
			self.list_of_boxes.append(self.part(-2))						#!
			
	def t_left(self):
		if self.direction == 'u' or self.direction == 'd':
			self.direction = 'l'
			self.track.append((self.x, self.y, self.direction))
			self.list_of_boxes[-1] = self.part(-3)
			self.list_of_boxes.append(self.part(-2))					#!
			
	def t_right(self):
		if self.direction == 'u' or self.direction == 'd':
			self.direction = 'r'
			self.track.append((self.x, self.y, self.direction))
			self.list_of_boxes[-1] = self.part(-3)
			self.list_of_boxes.append(self.part(-2))						#!
			
	def move(self):
		if self.direction == 'u':
			self.y-=self.game.d
			self.list_of_boxes[-1]=self.part(-2)			#!
		elif self.direction == 'd':
			self.y+=self.game.d
			self.list_of_boxes[-1]=self.part(-2)		#!
		elif self.direction == 'r':
			self.x+=self.game.d
			self.list_of_boxes[-1]=self.part(-2)		#!
		elif self.direction == 'l':
			self.x-=self.game.d
			self.list_of_boxes[-1]=self.part(-2)		#!
		self.head[0]=self.x
		self.head[1]=self.y
		
		if self.to_grow > 0:									#czy rozciagnac weza
			self.to_grow-=1										#jezeli jadl to nie przenosimy konca
		else:
			if self.end[2] == 'u':
				self.end[1]-=self.game.d
				self.list_of_boxes[0]=self.part(0)	#!
			elif self.end[2] == 'd':
				self.end[1]+=self.game.d
				self.list_of_boxes[0]=self.part(0)	#!
			elif self.end[2] == 'r':
				self.end[0]+=self.game.d
				self.list_of_boxes[0]=self.part(0)		#!
			elif self.end[2] == 'l':
				self.end[0]-=self.game.d
				self.list_of_boxes[0]=self.part(0)		#!
			
			if len(self.track)>0:
				cel = self.track[0]
				'''if self.end[0] == cel[0] and self.end[1] == cel[1]:
					#print('skret')
					self.end[2] = cel[2]										#ponizej rozwiazanie dzialajacce tylko jesli nic innego sie nie popsuje
					self.track.remove(cel)
				'''	
				if self.end[2]=='r':					#przy kazdym takim poleceniu usuwamy ostatni czlon weza
					if self.end[0] >= cel[0]:
						self.end[2] = cel[2]
						self.track.remove(cel)
						self.list_of_boxes.pop(0)		#!				
				elif self.end[2]=='l':
					if self.end[0] <= cel[0]:
						self.end[2] = cel[2]
						self.track.remove(cel)
						self.list_of_boxes.pop(0)		#!
				elif self.end[2]=='u':
					if self.end[1] <= cel[1]:
						self.end[2] = cel[2]
						self.track.remove(cel)
						self.list_of_boxes.pop(0)		#!
				elif self.end[2]=='d':
					if self.end[1] >= cel[1]:
						self.end[2] = cel[2]
						self.track.remove(cel)
						self.list_of_boxes.pop(0)		#!
	
				
		if True:		
			#chwilowo bez przechodzenia, bariery przy scianach
			if self.x < self.game.board_size[0][0]:
				self.game.end()
			elif self.x > self.game.board_size[1][0]:
				self.game.end()
			if self.y < self.game.board_size[0][1]:
				self.game.end()
			elif self.y > self.game.board_size[1][1]:
				self.game.end()
	
	
	def box(self):
		b = pygame.Rect(self.x,self.y,self.how_big,self.how_big)
		return b
	
	def list_of_parts(self):		#ma zwrocic liste par punktow lt i rb
		T = []							#cos tu nie tak
		L = self.track
		L.insert(0,self.end)
		L.append(self.head)
		t = len(L)
		for i in range(t-1):
			cur_pos = L[i]
			next_pos = L[i+1]
			if cur_pos[2] == 'r':
				T.append(((cur_pos[0],cur_pos[1]),(next_pos[0]+self.how_big,next_pos[1]+self.how_big)))
			elif cur_pos[2] == 'l':
				T.append(((next_pos[0],next_pos[1]),(cur_pos[0]+self.how_big,cur_pos[1]+self.how_big)))
			elif cur_pos[2] == 'd':
				T.append(((cur_pos[0],cur_pos[1]),(next_pos[0]+self.how_big,next_pos[1]+self.how_big)))
			elif cur_pos[2] == 'u':
				T.append(((next_pos[0],next_pos[1]),(cur_pos[0]+self.how_big,cur_pos[1]+self.how_big)))

		return T
		
	def part(self, i):
		if i == 0:
			cur_pos = self.end
			if len(self.track) == 0:
				next_pos = self.head
			else:
				next_pos = self.track[0]
		elif i == -2:
			if len(self.track) == 0:
				cur_pos = self.end
			else:	
				cur_pos = self.track[-1]
			next_pos = self.head
		elif i == -3:
			if len(self.track) == 0:
				print("nwm cco robic")
			else:
				if len(self.track) == 1:
					cur_pos = self.end
				else:
					cur_pos = self.track[-2]
				next_pos = self.track[-1]
		else:
			print("COS NIE TAK")
		
		#L = self.track
		#L.insert(0,self.end)
		#L.append(self.head)		#bez sensu
		#cur_pos = L[i]
		#next_pos = L[i+1]
		
		if cur_pos[2] == 'r':
			T=((cur_pos[0],cur_pos[1]),(next_pos[0]+self.how_big,next_pos[1]+self.how_big))
		elif cur_pos[2] == 'l':
			T=((next_pos[0],next_pos[1]),(cur_pos[0]+self.how_big,cur_pos[1]+self.how_big))
		elif cur_pos[2] == 'd':
			T=((cur_pos[0],cur_pos[1]),(next_pos[0]+self.how_big,next_pos[1]+self.how_big))
		elif cur_pos[2] == 'u':
			T=((next_pos[0],next_pos[1]),(cur_pos[0]+self.how_big,cur_pos[1]+self.how_big))
		return T
		
	def eat(self, how_much):
		self.length+=how_much

	

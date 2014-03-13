import pygame

class Button(object):
	def __init__(self, point_x, point_y, length_x, length_y, color, Main_Screen): #Color is a list of 3 indeces. [RED, GREEN, BLUE]
		self.point_x = point_x
		self.point_y = point_y
		self.length_x = length_x
		self.length_y = length_y
		self.color = color
		self.Main_Screen = Main_Screen
		self.Rectangle = pygame.Rect(self.point_x, self.point_y, self.length_x, self.length_y)
		self.Surface = pygame.Surface([self.length_x, self.length_y])
		self.Surface.fill((self.color[0], self.color[1], self.color[2]))
	def Do(self):
		self.Main_Screen.blit(self.Surface, self.Rectangle)
		
#-----------------------------------------------------------------------------------------------------------------------------------------

class Flavour(object):
	def __init__(self, color, price, calories=100):
		self.color = color
		self.price = price
		self.calories = calories

#-----------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
	y = 10
	pygame.init()
	Screen = pygame.display.set_mode((500, 500))
	Screen.fill((255,255,213))
	Lemon = Button(10,y,45,45,[255,213,0],Screen)
	counter	= 0
	while True and y <= 600:
		ev = pygame.event.poll()
		pygame.display.flip()
		Lemon = Button(10,y,45,45,[255,213,0],Screen)	
		Lemon.Do()
		y += 65
		counter += 1
	print counter

#Lemon
#Strawberry
#Chocolate
#Vanilla
#Mint
#Pineapple
#Kiwi
#Blueberries
#Coffee
#Oranges
	

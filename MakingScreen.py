import pygame
from Classes import *
from label import *

#---------------------------------------------------------------------------------------------------------------------
#This right here is the funtion
#That you are supposed to use
#If you want to draw
#The page with all the buttons
#For Flavors, Toppings, and Cone Size
#
#USE ONLY THIS HERE FUNCTION

def DrawLayout(Screen): ##This draws the WHOLE page
	Draw_Layout_LeftSide(AddFlavorButtons(Screen))
	Draw_Cone(Screen)
	Draw_DoneButton(Screen)
	
#---------------------------------------------------------------------------------------------------------------------

def Draw_Layout_LeftSide(Flavors):
	for i in Flavors:
		i.Do()

#---------------------------------------------------------------------------------------------------------------------

def AddFlavorButtons(Screen):
	Buttons = []
	global Lemon 

	Lemon = Button(0,100,50,50,[255,255,0], Screen)

	#TextAt(0,100,50,50,10, "Lemon", (0,0,0), Screen)
	Buttons.append(Lemon) #Lemon
	
	global Chocolate 
	Chocolate = Button(0,150+20,50,50,[102,51,0], Screen)
	Buttons.append(Chocolate) #Chocolate

	global Vanilla
	Vanilla = Button(0,200+40,50,50,[255,255,204], Screen)
	Buttons.append(Vanilla) #Vanilla

	global Strawberry
	Strawberry = Button(0,250+60,50,50,[255,102,102], Screen)
	Buttons.append(Strawberry) #Strawberry

	global Pistachio
	Pistachio = Button(0,300+80,50,50,[153,255,153], Screen)
	Buttons.append(Pistachio) #Pistachio

	return Buttons
#---------------------------------------------------------------------------------------------------------------------

def Draw_Cone(Screen):
	Cone = pygame.image.load("cone.jpg")
	Screen.blit(Cone, (150,300))

#---------------------------------------------------------------------------------------------------------------------

def Draw_BackButton(Screen):
	BackButton = Button(0,550,200,50,[0,0,0],Screen) ##
	BackButton.Do()

#---------------------------------------------------------------------------------------------------------------------

def Draw_DoneButton(Screen):
	global DoneButton
	DoneButton = Button(400,550,200,50,[0,0,0],Screen)
	DoneButton.Do()

#---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
	pygame.init()
	Screen = pygame.display.set_mode((600, 600))
	Screen.fill((255,255,255))
	DrawLayout(Screen)
	ClickedyClick = 0
	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos
			if ClickedyClick == 0:
				if Lemon.Rectangle.collidepoint(x, y):
					Yellow = pygame.image.load("Lemon.jpeg")
					Screen.blit(Yellow,(275,245))
					ClickedyClick = 1
				elif Chocolate.Rectangle.collidepoint(x, y):
					Chocolate = pygame.image.load("Chocolate.jpeg")
					Screen.blit(Chocolate,(275,245))
					ClickedyClick = 1
				elif Vanilla.Rectangle.collidepoint(x, y):
					Vanilla = pygame.image.load("Vanilla.jpeg")
					Screen.blit(Vanilla,(275,245))
					ClickedyClick = 1
				elif Strawberry.Rectangle.collidepoint(x, y):
					Strawberry = pygame.image.load("Strawberry.jpeg")
					Screen.blit(Strawberry,(275,245))
					ClickedyClick = 1
				elif Pistachio.Rectangle.collidepoint(x, y):
					Pistachio = pygame.image.load("Pistachio.jpeg")
					Screen.blit(Pistachio,(275,245))
					ClickedyClick = 1

			elif ClickedyClick == 1:
				if Lemon.Rectangle.collidepoint(x, y):
					Yellow = pygame.image.load("Lemon.jpeg")
					Screen.blit(Yellow,(275,245-60))
					ClickedyClick = 2
				elif Chocolate.Rectangle.collidepoint(x, y):
					Chocolate = pygame.image.load("Chocolate.jpeg")
					Screen.blit(Chocolate,(275,245-60))
					ClickedyClick = 2
				elif Vanilla.Rectangle.collidepoint(x, y):
					Vanilla = pygame.image.load("Vanilla.jpeg")
					Screen.blit(Vanilla,(275,245-60))
					ClickedyClick = 2
				elif Strawberry.Rectangle.collidepoint(x, y):
					Strawberry = pygame.image.load("Strawberry.jpeg")
					Screen.blit(Strawberry,(275,245-60))
					ClickedyClick = 2
				elif Pistachio.Rectangle.collidepoint(x, y):
					Pistachio = pygame.image.load("Pistachio.jpeg")
					Screen.blit(Pistachio,(275,245-60))
					ClickedyClick = 2

			elif ClickedyClick == 2:
				if Lemon.Rectangle.collidepoint(x, y):
					Yellow = pygame.image.load("Lemon.jpeg")
					Screen.blit(Yellow,(275,245-60-60))
					ClickedyClick = 3
				elif Chocolate.Rectangle.collidepoint(x, y):
					Chocolate = pygame.image.load("Chocolate.jpeg")
					Screen.blit(Chocolate,(275,245-60-60))
					ClickedyClick = 3
				elif Vanilla.Rectangle.collidepoint(x, y):
					Vanilla = pygame.image.load("Vanilla.jpeg")
					Screen.blit(Vanilla,(275,245-60-60))
					ClickedyClick = 3
				elif Strawberry.Rectangle.collidepoint(x, y):
					Strawberry = pygame.image.load("Strawberry.jpeg")
					Screen.blit(Strawberry,(275,245-60-60))
					ClickedyClick = 3
				elif Pistachio.Rectangle.collidepoint(x, y):
					Pistachio = pygame.image.load("Pistachio.jpeg")
					Screen.blit(Pistachio,(275,245-60-60))
					ClickedyClick = 3
			if DoneButton.Rectangle.collidepoint(x, y):
				break
	
		pygame.display.flip()
			

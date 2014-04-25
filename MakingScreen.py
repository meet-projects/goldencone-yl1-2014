import pygame
from Classes import *
from label import *

#---------------------------------------------------------------------------------------------------------------------

def ScreenIt(x,y,Screen,ClickedyClick):
	
	DrawLayout(Screen)
	if Lemon.Rectangle.collidepoint(x, y):
		Yellow = pygame.image.load("Lemon.jpeg")
		Screen.blit(Yellow,(275,245-60*ClickedyClick))
		ClickedyClick += 1
	elif Chocolate.Rectangle.collidepoint(x, y):
		Brown = pygame.image.load("Chocolate.jpeg")
		Screen.blit(Brown,(275,245-60*ClickedyClick))
		ClickedyClick += 1
	elif Vanilla.Rectangle.collidepoint(x, y):
		White = pygame.image.load("Vanilla.jpeg")
		Screen.blit(White,(275,245-60*ClickedyClick))
		ClickedyClick += 1
	elif Strawberry.Rectangle.collidepoint(x, y):
		Red = pygame.image.load("Strawberry.jpeg")
		Screen.blit(Red,(275,245-60*ClickedyClick))
		ClickedyClick += 1
	elif Pistachio.Rectangle.collidepoint(x, y):
		Green = pygame.image.load("Pistachio.jpeg")
		Screen.blit(Green,(275,245-60*ClickedyClick))
		ClickedyClick += 1
	return ClickedyClick

#---------------------------------------------------------------------------------------------------------------------

def DrawLayout(Screen): ##This draws the WHOLE page
	Draw_Layout_LeftSide(AddFlavorButtons(Screen))
	Draw_Cone(Screen)
	Draw_DoneButton(Screen)
	Label_DoneButton(Screen)
	
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
	DoneButton = Button(500,550,100,50,[0,0,0],Screen)
	DoneButton.Do()

#---------------------------------------------------------------------------------------------------------------------

def Label_DoneButton(Screen):
	TextAt(500,550,100,50,60,"Done",(255,255,255),(0,0,0), Screen)

#---------------------------------------------------------------------------------------------------------------------

#def Label_FlavourButtons(Screen):

#---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
	pygame.init()
	global Screen
	Screen = pygame.display.set_mode((600, 600))
	Screen.fill((255,255,255))
	global ClickedyClick
	ClickedyClick = 0
	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos
			ScreenIt(x, y)
			if DoneButton.Rectangle.collidepoint(x, y):
				break
		pygame.display.flip()

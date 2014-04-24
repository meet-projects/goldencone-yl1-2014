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

def DrawLayout(): ##This draws the WHOLE page
	Draw_Layout_LeftSide(AddFlavorButtons())
	Draw_Layout_RightSide(AddSizeButtons())
	Draw_Layout_UpSide(AddToppingsButtons())
	Draw_Cone()
	Draw_BackButton()
	Draw_DoneButton()
	
#---------------------------------------------------------------------------------------------------------------------

def Draw_Layout_LeftSide(Flavors):
	for i in Flavors:
		i.Do()

#---------------------------------------------------------------------------------------------------------------------

def Draw_Layout_RightSide(Sizes):
	for i in Sizes:
		i.Do()

#---------------------------------------------------------------------------------------------------------------------

def Draw_Layout_UpSide(Toppings):
	for i in Toppings:
		i.Do()

#---------------------------------------------------------------------------------------------------------------------

def AddFlavorButtons():
	Buttons = []
	Buttons.append(Button(0,100,50,50,[255,255,0], Screen)) #Lemon
	Buttons.append(Button(0,150+20,50,50,[102,51,0], Screen)) #Chocolate
	Buttons.append(Button(0,200+40,50,50,[255,255,204], Screen)) #Vanilla
	Buttons.append(Button(0,250+60,50,50,[255,102,102], Screen)) #Strawberry
	Buttons.append(Button(0,300+80,50,50,[153,255,153], Screen)) #Pistachio
	return Buttons
#---------------------------------------------------------------------------------------------------------------------

def AddSizeButtons():
	Buttons = []
	Buttons.append(Button(550,100,50,50,[102,51,0], Screen)) #Big
	Buttons.append(Button(550,150+20,50,50,[102,51,0], Screen)) #Medium
	Buttons.append(Button(550,200+40,50,50,[102,51,0], Screen)) #Small
	return Buttons

#---------------------------------------------------------------------------------------------------------------------

def AddToppingsButtons():
	Buttons = []
	Buttons.append(Button(60,0,50,50,[0,0,0], Screen)) #Sprinkles
	Buttons.append(Button(110+165,0,50,50,[0,0,0], Screen)) #Maple Syrup
	Buttons.append(Button(160+330,0,50,50,[0,0,0], Screen)) #Sugar Powder
	return Buttons

#---------------------------------------------------------------------------------------------------------------------

def Draw_Cone():
	Cone = pygame.image.load("cone.jpg")
	Screen.blit(Cone, (150,300))

#---------------------------------------------------------------------------------------------------------------------

def Draw_BackButton():
	BackButton = Button(0,550,200,50,[0,0,0],Screen)
	BackButton.Do()
	TextAt(0,550,200,50,40,"Back",(255,255,255))

#---------------------------------------------------------------------------------------------------------------------

def Draw_DoneButton():
	DoneButton = Button(400,550,200,50,[0,0,0],Screen)
	DoneButton.Do()

#---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
	pygame.init()
	Screen = pygame.display.set_mode((600, 600))
	Screen.fill((255,255,255))
	while True:
		ev = pygame.event.poll()
		pygame.display.flip()
		DrawLayout()

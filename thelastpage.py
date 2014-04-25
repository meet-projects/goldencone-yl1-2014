import pygame
import sys
import Classes
import label
import MakingScreen

def FinalPage(Screen, ClickedyClick):                                       #font     background
	label.TextAt(185,30,28,23,64,"Price: " + str(ClickedyClick*5)+" $",(0,0,102),(204,255,229),Screen)

	DoneButton = Classes.Button(380,530,300,90,[255,255,255],Screen)
	DoneButton.Do()

	DoneButton = Classes.Button(0,0,150,600,[255,255,255],Screen)
	DoneButton.Do()

if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600,600))
	main_screen.fill((255,253,253))
	# myfont = pygame.font.Font(None,40)
	ClickedyClick=2

	

	while True: 
		ev = pygame.event.poll()
		
		pygame.display.flip()
	



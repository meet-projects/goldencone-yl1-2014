import pygame
import sys
import Classes
import label
import MakingScreen


if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600,600))
	main_screen.fill((255,253,253))
	# myfont = pygame.font.Font(None,40)
	ClickedyClick=2

	label.TextAt(169,57,28,23,64,"Price: " + str(ClickedyClick*5)+" $",(25,25,255),(51,153,255),main_screen)

	DoneButton = Classes.Button(380,530,220,90,[255,255,255],main_screen)
	DoneButton.Do()

	DoneButton = Classes.Button(0,0,90,600,[255,255,255],main_screen)
	DoneButton.Do()

	while True: 
		ev = pygame.event.poll()
		
		pygame.display.flip()
	



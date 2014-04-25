import Classes
import label
import MakingScreen
import pygame
import main
import thelastpage

#--------------------------------------------------------------------------------------------

if __name__ == "__main__":
	pygame.init()
	global Button
	ClickedyClick = 0
	Screen = pygame.display.set_mode((600,600))
	Screen.fill((255,255,255))
	main.StartScreen(Screen)
	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos
			if main.Button.Rectangle.collidepoint(x, y):
				main.WhiteOut(Screen)
			ClickedyClick = MakingScreen.ScreenIt(x, y, Screen,ClickedyClick)
			if MakingScreen.DoneButton.Rectangle.collidepoint(x, y):
				thelastpage.FinalPage(Screen,ClickedyClick)
		pygame.display.flip()

#--------------------------------------------------------------------------------------------
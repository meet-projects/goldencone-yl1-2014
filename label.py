import pygame

if __name__=="__main__":
	pygame.init()
	label_rec = pygame.Rect(225, 225 ,200, 100)
	orderlabel = pygame.font.Font("Make icecream", 70)
	
	while True:
		ev = pygame.event.poll()
		pygame.display.flip()
		

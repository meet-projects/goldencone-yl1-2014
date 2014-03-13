import pygame

if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600, 600))
	main_screen.fill((255, 255, 255))

	while True: 
		ev = pygame.event.poll()
		
		pygame.display.flip()
	

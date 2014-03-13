import pygame
 
if __name__=="__main__":
	pygame.init()
    	screen_size = 600,600
    	main_screen = pygame.display.set_mode((600, 600))
	button_rec = pygame.Rect(100, 100, 80,40)	
	main_screen.fill((255,255,255))
    	square = pygame.Surface([80,40])

    	while True:
      	  ev = pygame.event.poll()
      	  if ev.type == pygame.QUIT:
            sys.exit()
      	  if ev.type == pygame.MOUSEBUTTONDOWN:
       	  x , y = ev.pos
       	  if button_rec.collidepoint(x, y):
        	print "clicked"
      	 
      	  pygame.display.flip()

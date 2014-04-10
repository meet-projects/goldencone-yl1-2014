import pygame
import sys

if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600,600))
	main_screen.fill((255,153,153))
	button_rec = pygame.Rect((180,120,250,100))
	button_sq = pygame.Surface([250,100])
	button_sq.fill((153,0,76))
	main_screen.blit(button_sq,button_rec)

	y=5
	x = raw_input ("how many?")
	if x==1:
		y=5
	elif x==2:
		y=y*2
	elif x==3:
		y=y*3
	elif x==4:
		y=y*4
	else:
		 print "you can't have over five flavores"
	

	label_rec = pygame.Rect(190,150,200,50)
	orderlabel = pygame.font.Font(None,45)
	label = orderlabel.render("price: "+str(y),1,  (255,255,255),(204,0,102))
	main_screen.blit(label,label_rec)


	while True: 
		ev = pygame.event.poll()
		
		pygame.display.flip()
	



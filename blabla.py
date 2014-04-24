import pygame
import buttonclass
import sys



#def TextAt(start_x, start_y, length_x, length_y, FontSize, Context, FontColor, BackgroundColor):
	#main_screen = pygame.display.set_mode((600, 600))
	#label_rec = pygame.Rect(start_x, start_y ,length_x, length_y)
	#Surface = pygame.Surface([length_x, length_y])
	#orderlabel = pygame.font.Font(None,FontSize)
	#label = orderlabel.render(Context, 1, FontColor, BackgroundColor)
	#main_screen.blit(label, label_rec)


if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600,600))
	main_screen.fill((255,153,153))

						
	myfont = pygame.font.SysFont("times new roman",40)
	label = myfont.render("price",1,(200, 28, 150))
	main_screen.blit(label, (5,20))
	
							
	button1 = buttonclass.button(12,50,78,45)
	button1.draw(main_screen)
	button1.button_su.fill((120, 57, 139))	
	myfont = pygame.font.sysfont("times new roman",40)
	label = myfont.render("choclate",1,(200, 28, 150))


	while True: 
		ev = pygame.event.poll()
		
		pygame.display.flip()





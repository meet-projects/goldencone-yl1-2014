import pygame
import sys
import buttonclass


def TextAt(start_x, start_y, length_x, length_y, FontSize, Context, FontColor, BackgroundColor):
	main_screen = pygame.display.set_mode((600, 600))
	label_rec = pygame.Rect(start_x, start_y ,length_x, length_y)
	Surface = pygame.Surface([length_x, length_y])
	orderlabel = pygame.font.Font(None,FontSize)
	label = orderlabel.render(Context, 1, FontColor, BackgroundColor)
	main_screen.blit(label, label_rec)


if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600,600))
	main_screen.fill((255,153,153))
	myfont = pygame.font.sys("times new roman",40)
	label = myfont.render("price",1,(200, 28, 150)

	main_screen.blit(label,(5,20))

	button1 = buttonclass.button(12,50,78,45)
	button1.draw(main_screen)
	button1.button_su.fill((120, 57, 139))
	myfont = pygame.font.sysfont("times new roman",40)
	label = myfont.render("choclate",1,(200, 28, 150)







	#"""button_rec = pygame.Rect((180,120,250,100))
	#button_sq = pygame.Surface([250,100])
	#button_sq.fill((153,0,76))
	#main_screen.blit(button_sq,button_rec)"""


	# x=["lemon", strwberry, choclate, vanille, pistachio]

	# y=5

	# x = raw_input("how many?")

	# if x==0:
	# 	print y
	# elif x=1:
	# 	print y*2
	# elif x=2:
	# 	print y*3
	# elif x=3:
	# 	print y*4
	# elif x=4:
	# 	print y*5
	# else: 
	# 	print "I'm sorry! You can't have more than four flavores!"


	TextAt(149,134,28,23,24,"price:",(225,225,225),(0,0,0))

	# """label_rec = pygame.Rect(190,150,200,50)
	# orderlabel = pygame.font.Font(None,45)
	# label = orderlabel.render("price: "+str(y),1,  (255,255,255),(204,0,102))
	# main_screen.blit(label,label_rec)"""


	while True: 
		ev = pygame.event.poll()
		
		pygame.display.flip()
	



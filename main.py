import pygame
import Classes 
import label
import sys

if __name__=="__main__":
    pygame.init()
    screen_size = 600,600
    main_screen = pygame.display.set_mode((600, 600))
   # button_rec = pygame.Rect(100, 100, 80,40)   
    main_screen.fill((255,255,255))
    
    #square = pygame.Surface([80,40])
    #main_screen.blit(square , button_rec) 

    Ice = pygame.image.load("th.jpeg")
    main_screen.blit(Ice,(115,32))

    Button = Classes.Button(120, 165 ,400, 100, [255,135,133],main_screen)
    Button.Do()
    

    while True:
        ev = pygame.event.poll()
        
        label.TextAt(140,185,200,100,70,"Make Ice Cream",(255,255,255),(255,102,102), main_screen)
        if ev.type == pygame.QUIT:
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x , y = ev.pos
            if Button.Rectangle.collidepoint(x, y):
                
                print "clicked"
        pygame.display.flip()
         

        
#def TextAt(start_x, start_y, length_x, length_y, FontSize, Context, FontColor, BackgroundColor, main_screen):
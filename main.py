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


    Button = Classes.Button(150, 225 ,350, 100, [237,133,69],main_screen)
    Button.Do()
    
     

    while True:
        ev = pygame.event.poll()
        
        label.TextAt(150,225,200,100,70,"Make IceCream",(255,255,255),(237,133,69), main_screen)
        if ev.type == pygame.QUIT:
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            x , y = ev.pos
            if Button.Rectangle.collidepoint(x, y):
                
                print "clicked"
        pygame.display.flip()
         

        

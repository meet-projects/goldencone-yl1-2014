import pygame
import Classes 
import label

if __name__=="__main__":
    pygame.init()
    screen_size = 600,600
    main_screen = pygame.display.set_mode((600, 600))
   # button_rec = pygame.Rect(100, 100, 80,40)   
    main_screen.fill((255,255,255))
    
    #square = pygame.Surface([80,40])
    #main_screen.blit(square , button_rec) 


    Button = Classes.Button(225, 225 ,350, 100, [0,0,255],main_screen)
    Button.Do()
    
     

while True:
    ev = pygame.event.poll()
    pygame.display.flip()
    label.TextAt(225,225,200,100,70,"Make IceCream",(0,255,0),(255,255,255))
    if ev.type == pygame.QUIT:
        sys.exit()
    if ev.type == pygame.MOUSEBUTTONDOWN:
        x , y = ev.pos
        if Button.Rectangle.collidepoint(x, y):
            
            print "clicked"
         

        

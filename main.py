import pygame
import Classes 
import label
import sys
import MakingScreen


#--------------------------------------------------------------------------------------

def StartScreen(Screen):
    global Button
    Ice = pygame.image.load("th.jpeg")
    Screen.blit(Ice,(115,32))

    Button = Classes.Button(120, 165 ,400, 100, [255,135,133],Screen)
    Button.Do()
    label.TextAt(140,185,200,100,70,"Make Ice Cream",(255,255,255),(255,102,102), Screen)

#--------------------------------------------------------------------------------------

def WhiteOut(Screen):
    Clear = Classes.Button(0,0,600,600,[255,255,255],Screen)
    Clear.Do()

#--------------------------------------------------------------------------------------




# if __name__=="__main__":
# #     pygame.init()
# #     screen_size = 600,600
# #     main_screen = pygame.display.set_mode((600, 600))   
# #     main_screen.fill((255,255,255))
# #     Button = Classes.Button(150, 225 ,350, 100, [237,133,69],main_screen)
# #     Button.Do()

# #     while True:
# #         ev = pygame.event.poll()
# #         label.TextAt(150,225,200,100,70,"Make IceCream",(255,255,255),(237,133,69), main_screen)
# #         if ev.type == pygame.QUIT:
# #             sys.exit()
# #         if ev.type == pygame.MOUSEBUTTONDOWN:
# #             x , y = ev.pos
# #             if Button.Rectangle.collidepoint(x, y):
#     Ice = pygame.image.load("th.jpeg")
#     main_screen.blit(Ice,(115,32))

#     Button = Classes.Button(120, 165 ,400, 100, [255,135,133],main_screen)
#     Button.Do()
    

#     while True:
#         ev = pygame.event.poll()
        
#         if ev.type == pygame.QUIT:
#             sys.exit()
#         if ev.type == pygame.MOUSEBUTTONDOWN:
#             x , y = ev.pos
#             if Button.Rectangle.collidepoint(x, y):
                
#                 print "clicked"
# #         pygame.display.flip()
         

        
# #def TextAt(start_x, start_y, length_x, length_y, FontSize, Context, FontColor, BackgroundColor, main_screen):
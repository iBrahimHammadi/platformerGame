import pygame
pygame.init()

#Creating the window Screen
HEIGHT, WIDTH = 600, 800
Screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Platformer Game")

#Creating the main function
def main(window):

    #Creating the GameLoop
    run = True
    while run:

    #Creating the event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(Screen)
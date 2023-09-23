import pygame
import os
from os.path import join
pygame.init()

#Creating the window Screen
HEIGHT, WIDTH = 600, 800
Screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Platformer Game")

#Fucntion for creating the grid for the background 
def get_background(bg_image):
    image  = pygame.image.load(join('assets','Background',bg_image))
    tile = []
    x, y, width, height = image.get_rect()

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i*width), (j*height)
            tile.append(pos)
    return tile, image

#Function to draw the background
def draw(window,background,bg_image):
    for tile in background:
        Screen.blit(bg_image,tile)
    pygame.display.update()


#Creating the main function
def main(window):

    background, bg_image = get_background('Yellow.png')

    #Creating the GameLoop
    run = True
    while run:
        #Creating the event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(Screen,background,bg_image)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(Screen)
import pygame
import os
from os.path import join

pygame.init()

#Creating the window Screen
HEIGHT, WIDTH = 600, 800
Screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Platformer Game")

#Creating the player Class
class Player(pygame.sprite.Sprite):
    Color = (255, 0, 0)
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self,vel):
        self.x_vel = -vel

    def move_right(self, vel):
        self.x_vel = vel
    
    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)

    def draw(self, win):
        pygame.draw.rect(win,self.Color, self.rect)


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
def draw(Screen,background,bg_image,player):
    for tile in background:
        Screen.blit(bg_image,tile)
    player.draw(Screen )
    pygame.display.update()


#Creating the main function
def main(window):

    background, bg_image = get_background('Yellow.png')
    player = Player(100, 400, 40, 40)

    #Creating the GameLoop
    run = True
    while run:
        #Creating the event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(Screen,background,bg_image, player)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(Screen)
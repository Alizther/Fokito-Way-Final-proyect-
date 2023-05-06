import pygame

#incio del pygame
pygame.init()

#tamaño de pantalla
screen=pygame.display.set_mode((1000,600))

#Titulo, icono
pygame.display.set_caption ("Final Fantasy XXX")
icon = pygame.image.load('Icon.png')
pygame.display.set_icon(icon)

#Jugador?
PlayerSprite = pygame.image.load('Player.png')
PlayerX= 500
PlayerY=500
PlayerX_Change= 0
PlayerY_Change= 0
def player(x,y):
    screen.blit(PlayerSprite,(x,y))


#Bucle del juego
RunGame = True
while RunGame:
    screen.fill((0,50,150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RunGame= False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerX_Change = -0.2
            if event.key == pygame.K_RIGHT:
                PlayerX_Change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_Change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                PlayerY_Change = -0.2
            if event.key == pygame.K_DOWN:
                PlayerY_Change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                PlayerY_Change = 0

    PlayerX+= PlayerX_Change
    PlayerY+= PlayerY_Change
    player(PlayerX,PlayerY)
    pygame.display.update()
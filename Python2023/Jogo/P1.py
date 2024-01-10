import pygame

pygame.init()
x = 400
y = 300
velocidade = 10

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Jogo Do carro")


while True:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= velocidade
    elif comandos[pygame.K_DOWN]:
        y+= velocidade
    elif comandos[pygame.K_RIGHT]:
        x+= velocidade
    elif comandos[pygame.K_LEFT]:
        x-= velocidade

    janela.fill((0,0,0))

    pygame.draw.circle(janela,(255,0,0),(x,y),50)
    pygame.display.update()
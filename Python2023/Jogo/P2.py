import pygame

pygame.init()
x = 400
y = 300
velocidade = 10
fundo = pygame.image.load('Mapa.png')
carro = pygame.image.load('CarroAjustado.png')

janela = pygame.display.set_mode((1200,680))
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

    janela.blit(fundo,(0,0))

    janela.blit(carro,(x,y))
    pygame.display.update()
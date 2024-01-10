import pygame

def run(screen):
    pygame.init()
    pygame.display.set_caption("Pokemon")
    background = pygame.image.load('assets/combat.png')

    running = True
    while running:
        screen.blit(background, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


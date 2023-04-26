import pygame

# font = None
def initiate_screen(SCREEN_WIDTH, SCREEN_HEIGHT, caption):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(caption)
    global font 
    # font = pygame.font.Font('freesansbold.ttf', 21)
    clock = pygame.time.Clock()

    return screen, clock

def plot(SCREEN_WIDTH, SCREEN_HEIGHT, screen, clock, w, arr, j, alt_j=None, elapsed=0):
    n=len(arr)
    x = w
    for d in range(n):

        # text = font.render(f"Time Elapsed: {elapsed}", True, (240,240,240))
        # screen.blit(text, (0,0))

        y = SCREEN_HEIGHT-arr[d]
        pygame.draw.rect(screen, (0,0,0), (x,0,w,SCREEN_HEIGHT))
        pygame.draw.rect(screen, (255,255,255), (x,y,w,arr[d]))
        target_x = (((j*2)+1) * w)
        pygame.draw.rect(screen, (0,255,0), (target_x, SCREEN_HEIGHT-arr[j], w, arr[j]))

        if(alt_j is not None):
            target_x_alt_j = (((alt_j*2)+1) * w)
            pygame.draw.rect(screen, (0,255,0), (target_x_alt_j, SCREEN_HEIGHT-arr[alt_j], w, arr[alt_j]))
        pygame.display.update()
        x = x + (2*w)
    clock.tick(60)


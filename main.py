from curses import window
import os
import pygame
import pygame.locals
import wordle

k_keys = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g,
         pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n,
         pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u,
         pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, pygame.K_BACKSPACE, pygame.K_RETURN
         ]
ch = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ-='


def drawRect(window, words, colors):
    default_font = pygame.font.SysFont(None, 80)
    h, w = 60, 60
    for i in range(6):
        for j in range(5):
            x = 110 + 80 * j
            y = 50 + 80 * i
            pygame.draw.rect(window, colors[i][j], [x, y, h, w], 0)
            text_surface = default_font.render(words[i][j], True, (0, 0, 0))
            window.blit(text_surface, (x + 10, y + 10))
    pygame.display.flip()
    return window


def getKey(key):
    for i in range(28):
        if key == k_keys[i]:
            return ch[i]
    return '.'


def printMsg(window, msg):
    default_font = pygame.font.SysFont(None, 100)
    text_surface = default_font.render(msg, True, (0, 0, 0))
    window.blit(text_surface, (110, 600))
    pygame.display.flip()
    return window


def quit():
    pygame.quit()
    os._exit()


def main():
    pygame.init()
    window = pygame.display.set_mode((600, 800))
    pygame.display.set_caption('Wordle')
    window.fill((255, 255, 255))
    my_wordle = wordle.Wordle()
    window = drawRect(window, my_wordle.words, my_wordle.colors)
    pygame.display.flip()
    i = 0
    while i < 6:
        j = 0
        while j <= 5:
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.locals.QUIT:
                        quit()
                    if event.type == pygame.locals.KEYDOWN:
                        window.fill((255, 255, 255))
                        key = getKey(event.key)
                        j = my_wordle.enter(i, j, key)
                        window = drawRect(window, my_wordle.words, my_wordle.colors)
                        run = False
                        break
            
        check_code =  my_wordle.check(i)
        window = drawRect(window, my_wordle.words, my_wordle.colors)

        if check_code == 0:
            i += 1
        elif check_code == 1:
            window = printMsg(window, 'Success')
            break
        elif check_code == -1:
            window = printMsg(window, 'Not Exist')

    if i == 6:
        window = printMsg(window, 'Die')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                quit()


if __name__ == '__main__':
    main()
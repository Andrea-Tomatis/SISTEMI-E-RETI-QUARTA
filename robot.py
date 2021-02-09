'''
Stanza Rettangolare Piastrellata:
 _______
|_|_|_|_|
|_|_|_|_| 
|_|_|_|_|
|_|_|_|_|

il robot si muove in questa stanza
la stanza contiene degli ostacoli
per rappresentare la situazione si puo' usare una matrice
le piastrelle possono trovarsi in 2 stati: libere o occupate

problema: se il robot si trova in un punto xy e vuole andare in un punto x'y' trovare il 
          percorso piu' breve

1- numeriamo le celle libere da 1 a n
2- il robot si muove in 4 direzioni
3- generare un dizionario che per ogni cella libera identifichi i possibili movimenti del robot
               -> dizionario delle prossimita'

Author: Andrea Tomatis
'''

import pygame,sys

def main():

    pavimento = [[0,0,0,-1,-1],
                [-1,0,0,0,-1],
                [0,0,-1,-1,-1],
                [0,0,-1,0,0],
                [-1,0,0,0,0],
                [-1,-1,-1,0,0]]


    #numerare celle libere
    cnt = 0
    for x, element in enumerate(pavimento):
        for y in range(len(element)):
            if pavimento[x][y] != -1:
                pavimento[x][y] = cnt
                cnt += 1
    

    #generare il dizionario
    dizionario_prossimita = {}

    lista  = [(0,1),(0,-1),(1,0),(-1,0)]

    for i, element in enumerate(pavimento):
        for j in range(len(element)):
            if pavimento[i][j] != -1:
                prossimi = []
                for tupla in lista:
                    try:
                        if(pavimento[i+tupla[0]][j+tupla[1]] != -1):
                            prossimi.append([i+tupla[0],j+tupla[1]])
                    except IndexError:
                        pass
                dizionario_prossimita[pavimento[i][j]] = prossimi


    for key, value in dizionario_prossimita.items():
        print(key,value)


    ROSSO = (255,0,0)
    NERO = (0,0,0)
    BIANCO = (255,255,255)
    global screen
    pygame.init()
    screen = pygame.display.set_mode((5*50,6*50))
    screen.fill(NERO)
    #disegna stanza
    dimensione = 50
    while True:
        for x in range(0,len(pavimento)*dimensione, dimensione):
            for y in range(0, len(pavimento[x//50])*dimensione, dimensione):
                if(pavimento[x//50][y//50] == -1):
                    ostacolo = pygame.Rect(x,y,dimensione,dimensione)
                    pygame.draw.rect(screen,ROSSO,ostacolo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    main()
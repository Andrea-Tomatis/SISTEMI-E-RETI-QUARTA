'''
Verifica 25/02/2021

Testo:
considerate stringhe lunghe al massimo 12 caratteri
i caratteri ammessi sono le cifre da “0” a “9”, il carattere spazio (“ “) e le lettere minuscole dell’alfabeto italiano da “a” a “z”
ognuno di questi caratteri può essere codificato su 5 bit.

Create un programma in Python3 che:

1) crei un dizionario che abbia come chiave ciascuno dei caratteri di cui sopra e come valori le liste di bit (numeri interi 0 oppure 1) corrispondenti alla codifica binaria su 5 bit. La codifica può essere inventata da voi
es: {“b” : [1,0,1,0,1],.............}

2) chieda all’utente una stringa composta secondo le ipotesi di cui sopra.

3) converta la stringa inserita dall’utente in una lista di liste effettuando la conversione da ogni carattere alla corrispondente lista di bit

4) disegni il qr code, ovvero rappresenti la lista di lista su uno screen di Pygame, usando celle nere per i bit a 1 e celle bianche per i bit a 0

5) salvi la lista di liste di cui al punto 3 all’interno di un file .csv.


BONUS:
l’utente può decidere se inserire una stringa oppure il nome di un file csv: nel secondo caso il programma apre il file .csv e rappresenta il qr code su uno screen di Pygame.


Author: Andrea Tomatis
class: 4^aRob
'''

#importa le librerie necessarie e inizializza pygame
import pygame, sys
pygame.init()

##dichiarazione delle costanti
DIM_MAX_STR = 12 #dimensione massima di una stringa
NERO = (0,0,0)  #rgb del colore nero
BIANCO = (255,255,255)  #rgb del colore bianco


#restituisce un dizionario che contenga i caratteri ammessi e la loro conversione binaria
def caricaCaratteriAmmessi():
    #lista di supporto
    lista1 = []

    #aggiunge i numeri da 0 a 9
    for i in range(0,9):
        lista1.append(str(i))

    #aggiunge lo spazio alla lista
    lista1.append(' ')

    #aggiunge i caratteri dalla a alla z alla lista
    for i in range(ord('a'),ord('z') + 1):
        if chr(i) != 'j' and chr(i) != 'w' and chr(i) != 'k' and chr(i) != 'y' and chr(i) != 'x':
            lista1.append(chr(i))
    
    #crea il dizionario contenente come chiave i caratteri e come valori
    #una stringa contenente la conversione binaria
    dictionary = {lista1[i] : bin(i)[2:].zfill(5) for i in range(len(lista1))}

    #trasforma ogni chiave del dizionario in una lista di caratteri
    for key, value in dictionary.items():
        valori = []
        for car in value:
            valori.append(car)
        dictionary[key] = valori
    
    return dictionary


#restituisce false se sono presenti caratteri non ammessi nella stringa
def isInCaratteri(stringa_input, caratteri_ammessi):
    for car in stringa_input:
        if car not in caratteri_ammessi:
            return False
    return True


#converte ogni carattere della stringa in una lista di liste
def convertiStringa(stringa_input, caratteri_ammessi):
    new_list = []
    for car in stringa_input:
        new_list.append(caratteri_ammessi[car])
    return new_list


#salva su file la una lista di liste
def salvaSuFile(stringa, nomefile='strings.csv'):
    with open(nomefile, 'w') as fp:
        for element in stringa:
            fp.write(','.join(str(i) for i in element) + '\n')


#controlla se e' il caso di terminare la finestra di pygame
def controllaChiusura():
    #scorre tutti gli eventi dello schermo alla richerca dell'evento quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


#stampa a schermo il qrcode
def stampaQrCode(stringa_convertita):
    #variabile contente la finestra di pygame
    global screen
    
    #fattore moltiplicativo per dimensionare la finestra di pygame
    dimensione = 50#
    
    #la larghezza e l'altezza dello schermo sono determinate dalla lista di liste
    width = len(stringa_convertita[0]) * dimensione
    height = len(stringa_convertita) * dimensione

    #istanzia lo schermo
    screen = pygame.display.set_mode((width,height))

    #finche' la finestra e' aperta stampa la lista di liste
    while True:
        for x in range(0, width, dimensione):
            for y in range(0, height, dimensione):
                #se la matrice contiene 1 allora sullo schermo appare un quadrato bianco
                if stringa_convertita[y//dimensione][x//dimensione] == '1':
                    rect = pygame.Rect(x, y, dimensione, dimensione)
                    pygame.draw.rect(screen, BIANCO, rect)
        
        #controlla se e' il caso di terminare la finestra
        controllaChiusura()
        #aggiorna la schermata 
        pygame.display.update()


#carica una lista di liste dal fine dato in input alla funzione
def caricaListaDaFile(stringa_input):
    new_lista = []
    with open(stringa_input, 'r') as fp:
        for line in fp:
            #divide la linea del csv per il carattere ,
            split_line = line.split(',')
            
            #split_list contiene una riga della matrice
            split_list = []
            for element in split_line:
                split_list.append(element)
            
            #le righe vengono aggiunte una ad una alla lista di liste
            new_lista.append(split_list)
    return new_lista


def main():

    #crea un dizionario contenente i caratteri ammessi e le 
    #rispettive conversioni in binario
    caratteri_ammessi = caricaCaratteriAmmessi()   
    
    #assume una stringa in input
    stringa_input = input('inserisci una stringa (max 12 caratteri): ')

    #se l'input e' il nome di un file genera la lista di liste leggendola da file
    if stringa_input[-4:] == '.csv':
        stringa_convertita = caricaListaDaFile(stringa_input)
    else:
        #se la stringa non rispetta le condizioni dell'input il programma crasha
        #e viene sollevata l'eccezione 'stringa non valida'
        if len(stringa_input) > DIM_MAX_STR or not isInCaratteri(stringa_input, caratteri_ammessi):
            raise Exception('stringa non valida')
        
        #converte la stringa in input in una lista di liste per poterla stampare come un qrcode
        stringa_convertita = convertiStringa(stringa_input, caratteri_ammessi)
        #salva su un file la lista di liste
        salvaSuFile(stringa_convertita)

    #stampa su una finestra di pygame il qrcode
    stampaQrCode(stringa_convertita)
    

#avvia il programma
if __name__ == "__main__":
    main()
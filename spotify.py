def readLista():
    file = open("spotify.csv","r")
    playlist = []

    for line in file:
        elements = line.split(",")
        canzone = {"id" : elements[0], "title" : elements[1], "author" : elements[2][:-1]}
        playlist.append(canzone)
    file.close()
    return playlist    

def readDict():
    file = open("spotify.csv","r")
    playlist = {}

    for line in file:
        elements = line.split(",")
        canzone = {"title" : elements[1], "author" : elements[2][:-1]}
        playlist[elements[0]] = canzone
    file.close()
    return playlist



playlist = readLista()
playlist2 = readDict()

for i,element in enumerate(playlist2):
    print(f"{i}: {playlist2[element]}")

for element in playlist:
    print(element)


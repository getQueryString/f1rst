# by Fin - learned from TMT

print("Eins")
print()

breite = "blibla\nwas anderes"
char = 'a'
liste = [[0, 1, 2], [4, 5, 6], [7, 8, 9]]
breite = char + breite[1:]
print(liste[0])
print(liste[1])
print(liste[2])

print()
print("Zwei")
print()

breite1 = 42
y = 2

if breite1 < 5000:
    print(breite1)
elif breite1 > 5000:
    print("zu groß")
else:
    print("5000")

if y == 2:
    print("lul")

print()
print("Drei")
print()

liste1 = [1, 2, 3, 4, 42, 1337]

for x in liste1:
    print(x)

print()
print("Vier")
print()

myVar = list(range(0, 10))    # min, max, step
print(myVar)

print()
print("Fünf")
print()

def meineFunktion(liste1):
    i = 0
    x = liste1[i]
    while x < 2000:
        print(x)
        i += 1
        if i >= len(liste1):
            break
        x = liste1[i]

def generiereListe():
    liste1 = [1, 2, 3, 4, 42, 1337]
    return liste1

listenVariante = generiereListe()
meineFunktion(listenVariante)
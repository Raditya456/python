import random

diceface = random.randint(1,6)

while True:
    angka = int(input("Masukan angka 1 angka di dadu :"))

    if angka != diceface:
        print("Hmm salah")
        continue

    else:
        print("Yak betul")
        

    another = input("Coba lagi? (y/n) :")
    if another == 'y':
        continue
    else:
        break





import random

angka = random.randint(1,25)

while True:

    tebak= int(input("Coba tebak 1-25 :"))

    if tebak > angka:
        print("angka terlalu besar")
        continue
    elif tebak < angka:
        print("angka terlalu kecil")
        continue
    else:
        print("BETUL!!!")
        break

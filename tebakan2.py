import random

angka = random.randint(1,50)


while True:

    tebak = int(input("Coba masukin angka 1-50 :"))
    
    if tebak > angka:
        print("Kegedean")
        continue
    elif tebak < angka:
        print("Kekecilan")
        continue
    else:
        print("betul")
        break

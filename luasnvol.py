def luassegi3(alas, tinggi):
    print((alas * tinggi) / 2)
def luasling(radius):
    print("Hasilnya adalah :{}".format(3.14 * radius * radius))#harus dikasi format biar muncul
    return(3.14 * radius * radius)

alas = int(input("Masukan besar alas :"))
tinggi = int(input("Masukan besar tinggi :"))
luassegi3(alas, tinggi)


radius = int(input("Masukan besar r :"))

luasling(radius)

def voltabung(luasling,panjang):
    print(luasling * panjang)
    return(luasling * panjang)

panjang = int(input("Masukan panjang tabung :"))

voltabung(luasling(radius), panjang)

def volbola(luasling):
    print("Vol Bola sebagai berikut")
    print((4/3) * luasling * radius)

volbola(luasling(radius))

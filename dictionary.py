def perkenalan(dictionary):
    for key,val in dictionary.items():
        print("Saya {} dan saya dari kelas {}".format(key,val))

murid = {}

while True:

    nama = input("Masukan nama anda :")
    kelas = input("Masukan kelas anda :")

    murid[nama] = kelas

    lagi = input("Tambah orang (y/n)? :")
    if lagi == 'y':
        continue
    else:
        break

print(murid)
perkenalan(murid)
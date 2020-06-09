def classed(dictionary):
    for key,val in dictionary.items():
        print('Nama: {} Grade: {}').format(key,val)


grades = {}   #dipakai untuk memanggil fungsi

while True:
    nama = input("Masukan nama anda :")
    nilai = int(input("Masukan nilai anda :"))

    if nilai >= 90:
        print("Grade anda : A")

    elif nilai >=80 and nilai < 90:
        print("Grade anda : B")

    elif nilai >=70  and nilai <80:
        print("Grade anda : C")

    else:
        print("Grade anda : F")
    
    another = input("Ada tambahan orang? (y/n) :")

    if another == 'y':
        continue
    else:
        break

classed(grades)
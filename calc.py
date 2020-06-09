
operasi_mat = input('Masukan operasi mat :') 

angka1 = int(input('Masukan angka 1 :'))
angka2 = int(input('Masukan angka 2 :'))

equals = 0

if operasi_mat == '+':
    equals = angka1 + angka2
elif operasi_mat == '-':
    equals = angka1 - angka2
elif operasi_mat == '*':
    equals = angka1 * angka2
elif operasi_mat == '/':
    if angka2 == 0:
        equals = "Mang bisa dibagi 0"
    else:
        equals = angka1 / angka2
else:
    equals = "Tunggu update terbaru software"


print("Hasilnya adalah : {}".format(equals))


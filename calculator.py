# COMMENT / Penjelasan kode diawali dengan tanda '#' --> Bagian ini ga bakal dijalanin sama python.

# Minta user input operasi matematika
operasi = input("Masukkan operasi matematika : ")

# User masukin 2 angka
angka_1 = int(input("Masukkan angka 1 : "))
angka_2 = int(input("Masukkan angka 2 : "))

# Hasil by default bentuknya integer tapi bisa diganti ke pesan string jg.
hasil = 0


if operasi == '+':
    hasil = angka_1 + angka_2
elif operasi == '-':
    hasil = angka_1 - angka_2
elif operasi == '*':
    hasil = angka_1 * angka_2
elif operasi == '/':
    # Pake nested if (If didalam elif atau if didalam if)
    if angka_2 == 0:
        # Kalo angka kedua 0, nilai hasil kita masukin string (di python bisa gitu)
        hasil = "Tidak bisa membagi dengan 0"
    else:
        hasil = angka_1 / angka_2
else:
    # Kalo user masukin input selain +,-,*,/
    hasil = "Anda salah masukin operasi."

print("Hasilnya adalah : {}".format(hasil))
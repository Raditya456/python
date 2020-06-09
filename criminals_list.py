import time

# --> merupakan comment/ penjelasan kode. Comment gabakal dibaca/dijalankan sama python.
# Guna comment cuman buat membantu programmer dalam membaca kode nya. --> Di biasa-in.
criminals = []

def add_criminal_to_list(name, age, crime):
    criminal_data = {
        "Fullname" : name,
        "Age" : age,
        "Crime" : crime
    }
    criminals.append(criminal_data)

tambah_berapa_kriminal = int(input("Mau tambahkan berapa kriminal? "))
counter = 1
while counter <= tambah_berapa_kriminal:
    nama_kriminal = input("Masukkan nama kriminal : ")
    umur_kriminal = int(input("Masukkan umur kriminal : "))
    kejahatan_kriminal = input("Masukkan kejahatan yang dilakukan kriminal : ")

    # Pake fungsi yg kita tulis diatas buat nambahin dictionary criminals ke list criminal.
    add_criminal_to_list(nama_kriminal, umur_kriminal, kejahatan_kriminal)
    
    # Kurangin counter biar ga terjadi infinite loop dan suatu saat looping berhenti
    counter = counter  + 1
    print()


my_password = ''
print("GUESS THE FBI PASSWORD : ")

# Agar orang bisa lihat daftar penjahat yang kita bikin, mereka harus tahu password.
while my_password != '191919':
    my_password = input ('Password? ')

print ('--------------------')
print ('FBI MOST WANTED LIST')
print ('--------------------')
print()
time.sleep(1)

print("Loading data...")
time.sleep(1)

print()
print (len(criminals) , ' IDENTIFIED.')
print()

time.sleep(1)
print("DAFTAR KRIMINAL FBI")

# Pake for loop buat nge print semua criminals.
# 'criminal' = variabel bebas yg baru kita bikin di for loop --> isinya setiap elemen di dalam list (berupa dictionary.)
for criminal in criminals:
    print("Nama : {}, Umur : {}, Kejahatan : {}".format(criminal["Fullname"], criminal["Age"], criminal["Crime"]))
    #                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
    #                                            ^ ini cuman buat lu akses value dari setiap key di dictionary criminal.

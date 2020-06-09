# SCOPE
# GLOBAL DAN LOKAL 

# input0 = 'andi'

# print(input0)
# def ask_name():
#     global input0 # --> input0 yg variabel global
#     input0 = input("Enter name : ")

# ask_name()
# print(input0)


print("SCOPE DI PYTHON")
print("Prioritas --> Bagaimana python itu me-refrence (merujuk) ke variabel.")
print("Global scope dan Local scope")

print("KONSEP 1 (GLOBAL SCOPE) : Variabel (objek) yang di bikin (di-definisikan) di luar fungsi itu bisa diakses di dalam fungsi.")
print("KONSEP 2 (LOCAL SCOPE): Varibel (objek) yang dibikin (di-definisikan) di dalam fungsi itu gabisa diakses diluar fungsi dengan cara biasa")

print()

'''
random_variable = "Apa aja" # GLOBAL VARIABLE

def random_function():
    return random_variable

def fungsi_random():
    variabel_random = "Whatever" #  LOCAL VARIABLE  
    return variabel_random


variabel_random = fungsi_random()
'''



# DEMONSTRASI 
'''
nama_orang = input("Masukkan nama anda : ")
print(nama_orang)

def my_function():
    nama_orang = input("Masukkan nama anda lagi : ") # --> variabel lokal 
    print("Nama orang hanya bisa dipake di dalam function ini.")

my_function()
print(nama_orang)
'''

jumlah_baju = 10
print(jumlah_baju)

def tambah_baju():
    global jumlah_baju # --> buat python merujuk variabel jumlah_baju yang global (yg diatas)
    jumlah_baju = 20
    return jumlah_baju

tambah_baju()
print(jumlah_baju)




# f(x) = 3x  + 5 -- > fungsi mat

'''
def fungsi_kosong():
    pass # ga ngapa2 in
    return "apa aja" # ngasi tau python fungsinya menghasilkan apa, dan hasil dari fungsi ini bisa kita utak atik


def namaFungsi(parameter1):
    # Kode
    return 3 * parameter1 + 5

def greet_user(nama_orang):
    print("Hello {}".format(nama_orang))
    return "Hello {}".format(nama_orang)


user_input = input("Nama kamu siapa? ")
# Nge-call function --> print hasil keluaran dari function ini
print(greet_user(user_input))


# Function lebih ribet
# Function hitung luas lingkaran --> pi, jari-jari

def hitung_luas_lingkaran(jari_jari):
    pi = 3.14 # Float
    luas = int(pi * jari_jari * jari_jari) # Float * Integer --> Float
    return luas # Angka --> integer


jari = int(input("Jari-jari  : "))
luas_ling = hitung_luas_lingkaran(jari)
print("Luas lingkaran : {}".format(luas_ling))

luas_dobel = hitung_luas_lingkaran(jari) * 2
print("Luas dobel : {}".format(luas_dobel))
'''


def fungsi_no_parameter():
    return "Hello World"

print(fungsi_no_parameter())
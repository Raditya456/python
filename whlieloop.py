variabel = 0

while True:
    username = input("Masukan username :")
    password = input("Masukan password :")
    variabel += 1
    if variabel == 3:
        print("Mohon coba 5 menit lagi")
        break

    else:    
        if username == 'adit' and password == '1234':
            print("login berhasil")

        else:
            print("Password atau Username salah, coba ulang")
        continue
  




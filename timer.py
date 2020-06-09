import time
detik = int(input("Masukan detik :"))
menit = int(input("Masukan menit :"))
waktu = detik + menit*60
for x in range(waktu + 1):
    print(waktu - x)
    time.sleep(1)

print("tetot")



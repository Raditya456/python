def umur(orang_lahir, tahun_now):
    return(tahun_now - orang_lahir)

def umur_nanti(umur, nantinya):
    print("Umur anda {} tahun kedepan adalah :".format(nantinya), umur + nantinya)

nantinya = int(input("Masukan pertambahan tahun :"))
orang_lahir = int(input("Masukan tahun lahir anda :"))
tahun_now = 2020

    
umur_nanti(umur(orang_lahir, tahun_now), nantinya)



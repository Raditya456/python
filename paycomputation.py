#jam kerja
#gaji per jam
#bonus 1.5

def pay_computation(jam_kerja, gaji_per_jam):
    # kalo kerja > 40 jam --> kasi bonus yaitu gaji/jam nya yang extra itu x 1.5
    if jam_kerja > 40:
        bonus = (jam_kerja - 40) * gaji_per_jam * 1.5
        return 40 * gaji_per_jam + bonus
    else:
        return jam_kerja * gaji_per_jam

print(pay_computation(40, 100000)) # 40 jam kerja dan Rp 100.000/jam
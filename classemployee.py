class employee:

    def __init__(self, nama, bayaran, jabatan, harikerja):
        self.nama = nama
        self.bayaran = bayaran
        self.jabatan = jabatan
        self.harikerja = harikerja

    def datapekerja (self):
        print (f'Saya {self.nama}, posisi {self.jabatan} dengan gaji {self.bayaran} per hari dan dengan {self.harikerja} hari bekerja')
   
emp1 = employee('Utap', 250000, 'karyawan', 6)    

emp1.datapekerja()    
    
        
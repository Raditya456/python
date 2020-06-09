def classed(dictionary):
    for key,val in dictionary.items():
        print('{} : {}'.format(key,val))


students = []   #dipakai untuk memanggil fungsi

while True:
    student = {}
    
    nama = input("Masukan nama anda :")
    nilai = int(input("Masukan nilai anda :"))

    if nilai >= 90:
        grade_anda = 'A'

    elif nilai >=80 and nilai < 90:
        grade_anda = 'B'

    elif nilai >=70  and nilai <80:
        grade_anda = 'C'

    else:
        grade_anda = 'F'
        

    student['nama'] = nama
    student['nilai'] = nilai
    student['grade'] = grade_anda
    
    students.append(student)
    
    another = input("Ada tambahan orang? (y/n) :")

    if another == 'y':
        continue
    else:
        break

for element in students:
    classed(element)
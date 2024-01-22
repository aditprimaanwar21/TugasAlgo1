nilai = int (input("masukan nilai mahasiswa: "))
grade = "E"

if nilai > 85:
    grade = "4.00 \ndengan predikat A"
elif nilai >= 80:
    grade = "3.70 \ndengan predikat A-"
elif nilai >= 75:
    grade = "3.30 \ndengan predikat B+"
elif nilai >= 70:
    grade = "3.00 \ndengan predikat B"
elif nilai >= 65:
    grade = "2.70 \ndengan predikat B-"
elif nilai >= 60:
    grade = "2.30 \ndengan predikat C+"
elif nilai >= 55:
    grade = "2.00 \ndengan predikat C"
elif nilai >= 50:
    grade = "1.70 \ndengan predikat C-"
elif nilai >= 40:
    grade = "1.00 \ndengan predikat D"
else:
    grade = "0 \ndengan predikat E"

print("ipk mahasiswa adalah {}".format(grade))
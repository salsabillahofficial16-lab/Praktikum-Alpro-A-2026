def fizzbuzz_plus(n):
   for X in range(n + 1):
     if X % 3 == 0 and X % 5 == 0:
         print("fizzbuzz")
     elif X % 3 == 0:
         print("Fizz")
     elif X % 5 == 0:
         print("buzz")
     elif X % 7 == 0:
         print("seven")
   else:
    print("angka")

#nomor 3
def hitung_nilai(tugas,uts,uas):
    return (0.3 * tugas + 0.3 * uts + 0.4 * uas)
nilai = 99
if nilai >= 85:
    print("A")
elif nilai >=70:
    print("B")
elif nilai >= 55:
    print("C")
elif nilai >= 40:
    print("D")
elif nilai < 40:
    print("E")
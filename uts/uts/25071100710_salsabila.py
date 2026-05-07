DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]
# DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)]

# ======= bagian A ==========
# buat fungsi pertama dengan mmenggunakan for loop
def  tebak_angka(angka_rahasia, maks_percobaan):
   angka_rahasia = ()
   maks_percobaan = 7   

   angka_rahasia = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]
   for  j in range(maks_percobaan): 
     if maks_percobaan == 7:
        return False
    
        for i in range (7):
            if  tebak_angka > angka_rahasia:
                return ("terlalu besar")
            if tebak_angka < angka_rahasia:
                return("terlalu kecil")
            if tebak_angka == angka_rahasia:
                return("Benar!")
            elif tebak_angka != angka_rahasia:
               return False
        
#===buat fungsi  ke 2    
#jika berhasil maka hasilnya true
def hitung_skor(berhasil, sisa_percobaan):
   if  berhasil == True:
     skor = sisa_percobaan * 10
   else:
      return 0
   
#fungsi ke 3
def main_satu_ronde(nama, nomor_ronde):
   
   nama = []
   nomor_ronde = []
   DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)]
print("=== permainan tebak angka ===")
for i in range(7):
 tebak_angka = (int(input("masukkkan angka: ")))
 hitung_skor = (int(input("hitung skor : ")))

#bagian b membuat fungsi menampilkan riwayat
def tampilkan_riwayat(riwayat):
   riwayat = ()


#bagian c membuat 2 fungsi Leaderboard dengan Selection Sort

def selection_sort_riwayat(riwayat):
   pass

def tampilkan_leaderboard(riwayat):
   selection_sort_riwayat = []


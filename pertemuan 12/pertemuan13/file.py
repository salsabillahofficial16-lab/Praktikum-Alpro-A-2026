import time
f = open("contoh.txt", "rt")  
# hanya untuk membuka /membaca file
print (f.read()) 
f.close()

with open("contoh.txt", "rt") as f: #ketika sudah menjalankannya bisa pakai ini tanpa  melakukan close karena dengan menggunakan with maka file akan otomatis tertutup setelah selesai digunakan
    print (f.read())

with open("contoh.txt") as f:
  print(f.read(5))  #membaca 5 karakter pertama

with open("contoh.txt") as f:  #membaca baris 2 x
  print(f.readline())
  print(f.readline())

with open("contoh.txt") as f:
  for x in f:
    print(x)

with open("contoh.txt", "a") as f:
    f.write("\n nim: 25071100710") #untuk menambahkan baris baru pada file contoh.txt

time.sleep(5) #untuk memberikan jeda waktu selama 1 detik sebelum mengeksekusi kode selanjutnya

with open("contoh.txt", "w") as f:
   f.write("ke overwrite") #untuk menimpa file contoh.txt dengan tulisan "ke overwrite file"


with open("file_baru.txt", "x") as f: #untuk membuat file baru dengan nama file_baru.txt
    pass

with open("file_baru.txt", "x") as f:
    f.write("isi file baru") #untuk menulis isi pada file_baru.txt dengan tulisan "isi file baru"


import os
os.remove("file_baru.txt") #untuk menghapus file_baru.txt

# import os
# if os.path.exists("file_baru.txt"):
#   os.remove("file_baru.txt")
# else:
#   print("The file does not exist")


# import os
# os.rmdir("myfolder") #untuk menghapus folder myfolder



# import os
# def tampilkanMenu():
#     print("============================")
#     print("PYTHON FILE MANAGER v1.0")
#     print("============================")

#     print("[1] Read file")
#     print("[2] Write file")
#     print("[3] Delete file")
#     print("[0] Exit")

#     pilihan = int(input('Pilih menu: '))
#     return pilihan



# def tampilkanFile():
#     print('------------------------------')
#     print('File tersedia:')
#     print('[1] catatan.txt')
#     print('[2] tugas.txt')
#     print('[3] jadwal.txt')

# def pilihFile():
#     print('------------------------------')
#     print('File tersedia:')
#     print('[1] catatan.txt')
#     print('[2] tugas.txt')
#     print('[3] jadwal.txt')


#     pilihan = int(input('Pilih file (nomor): '))
#     return pilihan

# def pilihFileW():
#     print('------------------------------')
#     print('File tersedia:')
#     print('[1] catatan.txt')
#     print('[2] tugas.txt')
#     print('[3] jadwal.txt')
#     print('kalo mau bikin file baru ketik [0]')


#     pilihan = int(input('Pilih file (nomor): '))
#     return pilihan

# def buatfile(file):
#     with open(file, 'x') as f:
#         f.write('masukkan isi file baru : ')


# def tulisfile(file):
#     with open(file, 'a') as f :
#         f.write(input(f'masukkan tulisan :'))


# def hapusfile(file):

#     if os.path.exists (file):
#         yakin = input('yakin mau hapus?? (y/n)')
#         if yakin.lower() == 'y' :
#             os.remove(file)
#     else: 
#         print('file tidak ada')

# def bacaFile(file):
#     print(f'--- Isi {file} ---')
#     with open(file ) as f :
#         print(f.read1())



        




# def main():
#     while True :
#         pilihMenu = tampilkanMenu()
#         match pilihMenu :
#             case 1 :
#                 pilihanFileR =  pilihFile()

#                 match pilihanFileR :
#                     case 1 :
#                         bacaFile('catatan.txt')
#                     case 2 : 
#                         bacaFile('tugas.txt')
#                     case 3 :
#                         bacaFile('jadwal.txt')





#             case 2 :
#                 pilihanFileW =  pilihFileW()
           
#                 match pilihanFileW :
#                     case 1 :
#                         tulisfile('catatan.txt')
#                     case 2 : 
#                         tulisfile('tugas.txt')
#                     case 3 :
#                         tulisfile('jadwal.txt')
#                     case 0 :
#                         namafile = input("masukkan nama file baru: ")
#                         buatfile(namafile)
                        
        
#             case 3 :
#                 pilihanFileD =  pilihFile()

#                 match pilihanFileD : 
                
#                     case 1 :
#                         hapusfile('catatan.txt')
#                     case 2 : 
#                         hapusfile('tugas.txt')
#                     case 3 :
#                         hapusfile('jadwal.txt')
#             case 0 :
#                 break
#         print('------------------------------')






# main()
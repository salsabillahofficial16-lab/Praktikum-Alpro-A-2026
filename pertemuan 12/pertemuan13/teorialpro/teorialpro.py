# #baca
# with open("data.txt", "r") as f: 
#     print(f.read())

#tulis
with open("heloo.txt", "w") as f:
    f.write("Ini adalah isi file data.txt")

#tambah
with open("data.txt", "a") as f:
    f.write("hobi : jalan jalan")

#hapus
import os
if os.path.exists("heloo.txt"):
    os.remove("heloo.txt")

#hitung 
with open("data.txt") as f: 
    print(f.readlines())

#simpan inputan user
with open("data.txt", "a") as f:
    f.write(input("masukkan hobi : "))

#tampilkan isi file perbaris
with open("data.txt") as f: 
    for line in f:
        print(line)


struktur = {
    "Skripsi_Aqil" :{
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
    },
    "Bab_3": {
        "metodologi.docx": 89,
        "diagram": {
            "flowchart.png": 512,
            "erd.png": 278,
            "arsitektur": {
                "sistem.png": 430
            }
        }
    },
    "sidang": {
        "presentasi.pptx": 2048,
        "catatan_revisi.txt": 15
    },
    "README.txt": 8
    }
}

#hitung total ukuran
def total_ukuran(folder: dict) -> int:
    total = 0
    for item in folder:
        if type(folder[item]) == int:
            total += folder[item] 
        else:
            total += total_ukuran(folder[item]) 
    return total

print(f"Total ukuran skripsi: {total_ukuran(struktur)} KB")

#hitung jumlah file
def hitung_file(folder: dict) -> int:
    total = 0
    for item in folder:
        if type(folder[item]) == int:
            total += 1
        else:
            total += hitung_file(folder[item])
    
    return total

print(f"Jumlah file: {hitung_file(struktur)}")

# cari file terbesar
def cari_terbesar(folder: dict) -> tuple:
    # Kembalikan (nama_file, ukuran_kb)
    nama_file = ""
    ukuran_kb = 0

    for nama, isi in folder.items():
        if isinstance(isi, dict):
            file_terbesar, ukuran_terbesar = cari_terbesar(isi)
            if ukuran_terbesar > ukuran_kb:
                nama_file = file_terbesar
                ukuran_kb = ukuran_terbesar
        else:
            if isi > ukuran_kb:
                nama_file = nama
                ukuran_kb = isi

    return nama_file, ukuran_kb

nama, ukuran = cari_terbesar(struktur)
print(f"File terbesar: {nama} ({ukuran} KB)")

#cetak struktur folder
def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    indentasi = "    " * level

    if level == 0:
        print("📁", nama)

    for key in folder:
        value = folder[key]

        if isinstance(value, dict):
            print(indentasi + "📁 " + key)
            tampilkan_tree(value, key, level + 1)

        else:
            print(indentasi + "📄 " + key + " (" + str(value) + " KB)")

tampilkan_tree(struktur)
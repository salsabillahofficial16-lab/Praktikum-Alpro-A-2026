class nama_terlalupendek(Exception):
    def __init__(self, nama):
        self.nama = nama
        super().__init__(f'nama tidak  valid. minimal 3 karakter')

class umurtidakvalid(Exception):
    def __init__(self, umur):
        self.umur = umur
        super().__init__(f'umur tidak memenuhi syarat, umur harus 17-60 tahun ')

class email(Exception):
    def __init__(self, email):
        self.email = email
        super().__init__(f'emai tidak valid! email harus menggunakan @')

class nomorhp(Exception):
    def __init__(self, nomor):
        self. nomor = nomor
        super().__init__(f'nomorhp tidak valid! nomorhp Harus 10-13 digit angka')

def validasi_namaterlalupendek(nama_input):
    if len(nama_input) < 3:
        raise nama_terlalupendek(nama_input)
    return True
def validasi_umurtidakvalid(umur_input):
    if umur_input < 17  or umur_input > 60:
        raise umurtidakvalid(umur_input)
    return True
def validasi_email(email_input):
    if '@' in email_input:
        pass
    else:
        raise email(email_input)
    return True
def validasi_nomorhp(nomorhp_input):
    if len (nomorhp_input) < 10 or len(nomorhp_input) > 13:
        raise nomorhp(nomorhp_input)
    return True

print(f"""==== REGISTRASI PESERTA SEMINAR ===""")
while True:
    try:
        nama = input("nama lengkap :")
        nama_valid = validasi_namaterlalupendek(nama)
    except nama_terlalupendek as sa:
        print(f'[eror] {sa}')
    else:
        break

while True:
    try:
        emaill = input("email :")
        email_valid = validasi_email(emaill)
    except email as sa:
        print(f'[eror] {sa}')
    else:
        break
while True:
    try:
        umur = int(input("umur :"))
        umur_valid = validasi_umurtidakvalid(umur)
    except ValueError:
        print('umur harus bilangan bulat')
    except umurtidakvalid as sa:
        print(f'[eror] {sa}')
    else:
        break
while True:
    try:
        nomorhpp = input("nomorhp :")
        nomorhp_valid = validasi_nomorhp(nomorhpp)
    except nomorhp as sa:
        print(f'[eror] {sa}')
    else:
        break
    finally:
        print("proses input selesai")

print(f"""=== DATA PESERTA ===
nama   : {nama}
umur   : {umur}
Email  : {emaill}
nomorhp  : {nomorhpp}
Status : TERDAFTAR""")




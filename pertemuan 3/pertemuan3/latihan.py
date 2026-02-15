class Negara:
    def __init__(self, nama, benua, ibukota):
        self.nama = nama
        self.benua = benua
        self.ibukota = ibukota

    def informasi(self):
        print(f"Negara: {self.nama}, benua: {self.benua}, ibukota: {self.ibukota}")

    def ubah_ibukota(self, ibukota_baru):
        self.ibukota = ibukota_baru
        
p1 = Negara("korea selatan", "asia", "seoul")
p2 = Negara("swedia", "eropa", "skotlandia")
p3 = Negara("indnesia", "asia", "jakarta")

print(p1.nama)
print(p2.benua)
print(p3.ibukota)


 






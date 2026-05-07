
# latihan no 1

def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1

pasien = [
"Budi Santoso", "Siti Rahayu", "Ahmad Fauzi", "Dewi Lestari",
"Eko Prasetyo", "Fitri Handayani", "Gilang Ramadan", "Hana Pertiwi",
"Irfan Maulana", "Joko Susilo"
]

namapasien = input("Masukkan nama pasien yang ingin dicari: ")
result = linearSearch(pasien, namapasien.lower())
if result != -1:
   print(namapasien, "ditemukan di urutan ke-", result + 1)
else:
  print(namapasien, "tidak ada dalam daftar hari ini.")


# latihan no 2
def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1
  perbandingan = 0

  while left <= right:
    mid = (left + right) // 2

    perbandingan += 1

    if arr[mid] == targetVal:
      return [mid, perbandingan]
    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return [-1, perbandingan ]

id_karyawan = [
1021, 1045, 1089, 1102, 1157, 1203, 1245, 1312,
1378, 1401, 1456, 1502, 1567, 1634, 1700
]

IDKaryawan = int(input("Masukkan ID karyawan yang dicari: "))
result_id = binarySearch(id_karyawan, IDKaryawan)
if result_id[0] != -1:
    print(f"Proses perbandingan: {result_id[1]} kali")
    print(f"ID {IDKaryawan} ditemukan! Posisi ke{result_id[0]+1} dalam daftar.") 
else:
  print(f"ID {IDKaryawan} tidak terdaftar sebagai karyawan.")


# no 3
rak_a = ["BK-045", "BK-012", "BK-078", "BK-033", "BK-091",
"BK-027", "BK-056"]
rak_b = ["BK-011", "BK-023", "BK-035", "BK-047", "BK-059",
"BK-071", "BK-083", "BK-095"]

kodeBuku = input("Masukkan kode buku yang dicari: ")

print("Mencari di Rak A (Linear Search)...")
resultbuku_linear = linearSearch(rak_b, kodeBuku)
if resultbuku_linear != -1:
  print(kodeBuku," ditemukan di urutan ke-", resultbuku_linear+1)
else:
  print(kodeBuku, "tidak ditemukan di Rak A.")

print("Mencari di Rak B (Binary Search)...")
resultbuku_binary = binarySearch(rak_b, kodeBuku)
if resultbuku_binary[0] != -1:
  print(f" {kodeBuku} ditemukan di rak B! Posisi ke{resultbuku_binary[0]+1} di rak B")
else:
  print(f" {kodeBuku} tidak ditemukan di Rak B.")
  print(f"kesimpulan: Buku {kodeBuku} tersedia di rak B.")

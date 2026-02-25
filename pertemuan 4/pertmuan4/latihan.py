#soal  1  
angka_list = [10, 20, 30]
try:
    idx = int(input('masukkan  index (0-2): '))
    print(f'nilai: {angka_list[idx]}')
except ValueError:
    print('harus berupa angka  bulat!')
except IndexError:
    print('index di luar jangkauan!')
finally:
    print('selesai')

#soal no 2
try:
    angka1 = float(input('masukkan angka  1 :'))#angka 1 sebagai pembilang
    angka2 = float(input('masukkan angka 2 :'))#angka 2 sebagai penyebut
    print(f'hasil bagi = {angka1 / angka2}')
except ValueError:
    print('harus  angka!')
except ZeroDivisionError:
    print('tidak boleh massukkan angka 0')
finally:
    print('sudah selesaiiii!')


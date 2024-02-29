### LIST BARANG DI GUDANG
data_logistik = [
{'Kode Barang':1,'Nama Barang':'Susu Kental Manis'     ,'Satuan':'Kaleng' ,'Barang Keluar':0,'Barang Masuk':5,'Stock Barang':5},
{'Kode Barang':2,'Nama Barang':'Susu UHT'              ,'Satuan':'Dus'    ,'Barang Keluar':0,'Barang Masuk':5,'Stock Barang':5},
{'Kode Barang':3,'Nama Barang':'Boba'                  ,'Satuan':'Bungkus','Barang Keluar':0,'Barang Masuk':5,'Stock Barang':5},
{'Kode Barang':4,'Nama Barang':'Susu Bubuk Varian Rasa','Satuan':'Bungkus','Barang Keluar':0,'Barang Masuk':5,'Stock Barang':5},
{'Kode Barang':5,'Nama Barang':'Cheese Cream'          ,'Satuan':'Bungkus','Barang Keluar':0,'Barang Masuk':5,'Stock Barang':5}
]

def main():
  print('''
        ========= KAMSIA BOBA GEMPOL SARI =========

        --------- Sistem Informasi Gudang ---------
        
          1. Menampilkan Daftar Barang
          2. Menambahkan Daftar Barang
          3. Memperbaharui Daftar Barang
          4. Menghapus Daftar Barang
          5. Keluar
        ''')

def read_data ():
  print('''
          ----------Menampilkan Daftar Barang----------
            1. Tampilkan Seluruh Daftar Barang
            2. Tampilkan Data Barang
            3. Mencari Data Tertentu
            4. Kembali ke Menu
          ''')

# MENAMPILKAN SELURUH DATA 
  read_data = int(input('Silahkan Pilih Menu Menampilkan Daftar Barang : '))
  if read_data == 1 :
    from tabulate import tabulate
    header = data_logistik[0].keys()
    rows = [x.values() for x in data_logistik]
    print('\n',tabulate(rows, header))
    print('\nDaftar Barang Berhasil Ditampilkan.\n')

# MENAMPILKAN SATU ROW DATA 
  elif read_data == 2:
    from tabulate import tabulate
    read_data1 = int(input('\nMasukkan Kode Barang : '))
    i = read_data1 - 1
    if read_data1 > len(data_logistik) :
      print('\nKode Barang Tidak Tersedia.')
    elif i != 0 :
        headers = data_logistik[i].keys()
        rows = [x.values() for x in data_logistik[i:i+1]]
        print('\n',tabulate(rows,headers))
    elif i == 0 :
        headers = data_logistik[i].keys()
        rows = [x.values() for x in data_logistik[0:1]]
        print('\n',tabulate(rows,headers))
    print('\nData Barang Berhasil Ditampilkan.\n')

# MENCARI DATA TERTENTU
  elif read_data == 3 :
    read_data2 = int(input('\nMasukkan Kode Barang : '))
    read_data3 = input('\nMasukkan Kata Kunci : ')
    i_2 = read_data2 - 1 # index dictionary
    if read_data2 > len(data_logistik) :
      print('\nKode Barang Tidak Tersedia.')
    elif read_data3 in data_logistik[i_2] :
      nilai = data_logistik[i_2][read_data3]
      print(f'\nData {read_data3} dengan Kode Barang {read_data2} = {nilai}')
    else :
      print('\nData Tidak Tersedia')

def create_data ():
  print('''       
        ----------Menambahkan Daftar barang----------
          1. Tambah Daftar Barang
          2. Kembali ke Menu 
        ''')

  create_data = int(input('Silahkan Pilih Menu Menambahkan Daftar Barang : '))
  from tabulate import tabulate
  if create_data == 1 :
    kode_barang = int(input('\nMasukkan Kode Barang : '))
    nama_barang = input('Masukkan Nama Barang : ')
    for i in data_logistik :  
      if kode_barang < len(data_logistik) :
        if i == data_logistik[(kode_barang-1)] :
            print(data_logistik[(kode_barang-1)])
            print('\nData Sudah Ada.')
            break
      else :
        satuan = input('Masukkan Satuan : ')
        barang_masuk = int(input('Masukkan Jumlah Barang Masuk : '))
        barang_keluar = int(input('Masukkan Jumlah Barang Keluar : '))
        stock_barang = int(input('Masukkan Stock Barang : '))
        certain = input('Apakah Data Akan Disimpan?(Y/N) : ')
        if certain == 'Y' or certain == 'y':
            data_logistik.extend([{'Kode Barang':kode_barang,'Nama Barang':nama_barang,'Satuan':satuan,'Barang Masuk':barang_masuk,'Barang Keluar':barang_keluar,'Stock Barang':stock_barang}])
            header = data_logistik[0].keys()
            rows = [x.values() for x in data_logistik]
            print('\n',tabulate(rows, header))
            print('\nData Berhasil Disimpan.\n')
        elif certain == 'N' or certain == 'n':  
            print('\nData Tidak Jadi Disimpan.')
        break
          
def update_data ():
  print('''
        ----------Memperbaharui Daftar barang----------
          1. Perbaharui Daftar Barang
          2. Kembali ke Menu 
        ''')
  
  update_data = int(input('Silahkan Pilih Menu Memperbaharui Daftar Barang : '))
  if update_data == 1 :
    kode_barang1 = int(input('\nMasukkan Kode Barang : '))   
    for i in data_logistik:
        if kode_barang1 > len(data_logistik):
            print('\nData Tidak Ada.')
            break
        if i == data_logistik[(kode_barang1-1)] :
            print(data_logistik[(kode_barang1-1)])
            certain1 = input('\nApakah Anda Akan Memperbaharui Data Tersebut?(Y/N) : ')
            if certain1 == 'Y' or certain1 == 'y':
              certain2 = input('\nMasukkan Data Yang Akan Anda Perbaharui : ')
              if certain2 != 'Stock Barang':
                if certain2 == 'Barang Masuk':
                    data_logistik[kode_barang1-1][certain2] = int(input(f'\nSilahkan Perbaharui Barang Masuk :'))                 
                    data_logistik[kode_barang1-1]['Stock Barang'] = data_logistik[kode_barang1-1][certain2] - data_logistik[kode_barang1-1]['Barang Keluar']
                    print('\nData Berhasil Diperbaharui.')
                elif certain2 == 'Barang Keluar':
                    data_logistik[kode_barang1-1][certain2] = int(input(f'\nSilahkan Perbaharui Barang Keluar :'))                  
                    data_logistik[kode_barang1-1]['Stock Barang'] = data_logistik[kode_barang1-1]['Barang Masuk'] - data_logistik[kode_barang1-1][certain2]
                    print('\nData Berhasil Diperbaharui.')
                else :
                    data_logistik[kode_barang1-1][certain2] = input(f'\nSilahkan Perbaharui {certain2} :') 
                    print('\nData Berhasil Diperbaharui.')
              elif certain2 == 'Stock Barang':
                print('\nData Tidak Dapat Diperbaharui.') 
            elif certain1 == 'N' or certain1 == 'n':
              print('\nData Tidak Jadi Diperbaharui.')

def delete_data ():
  print('''
        ----------Menghapus Daftar barang----------
          1. Hapus Daftar Barang
          2. Kembali ke Menu 
        ''')
  
  delete_data = int(input('\nSilahkan Pilih Menu Menghapus Daftar Barang : '))
  if delete_data == 1 :
    kode_barang2 = int(input('\nMasukkan Kode Barang : '))
    if kode_barang2 > len(data_logistik):
        print('\nData Tidak Ada.')

    for i in data_logistik:
        if i == data_logistik[(kode_barang2-1)] :
            print(data_logistik[(kode_barang2-1)])
            certain2 = input('\nAnda Yakin Akan Menghapus Data Tersebut?(Y/N) : ')
            if certain2 == 'Y' or certain2 == 'y':
              del data_logistik[kode_barang2-1]
              print('\nData Berhasil Dihapus.')
            elif certain2 == 'N' or certain2 == 'n':
              print('\nData Tidak Jadi Dihapus.')

main()
main_menu = int(input('Silahkan Pilih Menu (1-5) : '))
while main_menu != 5:
    if main_menu == 1:
        read_data()
    elif main_menu == 2:
        create_data()
    elif main_menu == 3:
        update_data()
    elif main_menu == 4:
        delete_data()
    else:
        print('\nPilihan Menu Tidak Valid. \n\nSilahkan Coba Lagi.')
    main()
    main_menu = int(input('Silahkan Pilih Menu (1-5) : '))
print('\nTerima kasih.\n')
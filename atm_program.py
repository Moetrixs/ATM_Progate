import random
import datetime
import os
from customer import Customer

os.system('cls')

atm = Customer(id)

while True:
    id = int(input('\nMasukan pin anda: '))
    trial = 1

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input('\nPin anda salah (' + str(trial) +')' + '\n\nSilahkan Masukan lagi: '))
        trial += 1

        if trial == 3:
            print('\n!Error!.\nPin anda salah (' + str(trial) +')' + '\n\nSilahkan ambil kartu dan coba lagi ...')
            exit()

    os.system('cls')
    while True:
        print('\nSelamat datang di ATM progate ...')
        print('\n1-Cek Saldo \n2-Tarik \n3-Simpan \n4-Ganti Pin')

        selectmenu = int(input('\nSilahkan pilih menu: '))
        os.system('cls')
        if selectmenu == 1:
            print('\nCEK SALDO')
            print('\nSaldo anda sekarang: Rp. ' + str(atm.checkBalance()) + '')

        elif selectmenu == 2:
            print('\nTARIK')
            nominal = float(input('\nMasukan nominal penarikan: '))
            verify_withdraw = input('Konfirmasi: Anda akan melakukan penarikan dengan nominal ' + str(nominal) + ' ? (Y/N): ')

            if verify_withdraw.upper() == 'Y':
                print('\nSaldo awal anda adalah: Rp. ' + str(atm.checkBalance()) + '')
            else:
                break

            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print('Transaksi Penarikan Berhasil!')
                print('Saldo sisa sekarang: Rp. ' + str(atm.checkBalance()) + '')
            else:
                print('Maaf. Saldo anda tidak cukup untuk melakukan Penarikan!')
                print('Silahkan lakukan penambahan nominal saldo')

        elif selectmenu == 3:
            print('\nSIMPAN')
            nominal = float(input('\nMasukan nominal Simpan: '))
            verify_deposit = input('Konfirmasi: Anda akan melakukan penyimpanan dengan nominal ' + str(nominal) + ' ? (Y/N): ')

            if verify_deposit.upper() == 'Y':
                atm.depositBalance(nominal)
                print('\nSaldo anda sekarang adalah: Rp. ' + str(atm.checkBalance()) + '')
            else:
                break

        elif selectmenu == 4:
            print('\nUBAH PIN')
            verify_pin = int(input('\nmasukan pin anda: '))

            while verify_pin != int(atm.checkPin()):
                print('Pin anda salah, Silahkan masukan kembali pin anda : ')

            updated_pin = int(input('Silahkan masukan pin baru: '))
            print('PIN anda berhasil diganti!')

            verify_newpin = int(input('\nCoba masukan pin baru: '))

            if verify_newpin == updated_pin:
                print('pin baru anda sukses!')
            else:
                print('maaf, pin anda salah!')

        else:
            print('\nError. Maaf, Menu tidak tersedia')

        Q = input('\nPerlu Transaksi Lain? (Y/N) : ')
        if Q.upper() == 'Y':
            os.system('cls')
        else:
            print('-'*45)
            print('Resi tercetak otomatis saat anda keluar. \nHarap simpan tanda terima ini \nsebagai bukti transaksi anda.')
            print('\nNo. Record: ',random.randint(100000, 1000000))
            print('Tanggal: ', datetime.datetime.now())
            print('Saldo akhir: ', atm.checkBalance())
            print('\nTerimakasih telah menggunakan ATM Progate!')
            print('-'*45)
            print("\n Silahkan ambil kartu anda, Terima kasih")
            exit()
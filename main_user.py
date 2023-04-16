from modul import Transaction

"""
    File main_user.py digunakan untuk implementasi method-method dengan input interaktif user.
"""
try:
    yesno = input("Apakah anda ingin melakukan transaksi? (Y/n)")
    if yesno == 'y' or yesno == 'Y':
        transaction = Transaction()
        while True:
            print("Pilih Menu:")
            print("\n1. Tambah item")
            print("2. Ubah nama item")
            print("3. Ubah jumlah item")
            print("4. Ubah harga item")
            print("5. Hapus item")
            print("6. Periksa pesanan")
            print("7. Reset transaksi")
            print("8. Total transaksi")
            print("9. Keluar")

            choice = input("\nMasukkan pilihan anda: ")

            if choice == "1":
                nama_item = input("Masukkan nama item: ")
                while True:
                    try:
                        jumlah_item = int(input("Masukkan jumlah item: "))
                        break
                    except ValueError:
                        print("Input harus berupa angka!")
                while True:
                    try:
                        harga_item = int(input("Masukkan harga item: "))
                        break
                    except ValueError:
                        print("Input harus berupa angka!")
                transaction.add_item([nama_item, jumlah_item, harga_item])

            elif choice == "2":
                nama_item = input("Masukkan nama item yang ingin diganti: ")
                nama_baru = input("Masukkan nama item baru: ")
                transaction.update_item_name(nama_item, nama_baru)

            elif choice == "3":
                nama_item = input("Masukkan nama item yang jumlahnya ingin diganti: ")
                while True:
                    try:
                        new_qty = int(input("Masukkan jumlah item baru: "))
                        break
                    except ValueError:
                        print("Input harus berupa angka!")
                transaction.update_item_qty(nama_item, new_qty)

            elif choice == "4":
                nama_item = input("Masukkan nama item yang harganya ingin diganti: ")
                while True:
                    try:
                        new_price = int(input("Masukkan harga item baru: "))
                        break
                    except ValueError:
                        print("Input harus berupa angka!")
                transaction.update_item_price(nama_item, new_price)

            elif choice == "5":
                nama_item = input("Masukkan nama item yang ingin dihapus: ")
                transaction.delete_item(nama_item)

            elif choice == "6":
                transaction.check_order()

            elif choice == "7":
                transaction.reset_transaction()
            
            elif choice == "8":
                transaction.total_price()

            elif choice == "9":
                print("Keluar dari aplikasi...")
                break
            else:
                print("Tidak terdapat pilihan tersebut, pilih lagi!")
    elif yesno == 'n' or yesno == 'N':
        print("Terima kasih!")
    else:
        raise NameError("Input salah!")
except NameError as n:
    print("Terjadi kesalahan: ", n)

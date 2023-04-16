# Super Cashier
Super Cashier adalah suatu project studi kasus sederhara dengan bahasa pemrograman Python yang menyelesaikan permasalahan sistem kasir pada supermarket.

## Requirements / Objectives
Suatu sistem self-servce kasir supermarket yang dapat melakukan:
1. Membuat transaksi yang unik berdasarkan pendefinisian object.
2. Membuat proses penambahan item
3. Membuat proses update untuk mengubah nama, jumlah, atau harga dengan method-method yang terpisah sesuai fungsinya.
4. Membuat proses penghapusan item
5. Membuat proses pembatalan transaksi
6. Membuat proses pemeriksaan pesanan
7. Membuat proses perhitungan total belanja berdasarkan item yang sudah diinput. Perhitungan total belanja memiliki ketentuann diskon, yaitu:
    * Total belanja > Rp200.000 -> 5%
    * Total belanja > Rp300.000 -> 8%
    * Total belanja > Rp500.000 -> 10%

## Alur Program
1. User memutuskan apakah akan membuat transaksi atau tidak.
2. Jika iya, user akan memilih menu berdasarkan fitur yang ada. Jika tidak, aplikasi berhenti
2. Jika user memilih untuk melakukan transaksi, akan keluar menu berdasarkan fitur yang ada.
3. Jika user memilih menu pertama (tambah item), maka user akan menginput nama, jumlah, dan harga item yang akan diproses pada method `add_item()`
4. Jika user memilih menu kedua (ubah nama item), maka user akan menginput nama item yang ingin diganti dan nama item baru yang akan diproses pada method `update_item_name()`
5. Jika user memilih menu ketiga (ubah jumlah item), maka user akan menginput nama item yang ingin diganti jumlahya dan jumlah item baru yang akan diproses pada method `update_item_qty()`
6. Jika user memilih menu keempat (ubah harga item), maka user akan menginput nama item yang ingin diganti harganya dan nama item baru yang akan diproses pada method `update_item_price()`
7. Jika user memilih menu kelima (hapus item), maka user akan menginput nama item yang ingin dihapus yang akan diproses pada method `delete_item()`
8. Jika user memilih menu keenam (periksa pesanan), maka aplikasi akan menampilkan informasi pesanan yang sudah diinput dalam bentuk tabel dan memberitahu apakah data yang diinput sudah benar atau belum dengan method `check_order()`
9. Jika user memilih menu ketujuh (reset transaksi), maka seluruh transaksi dibatalkan dengan method `reset_transaction()`
10. Jika user memilih menu kedelapan (total transaksi), maka seluruh transaksi akan diperiksa kembali menggunakan `check_order()` dan dihitung berdasarkan ketentuan diskon dengan method `total_price()`
11. Jika user memilih menu terakhir (keluar), maka aplikasi berhenti

## Penjelasan Code
1. Script pada `main_user.py` digunakan untuk implementasi method-method dengan input interaktif user.
2. Script pada `main_test.py` digunakan untuk melakukan test case dengan memanggil method-method terkait secara langsung
3. Script pada `modul.py` merupakan script yang berisikan Class `Transaction()` dengan method-methodnya untuk melakukan requirements yang sudah dijelaskan.

## Hasil Test Case
* Test case 1
```python
t = Transaction()

# TEST CASE 1
t.add_item(['Ayam Goreng',2,20000])
t.add_item(['Pasta Gigi',3,15000])
```
Output:
![Output Test Case 1]('/img_test_case/test_case1.png')

* Test case 2
```python
t = Transaction()

# TEST CASE 1
t.add_item(['Ayam Goreng',2,20000])
t.add_item(['Pasta Gigi',3,15000])

# # TEST CASE 2
t.delete_item('Pasta Gigi')
```
Output:
![Output Test Case 1]('/img_test_case/test_case1.png')

* Test case 3
```python
t = Transaction()

# TEST CASE 1
t.add_item(['Ayam Goreng',2,20000])
t.add_item(['Pasta Gigi',3,15000])

# # TEST CASE 2
t.delete_item('Pasta Gigi')

# # TEST CASE 3
t.reset_transaction()
```
Output:
![Output Test Case 1]('/img_test_case/test_case1.png')

* Test case 4
```python
t = Transaction()

# TEST CASE 1
t.add_item(['Ayam Goreng',2,20000])
t.add_item(['Pasta Gigi',3,15000])

# # TEST CASE 2
t.delete_item('Pasta Gigi')

# # TEST CASE 3
t.reset_transaction()

# TEST CASE 4
t.add_item(['Ayam Goreng',2,20000])
t.add_item(['Pasta Gigi',3,15000])
t.add_item(['Mainan Mobil',1,200000])
t.add_item(['Mi Instan', 5, 3000])
t.total_price()
```
Output:
![Output Test Case 1]('/img_test_case/test_case1.png')

## Conclusion/Future Work
* Dengan adanya aplikasi Super Cashier ini, user dapat melakukan self service pada kasir supermarket dengan lebih mudah.
* Jika waktu dan SDM lebih, program ini dapat dikembangkan dengan menggunakan database yang lebih baik agar barang bisa dipilih langsung dari persediaan yang ada.
from tabulate import tabulate

class Transaction:
    """
    Class untuk melakukan semua fitur transaksi
    """
    def __init__(self):
        """
        Attribute instance untuk mendefinisikan attribute pesanan dan total_cost pada setiap pembuatan transaksi
        """
        self.pesanan = []
        self.total_cost = 0

    def add_item(self, item):
        """
        Fungsi untuk menambahkan item pesanan

        Parameter
        ---------
        item: list pesanan berupa `[<nama item>, <jumlah item>, <harga per item>]`
        """
        base_item = [None, None, None] # list dasar selalu memiliki ukuran 1x3, agar mudah untuk mengidentifikasi salah input
        for b in range(len(item)):
            base_item[b] = item[b]
        self.pesanan.append(base_item)
        return print(f"Item yang dibeli adalah: {self.pesanan}")

    def update_item_name(self, nama_item, nama_item_baru):
        """
        Fungsi untuk mengubah nama item jika ada kesalahan input

        Parameter
        ---------
        nama_item: nama item yang ingin diganti
        nama_item_baru: nama item baru
        """
        try:
            # Melakukan pemeriksaan apakah nama item yang dimaksud terdapat pada list pesanan
            if any(nama_item == x[0] for x in self.pesanan):
                # looping untuk melakukan update nama item
                for item in self.pesanan:
                    if item[0] == nama_item:
                        item[0] = nama_item_baru
                return print(f"Nama item {nama_item} diubah menjadi {nama_item_baru}, sehingga detail pesanan menjadi: {self.pesanan}")
            else:
                return print(f"Item dengan nama {nama_item} tidak ditemukan dalam pesanan.")
        except Exception as e:
            print("Terjadi kesalahan:", e)

    def update_item_qty(self, nama_item, jumlah_item_baru):
        """
        Fungsi untuk mengubah jumlah item berdasarkan nama item jika ada kesalahan input
        
        Parameter
        ---------
        nama_item: nama item yang ingin diganti jumlahnya
        jumlah_item_baru: jumlah item baru
        """
        try:
            # Melakukan pemeriksaan apakah nama item yang dimaksud terdapat pada list pesanan
            if any(nama_item == x[0] for x in self.pesanan):
                # looping untuk melakukan update jumlah item
                for item in self.pesanan:
                    if item[0] == nama_item:
                        item[1] = jumlah_item_baru
                return print(f"Jumlah item {nama_item} diubah menjadi {jumlah_item_baru}, sehingga detail pesanan menjadi: {self.pesanan}")
            else:
                return print(f"Item dengan nama {nama_item} tidak ditemukan dalam pesanan.")
        except Exception as e:
            print("Terjadi kesalahan:", e)
        
    def update_item_price(self, nama_item, harga_item_baru):
        """
        Fungsi untuk mengubah harga item berdasarkan nama item jika ada kesalahan input
        
        Parameter
        ---------
        nama_item: nama item yang ingin diganti harganya
        harga_item_baru: harga item baru
        """
        try:
            # Melakukan pemeriksaan apakah nama item yang dimaksud terdapat pada list pesanan
            if any(nama_item == x[0] for x in self.pesanan):
                # looping untuk melakukan update harga item
                for item in self.pesanan:
                    if item[0] == nama_item:
                        item[2] = harga_item_baru
                return print(f"Harga item {nama_item} diubah menjadi {harga_item_baru}, sehingga detail pesanan menjadi: {self.pesanan}")
            else:
                return print(f"Item dengan nama {nama_item} tidak ditemukan dalam pesanan.")
        except Exception as e:
            print("Terjadi kesalahan:", e)

    def delete_item(self, nama_item):
        """
        Fungsi untuk menghapus item berdasarkan nama item

        Parameter
        ---------
        nama_item: nama item yang ingin dihapus
        """
        try:
            # Melakukan pemeriksaan apakah nama item yang dimaksud terdapat pada list pesanan
            if any(nama_item == x[0] for x in self.pesanan):
                # looping untuk menghapus item yang dipilih
                for i in range(len(self.pesanan)):
                    if self.pesanan[i][0] == nama_item:
                        del self.pesanan[i]
                        break
                return print(f"Item {nama_item} telah dihapus. {self.pesanan}")
            else:
                return print(f"Item dengan nama {nama_item} tidak ditemukan dalam pesanan.")
        except Exception as e:
            print("Terjadi kesalahan:", e)

    def reset_transaction(self):
        """
        Fungsi untuk membatalkan pesanan dengan mereset seluruh attribute yang ada (pesanan dan total_cost)
        """
        self.pesanan = []
        self.total_cost = 0
        return print(f'Semua item berhasil didelete! {self.pesanan}')

    def check_order(self):
        """
        Fungsi untuk memeriksa pesanan dengan menampilkan seluruh pesanan dalam bentuk tabel dan memberitahu apakah ada kesalahan input
        """

        # Menampilkan pesanan dalam bentuk tabel dengan tabulate
        header = ["No", "Item", "Jumlah Item", "Harga/Item"]
        with_numbering = [[i+1] + row for i,
                              row in enumerate(self.pesanan)]
        print(tabulate(with_numbering, headers=header))
        print("\n")
        try:
            # Melakukan pemeriksaan salah input
            for item in self.pesanan:
                nama_item = item[0]
                jumlah_item = item[1]
                harga_item = item[2]
                if not all([nama_item, jumlah_item, harga_item]):
                    raise ValueError("Informasi pada item tidak lengkap. Harap isi semua informasi pada setiap item.")
                if not isinstance(nama_item, str):
                    raise TypeError(f"Nama item {item[0]} harus berupa string")
                if not isinstance(jumlah_item, (int, float)):
                    raise TypeError(f"Jumlah item {item[0]} harus berupa integer atau float")
                if not isinstance(harga_item, int):
                    raise TypeError(f"Harga item {item[0]} harus berupa integer")
            return True
        except TypeError as e:
            print("Terjadi kesalahan: ", e)
            return False
        except ValueError as v:
            print("Terjadi kesalahan: ", v)
            return False
    
    def total_price(self):
        """
        Fungsi untuk menghitung seluruh pesanan berdasarkan ketentuan diskon
        """

        # Sebelum menghitung, melakukan check_order() untuk memastikan apakah data yang diinput sudah benar
        if not self.check_order():
            return print("Terjadi kesalahan input, perhitungan pesanan dibatalkan!")
            
        total = 0
        for i in range(len(self.pesanan)):
            total += (self.pesanan[i][1] * self.pesanan[i][2])
        if total > 500000:
            total *= 0.9
        elif total > 300000:
            total *= 0.92
        elif total > 200000:
            total *= 0.95
        
        self.total_cost = total
        return print(f"Total Belanja yang harus dibayarkan adalah Rp{self.total_cost}")
from modul import Transaction
"""
    File main_test.py digunakan untuk melakukan test case method-method yang ada pada requirements.
"""

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
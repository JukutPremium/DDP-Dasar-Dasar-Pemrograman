nama_barang = input("Masukkan nama barang: ")
harga_barang = float(input("Masukkan harga barang: "))

pajak = harga_barang * 11/100
total = harga_barang + pajak

print("\nHASIL PERHITUNGAN")
print(f"Nama Barang: {nama_barang}\nHarga Barang: Rp {harga_barang:g}\nTotal Belanja + PPN (11%): Rp {total:g}")
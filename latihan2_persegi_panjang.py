try:
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))

    if panjang <= 0 or lebar <= 0:
        print("Panjang dan lebar harus lebih besar dari 0.")
    else:
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)

        print("\nHASIL PERHITUNGAN")
        print(f"Luas      : {luas:g} m²\nKeliling  : {keliling:g} m")
except ValueError:
    print("Input tidak valid. Masukkan angka.")
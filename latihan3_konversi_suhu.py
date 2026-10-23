try:
    celsius = float(input("Masukkan suhu dalam Celsius (°C): "))

    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15
    reamur = celsius * 4 / 5

    print("\nHASIL KONVERSI SUHU")
    print(f"Celsius    : {celsius:.2f} °C\nFahrenheit : {fahrenheit:.2f} °F\nKelvin     : {kelvin:.2f} K\nReamur     : {reamur:.2f} °Ré")

except ValueError:
    print("Input tidak valid. Masukkan angka.")
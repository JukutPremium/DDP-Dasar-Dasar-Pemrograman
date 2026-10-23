# Trace Table DDP Python

## 1. Latihan Biodata

**Contoh nilai variabel:**

- `name` = `"Kadek Ayu"`
- `nim` = `"2601001"`
- `prodi` = `"Sistem Informasi"`
- `hobi` = `"Fotografi"`

| No. | Proses | `name` | `nim` | `prodi` | `hobi` |
|---:|---|---|---|---|---|
| 1 | Inisialisasi nama | Kadek Ayu | - | - | - |
| 2 | Inisialisasi NIM | Kadek Ayu | 2601001 | - | - |
| 3 | Inisialisasi program studi | Kadek Ayu | 2601001 | Sistem Informasi | - |
| 4 | Inisialisasi hobi | Kadek Ayu | 2601001 | Sistem Informasi | Fotografi |
| 5 | Menampilkan biodata | Kadek Ayu | 2601001 | Sistem Informasi | Fotografi |

**Output:**

```text
Nama: Kadek Ayu
NIM: 2601001
Program  Studi: Sistem Informasi
Hobi: Fotografi
```

## 2. Latihan Persegi Panjang

**Contoh input:** panjang = 8, lebar = 4.

| No. | Proses | `panjang` | `lebar` | `luas` | `keliling` |
|---:|---|---:|---:|---:|---:|
| 1 | Input panjang | 8 | - | - | - |
| 2 | Input lebar | 8 | 4 | - | - |
| 3 | Validasi `panjang <= 0 or lebar <= 0` | 8 | 4 | - | - |
| 4 | Hitung `luas = panjang * lebar` | 8 | 4 | 32 | - |
| 5 | Hitung `keliling = 2 * (panjang + lebar)` | 8 | 4 | 32 | 24 |
| 6 | Menampilkan hasil | 8 | 4 | 32 | 24 |

**Perhitungan:**

- Luas = 8 × 4 = 32 m²
- Keliling = 2 × (8 + 4) = 24 m

**Output:**

```text
HASIL PERHITUNGAN
Luas      : 32 m²
Keliling  : 24 m
```

## 3. Latihan Konversi Suhu

**Contoh input:** Celsius = 25

| No. | Proses | `celsius` | `fahrenheit` | `kelvin` | `reamur` |
|---:|---|---:|---:|---:|---:|
| 1 | Input suhu Celsius | 25 | - | - | - |
| 2 | Hitung Fahrenheit | 25 | 77 | - | - |
| 3 | Hitung Kelvin | 25 | 77 | 298.15 | - |
| 4 | Hitung Reamur | 25 | 77 | 298.15 | 20 |
| 5 | Menampilkan hasil | 25 | 77 | 298.15 | 20 |

**Rumus:**

- Fahrenheit = (Celsius × 9 / 5) + 32
- Kelvin = Celsius + 273.15
- Reamur = Celsius × 4 / 5

**Output:**

```text
HASIL KONVERSI SUHU
Celsius    : 25.00 °C
Fahrenheit : 77.00 °F
Kelvin     : 298.15 K
Reamur     : 20.00 °Ré
```

## 4. Latihan Total Belanja dan PPN

**Contoh input:**

- `nama_barang` = `"Buku"`
- `harga_barang` = 100000

| No. | Proses | `nama_barang` | `harga_barang` | `pajak` | `total` |
|---:|---|---|---:|---:|---:|
| 1 | Input nama barang | Buku | - | - | - |
| 2 | Input harga barang | Buku | 100000 | - | - |
| 3 | Hitung PPN = harga × 11 / 100 | Buku | 100000 | 11000 | - |
| 4 | Hitung total = harga + pajak | Buku | 100000 | 11000 | 111000 |
| 5 | Menampilkan hasil | Buku | 100000 | 11000 | 111000 |

**Perhitungan:**

- PPN = Rp100.000 × 11 / 100 = Rp11.000
- Total belanja = Rp100.000 + Rp11.000 = Rp111.000

**Output:**

```text
HASIL PERHITUNGAN
Nama Barang: Buku
Harga Barang: Rp 100000
Total Belanja + PPN (11%): Rp 111000
```

---
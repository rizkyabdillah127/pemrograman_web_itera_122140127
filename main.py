# main.py

# Mengimpor modul math_operations dengan cara biasa
import math_operations

# Mengimpor fungsi tertentu dari modul math_operations
from math_operations import celsius_to_fahrenheit, celsius_to_kelvin

def main():
    # Menggunakan fungsi dari modul math_operations
    sisi = 4
    panjang = 5
    lebar = 3
    radius = 7
    celsius = 25

    # Menghitung luas dan keliling persegi
    print(f"Luas Persegi (sisi {sisi}): {math_operations.luas_persegi(sisi)}")
    print(f"Keliling Persegi (sisi {sisi}): {math_operations.keliling_persegi(sisi)}")

    # Menghitung luas dan keliling persegi panjang
    print(f"Luas Persegi Panjang (panjang {panjang}, lebar {lebar}): {math_operations.luas_persegi_panjang(panjang, lebar)}")
    print(f"Keliling Persegi Panjang (panjang {panjang}, lebar {lebar}): {math_operations.keliling_persegi_panjang(panjang, lebar)}")

    # Menghitung luas dan keliling lingkaran
    print(f"Luas Lingkaran (radius {radius}): {math_operations.luas_lingkaran(radius)}")
    print(f"Keliling Lingkaran (radius {radius}): {math_operations.keliling_lingkaran(radius)}")

    # Mengonversi suhu
    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)
    print(f"Suhu dalam Fahrenheit (Celsius {celsius}): {fahrenheit}")
    print(f"Suhu dalam Kelvin (Celsius {celsius}): {kelvin}")

if __name__ == "__main__":
    main()
# Input berat badan (dalam kilogram) dan tinggi badan (dalam meter)
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

# Menghitung BMI
bmi = berat / (tinggi * tinggi)

# Menentukan kategori BMI
if bmi < 18.5:
    kategori = "Berat badan kurang"
elif 18.5 <= bmi < 25:
    kategori = "Berat badan normal"
elif 25 <= bmi < 30:
    kategori = "Berat badan berlebih"
else:
    kategori = "Obesitas"

# Menampilkan hasil
print(f"\nBMI Anda adalah: {bmi:.2f}")
print(f"Kategori: {kategori}")
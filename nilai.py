# Data mahasiswa
mahasiswa = [
    {"nama": "Andi", "nim": "122140127", "nilai_uts": 85, "nilai_uas": 80, "nilai_tugas": 90},
    {"nama": "Budi", "nim": "122140128", "nilai_uts": 70, "nilai_uas": 75, "nilai_tugas": 65},
    {"nama": "Citra", "nim": "122140129", "nilai_uts": 60, "nilai_uas": 58, "nilai_tugas": 65},
    {"nama": "Dina", "nim": "122140130", "nilai_uts": 45, "nilai_uas": 50, "nilai_tugas": 48},
    {"nama": "Eka", "nim": "122140131", "nilai_uts": 90, "nilai_uas": 92, "nilai_tugas": 88},
]

# Proses perhitungan nilai akhir dan grade
for mhs in mahasiswa:
    nilai_akhir = (0.3 * mhs["nilai_uts"]) + (0.4 * mhs["nilai_uas"]) + (0.3 * mhs["nilai_tugas"])
    mhs["nilai_akhir"] = nilai_akhir
    
    # Menentukan grade
    if nilai_akhir >= 80:
        mhs["grade"] = "A"
    elif nilai_akhir >= 70:
        mhs["grade"] = "B"
    elif nilai_akhir >= 60:
        mhs["grade"] = "C"
    elif nilai_akhir >= 50:
        mhs["grade"] = "D"
    else:
        mhs["grade"] = "E"

# Menampilkan hasil
print("Data Nilai Mahasiswa:\n")
for mhs in mahasiswa:
    print(f"Nama        : {mhs['nama']}")
    print(f"NIM         : {mhs['nim']}")
    print(f"Nilai Akhir : {mhs['nilai_akhir']:.2f}")
    print(f"Grade       : {mhs['grade']}")
    print("-" * 30)
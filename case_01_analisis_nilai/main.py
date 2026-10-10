# ==========================================
# KASUS 1: ANALISIS NILAI MAHASISWA
# ==========================================

data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dimas", "nim": "230104", "tugas": 78, "uts": 82, "uas": 80},
    {"nama": "Eka", "nim": "230105", "tugas": 95, "uts": 92, "uas": 94},
]

# 1. Menghitung nilai akhir menggunakan List Comprehension
mahasiswa = [
    {
        **m,
        "nilai_akhir": m["tugas"] * 0.30
        + m["uts"] * 0.30
        + m["uas"] * 0.40,
    }
    for m in data_mahasiswa
]

# 2. Filter mahasiswa dengan nilai akhir di atas 80
berprestasi = list(
    filter(lambda m: m["nilai_akhir"] > 80, mahasiswa)
)

# 3. Mengurutkan mahasiswa dari nilai tertinggi
ranking = sorted(
    mahasiswa,
    key=lambda m: m["nilai_akhir"],
    reverse=True,
)

# 4. Menampilkan seluruh hasil
print("=" * 50)
print("       ANALISIS NILAI MAHASISWA")
print("=" * 50)

print("\nDAFTAR NILAI AKHIR:")
for m in mahasiswa:
    print(f'{m["nama"]:<10} | NIM: {m["nim"]} | '
          f'Nilai Akhir: {m["nilai_akhir"]:.2f}')

print("\nMAHASISWA BERPRESTASI (NILAI > 80):")
for m in berprestasi:
    print(f'{m["nama"]} - {m["nilai_akhir"]:.2f}')

print("\nRANKING MAHASISWA:")
for nomor, m in enumerate(ranking, start=1):
    print(f'{nomor}. {m["nama"]} - {m["nilai_akhir"]:.2f}')

print("\nMAHASISWA TERBAIK:")
terbaik = ranking[0]
print(f'Nama : {terbaik["nama"]}')
print(f'NIM  : {terbaik["nim"]}')
print(f'Nilai: {terbaik["nilai_akhir"]:.2f}')

print("=" * 50)
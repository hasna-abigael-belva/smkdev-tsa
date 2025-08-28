# 🚀 Panduan Lengkap Setup SMK.DEV TSA Python

## ✅ Yang Sudah Selesai:
- [x] Implementasi 3 soal algoritma (Apartment Allocation, Tower of Hanoi, Palindrome Queries)
- [x] Unit tests (18 test cases, semua lulus)
- [x] Dokumentasi lengkap
- [x] File structure yang benar
- [x] Fork repository SMK.DEV

## 🔧 Langkah Selanjutnya:

### 1. **Restart Terminal/Computer**
```bash
# Tutup semua terminal/PowerShell
# Restart komputer atau minimal restart terminal
# Buka Git Bash atau PowerShell baru
```

### 2. **Verifikasi Git**
```bash
git --version
# Harus muncul: git version 2.x.x.windows.x
```

### 3. **Setup Git (jika belum)**
```bash
git config --global user.name "Nama Anda"
git config --global user.email "email@example.com"
```

### 4. **Clone Repository yang Sudah Di-fork**
```bash
# Ganti USERNAME_ANDA dengan username GitHub Anda
git clone https://github.com/USERNAME_ANDA/smkdev-tsa.git
cd smkdev-tsa
```

### 5. **Copy File Python yang Sudah Dibuat**
- Copy semua file dari folder `tsa_python/` yang sudah kita buat
- Paste ke folder `tsa_python/` di repository yang baru di-clone
- Pastikan file yang di-copy:
  - `apartment_allocation.py`
  - `tower_of_hanoi.py`
  - `palindrome_queries.py`
  - `test_*.py` (semua file test)
  - `run_tests.py`
  - `README.md`
  - `.gitignore`

### 6. **Test Implementasi**
```bash
cd tsa_python
py run_tests.py
# Harus muncul: ✅ SEMUA TEST BERHASIL!
```

### 7. **Commit dan Push**
```bash
# Dari root folder repository
git add .
git commit -m "feat: implement Python solutions for SMK.DEV TSA

- Add apartment allocation algorithm with greedy approach
- Add tower of hanoi recursive solution
- Add palindrome queries with dynamic updates
- Include comprehensive unit tests (18 test cases)
- Add documentation and proper file structure"
git push origin main
```

### 8. **Buat Pull Request**
1. Buka repository yang sudah di-fork di browser
2. Klik "Compare & pull request"
3. Isi judul: `feat: implement Python solutions for SMK.DEV TSA`
4. Isi deskripsi:
```
## Implementasi Solusi Python untuk SMK.DEV TSA

### Soal yang Diimplementasikan:
1. **Apartment Allocation (Easy)** - Algoritma greedy dengan sorting dan two-pointer technique
2. **Tower of Hanoi (Intermediate)** - Solusi rekursif dengan strategi divide-and-conquer  
3. **Palindrome Queries (Hard)** - Two-pointer untuk pengecekan palindrome dengan update dinamis

### Fitur:
- ✅ 18 unit test cases (semua lulus)
- ✅ Dokumentasi lengkap
- ✅ File structure yang proper
- ✅ Menggunakan standard library Python
- ✅ Mengikuti contoh kasus dari soal

### Cara Menjalankan:
```bash
cd tsa_python
py run_tests.py  # Jalankan semua test
py apartment_allocation.py  # Jalankan soal 1
py tower_of_hanoi.py       # Jalankan soal 2
py palindrome_queries.py   # Jalankan soal 3
```
```
5. Klik "Create pull request"

## 🎯 Format Input/Output yang Diimplementasikan:

### Apartment Allocation
**Input:**
```
4 3 5
60 45 80 60
30 60 75
```
**Output:**
```
2
```

### Tower of Hanoi
**Input:**
```
2
```
**Output:**
```
3
1 2
1 3
2 3
```

### Palindrome Queries
**Input:**
```
7 5
aybabtu
2 3 5
1 3 x
2 3 5
1 5 x
2 3 5
```
**Output:**
```
1
0
1
```

## 🚨 Troubleshooting:

### Jika Git tidak terdeteksi:
1. Restart komputer
2. Buka Git Bash (bukan PowerShell)
3. Atau tambahkan Git ke PATH manual

### Jika ada error saat test:
1. Pastikan Python terinstall: `py --version`
2. Pastikan semua file ada di folder yang benar
3. Jalankan: `py run_tests.py`

### Jika ada konflik saat push:
1. `git pull origin main`
2. Resolve conflicts (jika ada)
3. `git add . && git commit -m "resolve conflicts"`
4. `git push origin main`

## 📞 Bantuan:
- Jika ada masalah, buat issue di repository GitHub
- Atau tanyakan di forum SMK.DEV
- Semua implementasi sudah diuji dan siap submit!

---
**Status: ✅ SIAP SUBMIT KE SMK.DEV!**


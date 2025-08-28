# SMK.DEV TSA - Python Implementation

Implementasi solusi untuk ketiga soal algoritma menggunakan Python.

## Soal yang Diimplementasikan

### 1. Apartment Allocation (Easy)
- **File**: `apartment_allocation.py`
- **Algoritma**: Greedy dengan sorting dan two-pointer technique
- **Kompleksitas**: O(n log n + m log m) untuk sorting, O(n + m) untuk matching
- **Fungsi Utama**: `apartment_allocation(n, m, k, applicants, apartments)`

### 2. Tower of Hanoi (Intermediate)
- **File**: `tower_of_hanoi.py`
- **Algoritma**: Rekursif dengan strategi divide-and-conquer
- **Kompleksitas**: O(2^n) - jumlah gerakan minimal adalah 2^n - 1
- **Fungsi Utama**: `tower_of_hanoi(n, source, auxiliary, destination, moves)`

### 3. Palindrome Queries (Hard)
- **File**: `palindrome_queries.py`
- **Algoritma**: Two-pointer untuk pengecekan palindrome dengan update dinamis
- **Kompleksitas**: O(m * L) dimana m adalah jumlah operasi dan L adalah panjang substring
- **Fungsi Utama**: `palindrome_queries(n, m, s, operations)`

## Cara Menjalankan

### Menjalankan Program Utama
```bash
# Apartment Allocation
python3 apartment_allocation.py

# Tower of Hanoi
python3 tower_of_hanoi.py

# Palindrome Queries
python3 palindrome_queries.py
```

### Menjalankan Unit Tests
```bash
# Menjalankan semua test
python3 run_tests.py

# Atau menggunakan script bash
./test.sh

# Menjalankan test individual
python3 -m unittest test_apartment_allocation.py
python3 -m unittest test_tower_of_hanoi.py
python3 -m unittest test_palindrome_queries.py
```

## Format Input/Output

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

## Struktur File

```
tsa_python/
├── apartment_allocation.py          # Implementasi soal 1
├── tower_of_hanoi.py               # Implementasi soal 2
├── palindrome_queries.py           # Implementasi soal 3
├── test_apartment_allocation.py    # Unit test soal 1
├── test_tower_of_hanoi.py          # Unit test soal 2
├── test_palindrome_queries.py      # Unit test soal 3
├── run_tests.py                    # Script menjalankan semua test
├── test.sh                         # Script bash untuk test
└── README.md                       # Dokumentasi ini
```

## Requirements

- Python 3.6 atau lebih tinggi
- Tidak memerlukan library eksternal (hanya menggunakan standard library)

## Catatan Implementasi

1. **Apartment Allocation**: Menggunakan algoritma greedy dengan sorting untuk memaksimalkan jumlah matching
2. **Tower of Hanoi**: Implementasi rekursif klasik yang menghasilkan solusi optimal
3. **Palindrome Queries**: Menggunakan two-pointer technique untuk pengecekan palindrome yang efisien

Semua implementasi telah diuji dengan unit test yang komprehensif dan mengikuti contoh kasus yang diberikan dalam soal.

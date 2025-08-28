def apartment_allocation(n, m, k, applicants, apartments):
    """
    Mengalokasikan apartemen kepada pelamar sebanyak mungkin.
    
    Args:
        n (int): Jumlah pelamar
        m (int): Jumlah apartemen yang tersedia
        k (int): Maksimal perbedaan ukuran yang diizinkan
        applicants (list): List ukuran apartemen yang diinginkan pelamar
        apartments (list): List ukuran apartemen yang tersedia
    
    Returns:
        int: Jumlah maksimal pelamar yang bisa mendapat apartemen
    """
    # Sort kedua list untuk memudahkan matching
    applicants.sort()
    apartments.sort()
    
    # Two-pointer technique
    i = 0  # pointer untuk applicants
    j = 0  # pointer untuk apartments
    count = 0
    
    while i < n and j < m:
        # Cek apakah apartemen j cocok untuk pelamar i
        if abs(applicants[i] - apartments[j]) <= k:
            count += 1
            i += 1
            j += 1
        elif applicants[i] < apartments[j]:
            # Ukuran yang diinginkan pelamar terlalu kecil
            i += 1
        else:
            # Ukuran apartemen terlalu kecil
            j += 1
    
    return count


def solve_apartment_allocation():
    """
    Fungsi utama untuk membaca input dan menampilkan output
    """
    # Baca input
    n, m, k = map(int, input().split())
    applicants = list(map(int, input().split()))
    apartments = list(map(int, input().split()))
    
    # Hitung dan tampilkan hasil
    result = apartment_allocation(n, m, k, applicants, apartments)
    print(result)


if __name__ == "__main__":
    solve_apartment_allocation()

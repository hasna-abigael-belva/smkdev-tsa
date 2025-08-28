def is_palindrome(s, start, end):
    """
    Mengecek apakah substring dari start sampai end adalah palindrome.
    
    Args:
        s (str): String yang akan dicek
        start (int): Posisi awal substring (1-based index)
        end (int): Posisi akhir substring (1-based index)
    
    Returns:
        bool: True jika palindrome, False jika tidak
    """
    # Konversi ke 0-based index
    start_idx = start - 1
    end_idx = end - 1
    
    while start_idx < end_idx:
        if s[start_idx] != s[end_idx]:
            return False
        start_idx += 1
        end_idx -= 1
    
    return True


def palindrome_queries(n, m, s, operations):
    """
    Memproses operasi palindrome queries.
    
    Args:
        n (int): Panjang string
        m (int): Jumlah operasi
        s (str): String awal
        operations (list): List operasi yang akan diproses
    
    Returns:
        list: List hasil untuk setiap operasi tipe 2
    """
    results = []
    s_list = list(s)  # Konversi ke list untuk memudahkan update
    
    for operation in operations:
        op_type = operation[0]
        
        if op_type == 1:
            # Operasi update: ubah karakter di posisi k menjadi x
            k, x = operation[1], operation[2]
            s_list[k-1] = x  # Konversi ke 0-based index
        
        elif op_type == 2:
            # Operasi query: cek apakah substring dari a sampai b adalah palindrome
            a, b = operation[1], operation[2]
            current_s = ''.join(s_list)
            is_pal = is_palindrome(current_s, a, b)
            results.append(1 if is_pal else 0)
    
    return results


def solve_palindrome_queries():
    """
    Fungsi utama untuk membaca input dan menampilkan output
    """
    # Baca input
    n, m = map(int, input().split())
    s = input().strip()
    
    operations = []
    for _ in range(m):
        op = input().split()
        op_type = int(op[0])
        
        if op_type == 1:
            # Operasi update: 1 k x
            k, x = int(op[1]), op[2]
            operations.append((op_type, k, x))
        elif op_type == 2:
            # Operasi query: 2 a b
            a, b = int(op[1]), int(op[2])
            operations.append((op_type, a, b))
    
    # Proses operasi
    results = palindrome_queries(n, m, s, operations)
    
    # Tampilkan hasil
    for result in results:
        print(result)


if __name__ == "__main__":
    solve_palindrome_queries()

def is_palindrome(s, start, end):
    """
    Mengecek apakah substring dari start sampai end adalah palindrome.
    """
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
    """
    results = []
    s_list = list(s)
    
    print(f"Initial string: {s}")
    
    for i, operation in enumerate(operations):
        op_type = operation[0]
        print(f"Operation {i+1}: {operation}")
        
        if op_type == 1:
            k, x = operation[1], operation[2]
            s_list[k-1] = x
            print(f"After update: {''.join(s_list)}")
        
        elif op_type == 2:
            a, b = operation[1], operation[2]
            current_s = ''.join(s_list)
            is_pal = is_palindrome(current_s, a, b)
            result = 1 if is_pal else 0
            results.append(result)
            print(f"Query {a}-{b}: {current_s[a-1:b]} -> {result}")
    
    return results


def solve_palindrome_queries():
    """
    Fungsi utama untuk membaca input dan menampilkan output
    """
    print("Reading input...")
    
    # Baca input
    n, m = map(int, input().split())
    print(f"n={n}, m={m}")
    
    s = input().strip()
    print(f"String: '{s}'")
    
    operations = []
    for i in range(m):
        op = input().split()
        op_type = int(op[0])
        print(f"Reading operation {i+1}: {op}")
        
        if op_type == 1:
            k, x = int(op[1]), op[2]
            operations.append((op_type, k, x))
        elif op_type == 2:
            a, b = int(op[1]), int(op[2])
            operations.append((op_type, a, b))
    
    print(f"Operations: {operations}")
    
    # Proses operasi
    results = palindrome_queries(n, m, s, operations)
    
    print(f"Results: {results}")
    
    # Tampilkan hasil
    for result in results:
        print(result)


if __name__ == "__main__":
    solve_palindrome_queries()


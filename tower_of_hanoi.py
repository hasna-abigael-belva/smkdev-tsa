def tower_of_hanoi(n, source, auxiliary, destination, moves):
    """
    Menyelesaikan puzzle Tower of Hanoi secara rekursif.
    
    Args:
        n (int): Jumlah disk yang akan dipindahkan
        source (int): Stack sumber (1, 2, atau 3)
        auxiliary (int): Stack bantuan (1, 2, atau 3)
        destination (int): Stack tujuan (1, 2, atau 3)
        moves (list): List untuk menyimpan urutan gerakan
    
    Returns:
        list: List berisi urutan gerakan (source, destination)
    """
    if n == 1:
        moves.append((source, destination))
        return moves
    
    # Pindahkan n-1 disk dari source ke auxiliary
    tower_of_hanoi(n-1, source, destination, auxiliary, moves)
    
    # Pindahkan disk terbesar dari source ke destination
    moves.append((source, destination))
    
    # Pindahkan n-1 disk dari auxiliary ke destination
    tower_of_hanoi(n-1, auxiliary, source, destination, moves)
    
    return moves


def solve_tower_of_hanoi():
    """
    Fungsi utama untuk membaca input dan menampilkan output
    """
    # Baca input
    n = int(input())
    
    # Selesaikan puzzle
    moves = []
    tower_of_hanoi(n, 1, 2, 3, moves)
    
    # Tampilkan hasil
    print(len(moves))  # Jumlah gerakan minimal
    for source, destination in moves:
        print(f"{source} {destination}")


if __name__ == "__main__":
    solve_tower_of_hanoi()

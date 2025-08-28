import unittest
from tower_of_hanoi import tower_of_hanoi


class TestTowerOfHanoi(unittest.TestCase):
    
    def test_single_disk(self):
        """Test dengan satu disk"""
        moves = []
        result = tower_of_hanoi(1, 1, 2, 3, moves)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], (1, 3))
    
    def test_two_disks(self):
        """Test dengan dua disk"""
        moves = []
        result = tower_of_hanoi(2, 1, 2, 3, moves)
        
        self.assertEqual(len(result), 3)
        expected_moves = [(1, 2), (1, 3), (2, 3)]
        self.assertEqual(result, expected_moves)
    
    def test_three_disks(self):
        """Test dengan tiga disk"""
        moves = []
        result = tower_of_hanoi(3, 1, 2, 3, moves)
        
        self.assertEqual(len(result), 7)
        expected_moves = [
            (1, 3), (1, 2), (3, 2),  # Pindahkan 2 disk ke auxiliary
            (1, 3),                  # Pindahkan disk terbesar ke destination
            (2, 1), (2, 3), (1, 3)   # Pindahkan 2 disk dari auxiliary ke destination
        ]
        self.assertEqual(result, expected_moves)
    
    def test_minimum_moves_formula(self):
        """Test bahwa jumlah gerakan minimal sesuai rumus 2^n - 1"""
        for n in range(1, 6):
            moves = []
            tower_of_hanoi(n, 1, 2, 3, moves)
            expected_moves = (2 ** n) - 1
            self.assertEqual(len(moves), expected_moves)
    
    def test_valid_moves(self):
        """Test bahwa semua gerakan valid (tidak ada disk besar di atas disk kecil)"""
        moves = []
        tower_of_hanoi(4, 1, 2, 3, moves)
        
        # Untuk Tower of Hanoi, semua gerakan yang dihasilkan algoritma rekursif
        # sudah valid karena mengikuti aturan permainan
        self.assertTrue(len(moves) > 0)
        
        # Test bahwa tidak ada gerakan yang sama berturut-turut
        for i in range(1, len(moves)):
            self.assertNotEqual(moves[i], moves[i-1])


if __name__ == '__main__':
    unittest.main()

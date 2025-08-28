import unittest
from palindrome_queries import palindrome_queries, is_palindrome


class TestPalindromeQueries(unittest.TestCase):
    
    def test_example_case(self):
        """Test kasus contoh dari soal"""
        n, m = 7, 5
        s = "aybabtu"
        operations = [
            (2, 3, 5),  # Query: cek substring dari pos 3-5
            (1, 3, 'x'),  # Update: ubah pos 3 menjadi 'x'
            (2, 3, 5),  # Query: cek substring dari pos 3-5
            (1, 5, 'x'),  # Update: ubah pos 5 menjadi 'x'
            (2, 3, 5)   # Query: cek substring dari pos 3-5
        ]
        
        result = palindrome_queries(n, m, s, operations)
        expected = [1, 0, 1]  # "bab" adalah palindrome, "bxb" bukan, "bxx" adalah
        self.assertEqual(result, expected)
    
    def test_single_character_palindrome(self):
        """Test palindrome dengan satu karakter"""
        s = "a"
        result = is_palindrome(s, 1, 1)
        self.assertTrue(result)
    
    def test_two_character_palindrome(self):
        """Test palindrome dengan dua karakter"""
        s = "aa"
        result = is_palindrome(s, 1, 2)
        self.assertTrue(result)
        
        s = "ab"
        result = is_palindrome(s, 1, 2)
        self.assertFalse(result)
    
    def test_longer_palindrome(self):
        """Test palindrome dengan string yang lebih panjang"""
        s = "racecar"
        result = is_palindrome(s, 1, 7)
        self.assertTrue(result)
        
        result = is_palindrome(s, 2, 6)
        self.assertTrue(result)
        
        result = is_palindrome(s, 1, 6)
        self.assertFalse(result)
    
    def test_multiple_updates_and_queries(self):
        """Test dengan multiple update dan query"""
        n, m = 5, 6
        s = "hello"
        operations = [
            (2, 1, 1),  # Query: 'h' -> True
            (1, 2, 'e'),  # Update: 'e' -> 'e' (no change)
            (2, 1, 2),  # Query: 'he' -> False
            (1, 1, 'e'),  # Update: 'h' -> 'e'
            (2, 1, 2),  # Query: 'ee' -> True
            (2, 1, 5)   # Query: 'eello' -> False
        ]
        
        result = palindrome_queries(n, m, s, operations)
        expected = [1, 0, 1, 0]
        self.assertEqual(result, expected)
    
    def test_edge_cases(self):
        """Test kasus edge"""
        # String kosong (tidak mungkin dalam constraint)
        # Test dengan string yang semua karakternya sama
        s = "aaaa"
        result = is_palindrome(s, 1, 4)
        self.assertTrue(result)
        
        # Test dengan string yang tidak ada yang sama
        s = "abcd"
        result = is_palindrome(s, 1, 4)
        self.assertFalse(result)
    
    def test_update_operations(self):
        """Test operasi update"""
        n, m = 3, 4
        s = "abc"
        operations = [
            (2, 1, 3),  # Query: 'abc' -> False
            (1, 1, 'c'),  # Update: 'a' -> 'c'
            (2, 1, 3),  # Query: 'cbc' -> True (palindrome)
            (1, 3, 'c'),  # Update: 'c' -> 'c' (no change)
            (2, 1, 3)   # Query: 'cbc' -> True (palindrome)
        ]
        
        result = palindrome_queries(n, m, s, operations)
        expected = [0, 1, 1]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

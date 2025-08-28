import unittest
from apartment_allocation import apartment_allocation


class TestApartmentAllocation(unittest.TestCase):
    
    def test_example_case(self):
        """Test kasus contoh dari soal"""
        n, m, k = 4, 3, 5
        applicants = [60, 45, 80, 60]
        apartments = [30, 60, 75]
        
        result = apartment_allocation(n, m, k, applicants, apartments)
        self.assertEqual(result, 2)
    
    def test_single_applicant_single_apartment(self):
        """Test dengan satu pelamar dan satu apartemen"""
        n, m, k = 1, 1, 5
        applicants = [50]
        apartments = [55]
        
        result = apartment_allocation(n, m, k, applicants, apartments)
        self.assertEqual(result, 1)
    
    def test_no_matching(self):
        """Test ketika tidak ada yang cocok"""
        n, m, k = 2, 2, 1
        applicants = [10, 20]
        apartments = [50, 60]
        
        result = apartment_allocation(n, m, k, applicants, apartments)
        self.assertEqual(result, 0)
    
    def test_all_matching(self):
        """Test ketika semua cocok"""
        n, m, k = 3, 3, 10
        applicants = [10, 20, 30]
        apartments = [15, 25, 35]
        
        result = apartment_allocation(n, m, k, applicants, apartments)
        self.assertEqual(result, 3)
    
    def test_more_applicants_than_apartments(self):
        """Test ketika pelamar lebih banyak dari apartemen"""
        n, m, k = 5, 3, 5
        applicants = [10, 20, 30, 40, 50]
        apartments = [15, 25, 35]
        
        result = apartment_allocation(n, m, k, applicants, apartments)
        self.assertEqual(result, 3)
    
    def test_more_apartments_than_applicants(self):
        """Test ketika apartemen lebih banyak dari pelamar"""
        n, m, k = 2, 5, 5
        applicants = [10, 20]
        apartments = [15, 25, 35, 45, 55]
        
        result = apartment_allocation(n, m, k, applicants, apartments)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()

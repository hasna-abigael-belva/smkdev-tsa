#!/usr/bin/env python3
"""
Script untuk menjalankan semua unit test untuk ketiga soal.
"""

import unittest
import sys
import os

# Tambahkan current directory ke Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def run_all_tests():
    """Menjalankan semua unit test"""
    # Import semua test modules
    from test_apartment_allocation import TestApartmentAllocation
    from test_tower_of_hanoi import TestTowerOfHanoi
    from test_palindrome_queries import TestPalindromeQueries
    
    # Buat test suite
    test_suite = unittest.TestSuite()
    
    # Tambahkan semua test cases
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApartmentAllocation))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTowerOfHanoi))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPalindromeQueries))
    
    # Jalankan test
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Tampilkan ringkasan
    print("\n" + "="*50)
    print("RINGKASAN TEST")
    print("="*50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    if result.wasSuccessful():
        print("\n✅ SEMUA TEST BERHASIL!")
        return 0
    else:
        print("\n❌ ADA TEST YANG GAGAL!")
        return 1


if __name__ == '__main__':
    exit_code = run_all_tests()
    sys.exit(exit_code)

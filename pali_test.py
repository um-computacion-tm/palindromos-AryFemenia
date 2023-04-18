import unittest
from palindrome import palindrome

#class TestFibo(unittest.Testcase):
#    def test1(self):
#        self.assertEqual(1, fibonacci(1))

class TestPalindromo(unittest.Testcase):
    def test_palindrome_simple(self):
        result = palindrome('neuquen')
        self.assertEqual(result, True)
    def test_palindrome_simple(self):
        result = palindrome('neuquen')
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()

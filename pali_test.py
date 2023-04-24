import unittest
from palindrome import palindrome

class TestPalindromo(unittest.TestCase):

    def test_palindrome_1(self):
        result = palindrome('neuquen')
        self.assertEqual(result, True)        

    def test_palindrome_2(self):
        result = palindrome('ala')
        self.assertEqual(result, True)

    def test_palindrome_3(self):
        result = palindrome('nadan')
        self.assertEqual(result, True)

    def test_palindrome_4(self):
        result = palindrome('ary')
        self.assertEqual(result, False)

    def test_palindrome_5(self):
        result = palindrome('otto')
        self.assertEqual(result, True)

    def test_palindrome_6(self):
        result = palindrome('electrocardiograma')
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()

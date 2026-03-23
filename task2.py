
import unittest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from string_utils import reverse_string, count_vowels, capitalize_words, is_palindrome, truncate


class TestReverseStringNormal(unittest.TestCase):

    def test_reverse_lowercase_word(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_uppercase_word(self):
        self.assertEqual(reverse_string("WORLD"), "DLROW")

    def test_reverse_mixed_case(self):
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_reverse_sentence(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_reverse_with_numbers(self):
        self.assertEqual(reverse_string("abc123"), "321cba")



class TestCountVowelsNormal(unittest.TestCase):

    def test_basic_word(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_sentence(self):
        self.assertEqual(count_vowels("unit testing"), 4)

    def test_uppercase_vowels(self):
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_mixed_case(self):
        self.assertEqual(count_vowels("Python"), 1)

    def test_string_with_numbers(self):
        self.assertEqual(count_vowels("a1e2i3"), 3)



class TestCapitalizeWordsNormal(unittest.TestCase):

    def test_lowercase_sentence(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")

    def test_single_word(self):
        """Single lowercase word should be capitalized"""
        self.assertEqual(capitalize_words("python"), "Python")

    def test_already_capitalized(self):
        """Already capitalized string should remain the same"""
        self.assertEqual(capitalize_words("Hello World"), "Hello World")

    def test_multiple_words(self):
        """Multiple words all get capitalized"""
        self.assertEqual(capitalize_words("unit testing in python"), "Unit Testing In Python")

    def test_word_with_numbers(self):
        """Numbers between words do not affect capitalization"""
        self.assertEqual(capitalize_words("unit 6 testing"), "Unit 6 Testing")



class TestIsPalindromeNormal(unittest.TestCase):

    def test_simple_palindrome(self):
        """Classic palindrome word"""
        self.assertTrue(is_palindrome("madam"))

    def test_not_a_palindrome(self):
        """Regular word that is not a palindrome"""
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_with_spaces(self):
        """Palindrome phrase ignoring spaces"""
        self.assertTrue(is_palindrome("race car"))

    def test_palindrome_case_insensitive(self):
        """Palindrome check should be case-insensitive"""
        self.assertTrue(is_palindrome("Madam"))

    def test_numeric_palindrome_string(self):
        """Numeric string that is a palindrome"""
        self.assertTrue(is_palindrome("12321"))


class TestTruncateNormal(unittest.TestCase):

    def test_truncate_long_string(self):
        """String longer than max_length should be cut and have '...' appended"""
        self.assertEqual(truncate("Hello, World!", 5), "Hello...")

    def test_string_shorter_than_max(self):
        """String shorter than max_length should be returned unchanged"""
        self.assertEqual(truncate("Hi", 10), "Hi")

    def test_string_equal_to_max(self):
        """String exactly at max_length should be returned unchanged"""
        self.assertEqual(truncate("Hello", 5), "Hello")

    def test_truncate_sentence(self):
        """Truncating a sentence to a few characters"""
        self.assertEqual(truncate("unit testing is fun", 4), "unit...")

    def test_truncate_preserves_start(self):
        """The beginning of the string should be preserved exactly"""
        self.assertEqual(truncate("Lahore, Pakistan!", 6), "Lahore...")


if __name__ == "__main__":
    unittest.main(verbosity=2)
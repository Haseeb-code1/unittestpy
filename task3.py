
import unittest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from string_utils import reverse_string, count_vowels, capitalize_words, is_palindrome, truncate


class TestReverseStringEdge(unittest.TestCase):

    def test_empty_string(self):
        """Empty string should return empty string"""
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        """Single character reversed is itself"""
        self.assertEqual(reverse_string("a"), "a")

    def test_palindrome_unchanged(self):
        """A palindrome reversed is the same string"""
        self.assertEqual(reverse_string("madam"), "madam")

    def test_whitespace_only(self):
        """A string of only spaces reversed stays the same"""
        self.assertEqual(reverse_string("   "), "   ")

    def test_special_characters(self):
        """Reversing special/punctuation characters"""
        self.assertEqual(reverse_string("!@#$"), "$#@!")

    def test_unicode_characters(self):
        """Reversing a string with unicode characters"""
        self.assertEqual(reverse_string("café"), "éfac")



class TestCountVowelsEdge(unittest.TestCase):

    def test_empty_string(self):
        """Empty string has zero vowels"""
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        """String with no vowels returns zero"""
        self.assertEqual(count_vowels("gym"), 0)

    def test_all_vowels(self):
        """String made entirely of vowels"""
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_spaces_only(self):
        """Spaces are not vowels"""
        self.assertEqual(count_vowels("   "), 0)

    def test_vowels_with_spaces(self):
        """Vowels separated by spaces are still counted"""
        self.assertEqual(count_vowels("  a  e  "), 2)

    def test_special_characters(self):
        """Special characters are not vowels"""
        self.assertEqual(count_vowels("!@#$"), 0)


class TestCapitalizeWordsEdge(unittest.TestCase):

    def test_empty_string(self):
        """Empty string should return empty string"""
        self.assertEqual(capitalize_words(""), "")

    def test_single_character(self):
        """Single character should be capitalized"""
        self.assertEqual(capitalize_words("a"), "A")

    def test_all_uppercase(self):
        """All uppercase string: title() lowercases after first letter"""
        self.assertEqual(capitalize_words("HELLO WORLD"), "Hello World")

    def test_spaces_only(self):
        """String of spaces should stay as spaces"""
        self.assertEqual(capitalize_words("   "), "   ")

    def test_mixed_spaces_words(self):
        """Extra spaces between words are preserved"""
        self.assertEqual(capitalize_words("hi  there"), "Hi  There")

    def test_special_characters(self):
        """Special characters at start of word are handled"""
        self.assertEqual(capitalize_words("!hello #world"), "!Hello #World")


class TestIsPalindromeEdge(unittest.TestCase):

    def test_empty_string(self):
        """Empty string is considered a palindrome"""
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        """A single character is always a palindrome"""
        self.assertTrue(is_palindrome("a"))

    def test_two_same_characters(self):
        """Two identical characters form a palindrome"""
        self.assertTrue(is_palindrome("aa"))

    def test_two_different_characters(self):
        """Two different characters are not a palindrome"""
        self.assertFalse(is_palindrome("ab"))

    def test_spaces_only(self):
        """Only spaces: after stripping spaces, empty string = palindrome"""
        self.assertTrue(is_palindrome("   "))

    def test_long_palindrome_phrase(self):
        """Long palindrome phrase with mixed case (spaces removed)"""
        self.assertTrue(is_palindrome("amanaplanacanalpanama"))


class TestTruncateEdge(unittest.TestCase):

    def test_empty_string(self):
        """Empty string should return empty string regardless of max_length"""
        self.assertEqual(truncate("", 5), "")

    def test_max_length_zero(self):
        """max_length of 0 should return only '...'"""
        self.assertEqual(truncate("Hello", 0), "...")

    def test_max_length_one(self):
        """max_length of 1 should return first character + '...'"""
        self.assertEqual(truncate("Hello", 1), "H...")

    def test_very_large_max_length(self):
        """Very large max_length should return string unchanged"""
        self.assertEqual(truncate("Hi", 1000), "Hi")

    def test_string_with_spaces_truncated(self):
        """Spaces within the string are counted toward length"""
        self.assertEqual(truncate("ab cd ef", 5), "ab cd...")

    def test_unicode_string(self):
        """Unicode characters should be truncated correctly"""
        self.assertEqual(truncate("café latte", 4), "café...")


if __name__ == "__main__":
    unittest.main(verbosity=2)
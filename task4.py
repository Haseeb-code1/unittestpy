
import unittest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from string_utils import reverse_string, count_vowels, capitalize_words, is_palindrome, truncate


class TestReverseStringError(unittest.TestCase):

    def test_none_raises_type_error(self):
        """None input should raise TypeError"""
        with self.assertRaises(TypeError):
            reverse_string(None)

    def test_integer_raises_type_error(self):
        """Integer input should raise TypeError"""
        with self.assertRaises(TypeError):
            reverse_string(123)

    def test_float_raises_type_error(self):
        """Float input should raise TypeError"""
        with self.assertRaises(TypeError):
            reverse_string(3.14)

    def test_list_raises_type_error(self):
        """List input should raise TypeError"""
        with self.assertRaises(TypeError):
            reverse_string(["a", "b"])

    def test_bool_raises_type_error(self):
        """Boolean input should raise TypeError"""
        with self.assertRaises(TypeError):
            reverse_string(True)


class TestCountVowelsError(unittest.TestCase):

    def test_none_raises_type_error(self):
        """None input should raise TypeError"""
        with self.assertRaises(TypeError):
            count_vowels(None)

    def test_integer_raises_type_error(self):
        """Integer input should raise TypeError"""
        with self.assertRaises(TypeError):
            count_vowels(42)

    def test_float_raises_type_error(self):
        """Float input should raise TypeError"""
        with self.assertRaises(TypeError):
            count_vowels(1.5)

    def test_list_raises_type_error(self):
        """List input should raise TypeError"""
        with self.assertRaises(TypeError):
            count_vowels(["a", "e", "i"])

    def test_dict_raises_type_error(self):
        """Dictionary input should raise TypeError"""
        with self.assertRaises(TypeError):
            count_vowels({"a": 1})


class TestCapitalizeWordsError(unittest.TestCase):

    def test_none_raises_type_error(self):
        """None input should raise TypeError"""
        with self.assertRaises(TypeError):
            capitalize_words(None)

    def test_integer_raises_type_error(self):
        """Integer input should raise TypeError"""
        with self.assertRaises(TypeError):
            capitalize_words(123)

    def test_float_raises_type_error(self):
        """Float input should raise TypeError"""
        with self.assertRaises(TypeError):
            capitalize_words(3.14)

    def test_list_raises_type_error(self):
        """List input should raise TypeError"""
        with self.assertRaises(TypeError):
            capitalize_words(["hello", "world"])

    def test_dict_raises_type_error(self):
        """Dictionary input should raise TypeError"""
        with self.assertRaises(TypeError):
            capitalize_words({"word": "hello"})


class TestIsPalindromeError(unittest.TestCase):

    def test_none_raises_type_error(self):
        """None input should raise TypeError"""
        with self.assertRaises(TypeError):
            is_palindrome(None)

    def test_integer_raises_type_error(self):
        """Integer input should raise TypeError"""
        with self.assertRaises(TypeError):
            is_palindrome(12321)

    def test_float_raises_type_error(self):
        """Float input should raise TypeError"""
        with self.assertRaises(TypeError):
            is_palindrome(1.1)

    def test_list_raises_type_error(self):
        """List input should raise TypeError"""
        with self.assertRaises(TypeError):
            is_palindrome(["m", "a", "d", "a", "m"])

    def test_bool_raises_type_error(self):
        """Boolean input should raise TypeError"""
        with self.assertRaises(TypeError):
            is_palindrome(False)


class TestTruncateError(unittest.TestCase):

    def test_none_string_raises_type_error(self):
        """None as string input should raise TypeError"""
        with self.assertRaises(TypeError):
            truncate(None, 5)

    def test_integer_string_raises_type_error(self):
        """Integer as string input should raise TypeError"""
        with self.assertRaises(TypeError):
            truncate(123, 5)

    def test_negative_max_length_raises_value_error(self):
        """Negative max_length should raise ValueError"""
        with self.assertRaises(ValueError):
            truncate("Hello", -1)

    def test_float_max_length_raises_value_error(self):
        """Float max_length should raise ValueError"""
        with self.assertRaises(ValueError):
            truncate("Hello", 3.5)

    def test_string_max_length_raises_value_error(self):
        """String as max_length should raise ValueError"""
        with self.assertRaises(ValueError):
            truncate("Hello", "five")

    def test_none_max_length_raises_value_error(self):
        """None as max_length should raise ValueError"""
        with self.assertRaises(ValueError):
            truncate("Hello", None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
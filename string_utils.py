
def reverse_string(s):

    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]


def count_vowels(s):

    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return sum(1 for ch in s.lower() if ch in "aeiou")


def capitalize_words(s):

    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s.title()


def is_palindrome(s):

    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def truncate(s, max_length):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if not isinstance(max_length, int) or max_length < 0:
        raise ValueError("max_length must be a non-negative integer")
    if len(s) <= max_length:
        return s
    return s[:max_length] + "..."
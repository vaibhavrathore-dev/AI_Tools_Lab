def is_palindrome(s):
    """
    Check whether the given string is a palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, otherwise False.
    """
    cleaned_string = s.lower().replace(" ", "")
    return cleaned_string == cleaned_string[::-1]


def count_words(text):
    """
    Count the number of words in the given text.

    Args:
        text (str): The input text.

    Returns:
        int: Number of words in the text.
    """
    return len(text.split())


def celsius_to_fahrenheit(c):
    """
    Convert Celsius temperature to Fahrenheit.

    Args:
        c (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return (c * 9 / 5) + 32


print(is_palindrome("Madam"))
print(count_words("Welcome to AI Tools Lab"))
print(celsius_to_fahrenheit(25))

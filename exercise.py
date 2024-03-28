import doctest


def get_squares(n: int) -> list:
    """
    Generates and returns a list of squares of the numbers from 1 to n.

    :param n: Upper limit of list.
    :return: List of squared integers.

    >>> get_squares(6)
    [1, 4, 9, 16, 25, 36]
    """

    return [i ** 2 for i in range(1, n + 1)]




def filter_even(l: list) -> list:
    """
    Filters even numbers in a list

    :param l: List of integers.
    :return: List of even elements in l.

    >>> filter_even([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
    [4, 16, 36, 64, 100]
    """
    return [x for x in l if x % 2 == 0]


def sum_even(l: list) -> int:
    """
    Calculates sum of the even numbers in a list.

    :param l: List of integers.
    :return: Sum of even elements in l.

    >>> sum_even([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
    220
    """
    result=0
    for i in l:
        if i%2==0:
            result+=i

    return result


def filter_less_than_n(l: list, n: int) -> list:
    """
    Filters elements of a list of numbers which are less than a given integer
    number.

    :param l: Input list.
    :param n: Integer number.
    :return: Filtered list.

    >>> filter_less_than_n([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 5)
    [1, 1, 2, 3]
    """
    return [i for i in l if i<n]


def remove_duplicates(l: list) -> list:
    """
    Returns a list with all elements of the input list without duplicates.

    :param l: Input list.
    :return: List of all elements of l list without duplicates.

    >>> remove_duplicates([1, 1, 2, 3, 5])
    [1, 2, 3, 5]
    """
    return list(set(l))


def common_elements(l1: list, l2: list) -> list:
    """
    Returns all common elements of two lists without duplicates.

    :param l1: First list.
    :param l2: Second list.
    :return: List of common elements.

    >>> common_elements([1, 2, 3, 5, 8, 21], [1, 2, 3, 7, 8, 9])
    [1, 2, 3, 8]
    """
    return [i for i in l1 if i in l2]



def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    """
    Merges two dictionaries, where values of overlapping keys are summed, e.g.,
    for {'a': 5, 'b': 3} and {'b': 2, 'c': 1}, the result should be
    {'a': 5, 'b': 5, 'c': 1}.

    :param dict1: First dictionary.
    :param dict2: Second dictionary.
    :return: Merged dictionary.

    >>> merge_dictionaries({'a': 5, 'b': 3}, {'b': 2, 'c': 1})
    {'a': 5, 'b': 5, 'c': 1}
    """

    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict



def first_and_last(l: list) -> tuple:
    """
    Returns the first and last element of a list.

    :param l: Non-empty list.
    :return: Tuple with first and last element of l.

    >>> first_and_last([1, 2, 3])
    (1, 3)
    """
    return (l[0], l[-1])


def fibonacci(n: int) -> int:
    """
    Return the n-th Fibonacci number. The Fibonacci numbers are defined as:
        - f(1) = 1
        - f(2) = 1
        - f(n) = f(n - 1) + f(n - 2) for n > 2

    :param n: Positive integer.
    :return: n-th Fibonacci number.

    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(7)
    13
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



def reverse_word_order(text: str) -> str:
    """
    Reverses the word order in a string of words.

    :param text: String with words.
    :return: String with words (separated by blanks) of text reversed.

    >>> reverse_word_order('hello world')
    'world hello'
    """
    words = text.split()  # Split the input string into a list of words
    reversed_text = ' '.join(reversed(words))  # Reverse the list of words and join them with spaces
    return reversed_text


def count_vowels(text: str) -> int:
    """
    Counts vowels (a, e, i, o, u) in a given string

    :param text: Text to check as string.
    :return: Number of vowels in text.

    >>> count_vowels('hello world')
    3
    """
    result=0
    for x in text:
        if x == 'a' or x=='e' or x=='i' or x=='o' or x=='u':
            result+=1

    return result


def check_palindrome(word: str) -> bool:
    """
    Checks if a given word is a palindrome (reads the same forwards as
    backwards).

    :param word: Word to check as string.
    :return: True if the word is a palindrome, else False.

    >>> check_palindrome("hello")
    False
    >>> check_palindrome("racecar")
    True
    """
    word = word.replace(" ", "").lower()
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return word == reversed_word


if __name__ == '__main__':
    doctest.testmod(verbose=True)
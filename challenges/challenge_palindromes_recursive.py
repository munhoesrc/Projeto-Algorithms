def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    # raise NotImplementedError
    if low_index is None and high_index is None:
        low_index = 0
        high_index = len(word) - 1

    if len(word) == 0:
        return False
    elif low_index >= high_index:
        return True
    elif word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

def merge_sort(string):
    if len(string) <= 1:
        return string

    meio = len(string) // 2
    esq = merge_sort(string[:meio])
    dir = merge_sort(string[meio:])
    return merge(esq, dir)


def merge(esq, dir):
    merged = ""
    esq_cursor, dir_cursor = 0, 0

    while esq_cursor < len(esq) and dir_cursor < len(dir):
        if esq[esq_cursor] < dir[dir_cursor]:
            merged += esq[esq_cursor]
            esq_cursor += 1
        else:
            merged += dir[dir_cursor]
            dir_cursor += 1

    merged += esq[esq_cursor:]
    merged += dir[dir_cursor:]

    return merged


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    # raise NotImplementedError
    if not first_string and not second_string:
        return (first_string, second_string, False)

    first_string = first_string.lower()
    second_string = second_string.lower()

    first_sorted = merge_sort(first_string)
    second_sorted = merge_sort(second_string)

    return (first_sorted, second_sorted, first_sorted == second_sorted)

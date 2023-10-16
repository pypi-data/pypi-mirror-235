def compute_prefix_table(pattern):
    m = len(pattern)
    prefix_table = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            prefix_table[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix_table[length - 1]
            else:
                prefix_table[i] = 0
                i += 1

    return prefix_table


def kmp(text: str, pattern: str):
    n, m = len(text), len(pattern)
    if m == 0:
        return []

    prefix_table = compute_prefix_table(pattern)
    matches = []
    i, j = 0, 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                matches.append(i - j)
                j = prefix_table[j - 1]
        else:
            if j != 0:
                j = prefix_table[j - 1]
            else:
                i += 1

    return matches

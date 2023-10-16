def boyer_moore(text, pattern):
    def build_bad_match_table(pattern):
        table = {}
        for i in range(len(pattern) - 1):
            table[pattern[i]] = len(pattern) - 1 - i
        return table

    def build_prefix_table(pattern):
        prefix_table = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[j] != pattern[i]:
                j = prefix_table[j - 1]
            if pattern[j] == pattern[i]:
                j += 1
            prefix_table[i] = j
        return prefix_table

    n, m = len(text), len(pattern)
    if m == 0:
        return []

    bad_match_table = build_bad_match_table(pattern)
    prefix_table = build_prefix_table(pattern)
    matches = []
    i = m - 1
    while i < n:
        j = m - 1
        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1
        if j == -1:
            matches.append(i + 1)
            i += m - prefix_table[0] + 1
        else:
            i += max(bad_match_table.get(text[i], m), m - j)
    return matches

def rabin_karp(text: str, pattern: str) -> list[int]:
    def calculate_hash(string: str):
        hash_value = 0
        for char in string:
            hash_value = (hash_value * prime + ord(char)) % modulus
        return hash_value

    def rehash(old_hash, old_char, new_char, pattern_length):
        new_hash = ((old_hash - ord(old_char) * high_power) * prime + ord(new_char)) % modulus
        if new_hash < 0:
            new_hash += modulus
        return new_hash

    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    prime = 101
    modulus = 10 ** 9 + 7
    high_power = pow(prime, m - 1, modulus)

    pattern_hash = calculate_hash(pattern)
    text_hash = calculate_hash(text[:m])

    matches = []

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                matches.append(i)

        if i < n - m:
            text_hash = rehash(text_hash, text[i], text[i + m], m)

    return matches

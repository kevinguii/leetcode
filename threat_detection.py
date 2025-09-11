def threat_detection(message):
    n = len(message)
    total_length = 0

    # Helper to expand around center
    def expand(left, right):
        nonlocal total_length
        while left >= 0 and right < n and message[left] == message[right]:
            length = right - left + 1
            if length >= 3:
                total_length += length
            left -= 1
            right += 1

    # Expand around each possible center
    for i in range(n):
        expand(i, i)       # Odd-length palindromes
        expand(i, i + 1)   # Even-length palindromes

    # Determine threat level
    if 1 <= total_length <= 10:
        return "Possible"
    elif 11 <= total_length <= 40:
        return "Probable"
    elif 41 <= total_length <= 150:
        return "Escalate"
    else:
        return "Ignore"

print(threat_detection("ababa"))  # Example usage
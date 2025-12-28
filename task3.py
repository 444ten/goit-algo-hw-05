import timeit

# 1. Boyer-Moore Algorithm
def build_shift_table(pattern):
    """Creates a table of shifts."""
    table = {}
    length = len(pattern)
    for i in range(length - 1):
        table[pattern[i]] = length - 1 - i
    return table

def boyer_moore_search(text, pattern):
    """
    Performs Boyer-Moore search.
    Returns the index of the first occurrence or -1 if not found.
    """
    shift_table = build_shift_table(pattern)
    n = len(text)
    m = len(pattern)
    i = 0

    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        
        if j < 0:
            return i  # Match found
        
        shift = shift_table.get(text[i + m - 1], m)
        i += shift
        
    return -1


# 2. Knuth-Morris-Pratt (KMP) Algorithm
def compute_lps(pattern):
    """
    Computes the Longest Prefix Suffix (LPS) array.
    Used to skip characters in KMP.
    """
    lps = [0] * len(pattern)
    length = 0
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """Performs KMP search using the LPS array."""
    M = len(pattern)
    N = len(text)
    lps = compute_lps(pattern)
    i = 0 # index for text
    j = 0 # index for pattern
    
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == M:
            return i - j # Match found
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


# 3. Rabin-Karp Algorithm
def rabin_karp_search(text, pattern):
    """Performs Rabin-Karp search using rolling hash."""
    d = 256
    q = 101
    M = len(pattern)
    N = len(text)
    p = 0
    t = 0
    h = 1

    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(N - M + 1):
        if p == t:
            if text[i:i + M] == pattern:
                return i
    
        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t = t + q
                
    return -1


def read_file(filename):
    """Helper to read file content with encoding handling."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        # Fallback for Windows-1251 if utf-8 fails
        with open(filename, 'r', encoding='cp1251') as f:
            return f.read()
    except FileNotFoundError:
        return None

if __name__ == '__main__':
    # 1. Load Texts
    text1 = read_file("text1.txt")
    text2 = read_file("text2.txt")
    
    if text1 is None or text2 is None:
        print("Error: Files 'text1.txt' or 'text2.txt' not found.")
        # Dummy data for testing if files are missing
        text1 = "This is a dummy text to test algorithms when files are missing."
        text2 = "Another dummy text for testing purposes."

    # 2. Define patterns (substrings)
    # "Existing" pattern should ideally be something present in the texts.
    # Change "algor" to a word that actually exists in your text files (e.g. "алгоритм")
    existing_pattern = "алгоритм" 
    fake_pattern = "nonexistent_substring_xyz"

    print(f"{'Algorithm':<20} | {'Text':<10} | {'Pattern':<15} | {'Time (sec)':<15}")
    print("-" * 70)

    # List of algorithms to test
    algorithms = [
        ("Boyer-Moore", boyer_moore_search),
        ("KMP", kmp_search),
        ("Rabin-Karp", rabin_karp_search)
    ]

    # Run tests
    for text_name, text_content in [("Article 1", text1), ("Article 2", text2)]:
        for pattern_type, pattern in [("Existing", existing_pattern), ("Fake", fake_pattern)]:
            for algo_name, algo_func in algorithms:
                
                # Measure execution time
                # number=100 means we run the search 100 times to get a stable average
                time_taken = timeit.timeit(lambda: algo_func(text_content, pattern), number=100)
                
                print(f"{algo_name:<20} | {text_name:<10} | {pattern_type:<15} | {time_taken:.5f}")
            print("-" * 70)
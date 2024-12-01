# https://cp-algorithms.com/string/string-hashing.html

def char_val(ch):
    return ord(ch) - ord('a') + 1

def string_hash(s):

    p = 31
    mod = 10 ** 9 + 9
    hash = 0
    power = 1
    n = len(s)

    for i in range(n):
        val = char_val(s[i])
        hash = (hash + val * power) % mod
        power = (power * p) % mod

    return hash


def rolling_hash(s, window):
    n = len(s)
    p = 31
    mod = 10 ** 9 + 9
    hash = 0
    power = p ** (window - 1)
    hashes = []

    for i in range(window):
        hash = (hash * p + char_val(s[i])) % mod
    hashes.append(hash)
    
    for i in range(window, n):
        hash -= (char_val(s[i - window]) * power + mod) % mod
        hash = (hash * p + char_val(s[i])) % mod
        hashes.append(hash)
    
    return hashes



if __name__ == '__main__':

    print(string_hash('cat'))

    print(rolling_hash('helloworld', 5))




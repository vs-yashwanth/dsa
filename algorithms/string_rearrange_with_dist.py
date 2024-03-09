from collections import Counter
import math

# Given a string and a number ‘K’, find if the string can be rearranged
# such that the same characters are at least ‘K’ distance apart from each other.


def rearrange(s, k):  # O(n)
    counts = Counter(s)

    most_freq = ''
    max_freq = 0
    for ch in counts:
        if counts[ch] > max_freq:
            max_freq = counts[ch]
            most_freq = ch

    if counts[most_freq] > math.ceil(len(s)/k):
        return '-1'

    filled = 0
    out = ['']*len(s)
    i = 0
    while i < len(s) and counts[most_freq] > 0:
        out[i] = most_freq
        counts[most_freq] -= 1
        i += k

    for ch in counts:
        while counts[ch] > 0:
            if i >= len(s):
                filled += 1
                i = filled
            out[i] = ch
            counts[ch] -= 1
            i += k

    return ''.join(out)


if __name__ == '__main__':

    print(rearrange("mmpp", 2))  # "mpmp" or "pmpm"
    print(rearrange('Programming', 3))  # "rgmPrgmiano" or a few more
    print(rearrange('abb', 2))  # 'aba'
    print(rearrange('aappa', 3))  # ''
    print(rearrange('aabbcc', 3))  # 'abcabc'
    print(rearrange('aaabc', 3))  # ''
    print(rearrange('aaadbbcc', 2))  # abacabcd
    print(rearrange('aaa', 2))  # ''

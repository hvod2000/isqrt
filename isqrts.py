from math import floor
from itertools import count


def isqrt_digit_by_digit(y):
    y = bytearray(y.to_bytes((y.bit_length() + 7) // 8, "little"))
    result, delta = 0, 0
    for i in range(len(y) * 8 - 2, -1, -2):
        delta, result = delta * 4 + ((y[i // 8] >> i % 8) & 3), result * 2
        if (new_delta := delta - (2 * result + 1)) >= 0:
            delta, result = new_delta, result + 1
    return result


def isqrt_dichotomy(x):
    x0, x2 = 0, 1
    while x2 ** 2 < x:
        x0, x2 = x2, x2 * 2
    while x0 != x2:
        x1 = (x0 + x2 + 1) // 2
        if x1 ** 2 > x:
            x2 = x1 - 1
        else:
            x0 = x1
    return x0


def isqrt_linear(y):
    for x in count():
        if y <= 0:
            return x
        y -= 3 + x * 2


def isqrt_jarvis(y):
    for x in count(1, 2):
        if y < x:
            return x // 2
        y -= x


def isqrt_newton(y):
    old_x, x = None, 1
    while x != old_x:
        old_x, x = x, (x + y // x) // 2
    return x


def isqrt_recursive(y):
    if not y:
        return 0
    x = isqrt_recursive(y // 4) * 2
    return x if ((x + 1) ** 2) > y else (x + 1)


def isqrt_dichotomy2(y):
    result = 0
    for shift in range(y.bit_length() // 2, -1, -1):
        result *= 2
        result += (result + 1) ** 2 <= y >> 2 * shift
    return result


def isqrt_wiki_bin_dgd(x):
    d = 2 ** x.bit_length()
    c = 0
    while d != 0:
        if x >= c + d:
            x -= c + d
            c = (c >> 1) + d
        else:
            c >>= 1
        d >>= 2
    return c


isqrts = {
    "simple digit-by-digit calculation": isqrt_digit_by_digit,
    "find square root by dichotomy": isqrt_dichotomy,
    "linear descending search": isqrt_linear,
    "Jarvis's algorithm": isqrt_jarvis,
    "Newton's method": isqrt_newton,
    "recursion on bits": isqrt_recursive,
    "digit-by-digit dichotomy": isqrt_dichotomy2,
    "binary digit-by-digit algorithm from wikipedia": isqrt_wiki_bin_dgd,
}

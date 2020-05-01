# Jibril Ali
# 2700 Lab 3

# 1. Compute gcd
def gcd(x, y):
    midd = y % x    # intermediate midd = y mod x

    if x > y:       # flip the numbers if needed
        return gcd(y, x)

    if midd == 0:   # found GCD
        return x
    else:           # recursive call to gcd
        return gcd(midd, x)

    return midd # return GCD

# 2. Compute modular inverse
def mod_inv(x, y):
    r_not = x; ri = y
    snot = 1; si = 0
    t_not = 0; ti = 1
    r = 1

    while r != 0:
        q = r_not // ri     # compute new quotient (int division)

        r = r_not % ri      # compute new remainder, assign to placeholder r
        r_not = ri; ri = r  # swap old remainder with current, and current with new

        s = snot - q*si     # compute new coefficient s
        snot = si; si = s   # swap old co-eff with current, and current with new

        t = t_not - q*ti    # compute new coefficient t
        t_not = ti; ti = t  # swap old co-eff with current, and current with new

    return snot % y

# 3. Compute modular exponentiation
def mod_exp(x, y, n):
    p = 1   # p tracks the partial result
    s = x   # s holds the current value of x^(2^j)
    r = y   # r is used to help compute the binary expansion of y

    while r > 0:
        if r % 2 == 1:      # if r/2 has a remainder, i.e. if bit j = 1
            p = p * s % n   # if the bit is 1, multiply p by x^2, then mod n
        s = s * s % n       # square s, then mod n
        r = r // 2          # get ready to compute the next bit of r in base 2

    return p

# 4. 


if __name__ == '__main__':
    test = gcd(462, 1071)
    print(test)
    print(mod_inv(52, 77))
    print(mod_exp(7, 64, 2399))
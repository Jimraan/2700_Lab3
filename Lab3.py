# Jibril Ali
# 2700 Lab 3

# 1. Compute gcd
def gcd(x, y):
    midd = y % x

    if x > y:   # flip the numbers if needed
        return gcd(y, x)

    if midd == 0: # found GCD
        return x
    else:
        return gcd(midd, x) # recursive call to gcd

    return midd # return GCD

# 2. Compute modular inverse
def mod_inv(x, y):
    # r_not = x; ri = y
    # snot = 1; si = 0
    # t_not = 0; ti = 1
    i = 1

    while ((i*x) % y) != 1 and i < y - 1:
        i += 1
        # q = r_not // ri # quotient
        #
        # r = r_not; r_not = ri
        # ri = r // ri # remainder
        #
        # s = snot; snot = si
        # si = s - q*si
        #
        # t = t_not; tnot = ti
        # ti = t - q*ti

    return i

# 3. Compute modular exponentiation
def mod_exp(x, y, n):
    p = 1; s = x; r = y;

    while r > 0:
        if r % 2 == 1:
            p = p * s % n
        s = s * s % n
        r = r // 2

    return p


if __name__ == '__main__':
    test = gcd(462, 1071)
    print(test)
    print(mod_inv(52, 77))
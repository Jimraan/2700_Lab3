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

    return midd     # return GCD

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

    return snot % y         # return MI mod y of x

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

    return p                # return the modular exponentiation, x^y mod n

# 4. Generate RSA Keys
def generate_RSA_keys(p, q):
    key = [0, 0, 0]           # list that will hold key values
    n = p * q           # compute n
    phi = (p-1) * (q-1) # compute phi
    e = 3               # use this to find M.I.

    while gcd(phi, e) != 1 :
        e += 2   # increment e while it's not relatively prime with phi

    d = mod_inv(e, phi) # use our function to compute mod inv of e mod phi

    key[0] = n; key[1] = e; key[2] = d   # assign the values to the key list

    return key          # return the list of key values


if __name__ == '__main__':
    input("(press enter to continue)")
    input("Slake: Finally, you're here. ")
    input("Slake: They're getting ready to wipe the systems, ")
    input("so let's make this quick before the feds get on us. Ramona?")

    x = int(input("\nRamona: Spice, you should've gotten two primes from Maslothsri. Type in the first: "))
    y = int(input("Ramona: And the second: "))

    key = generate_RSA_keys(x, y)
    N = key[0]; e = key[1]; d = key[2]

    print("[[:***RSA KEY GENERATION SUCCESSFUL]]"
          "\n[[ Public Key: (" + str(N) + ", " + str(e) + ")   Private Key: (" + str(d) + ") ]]")
    input()
    input("Ramona: Alright, that worked. Keys are generated.")
    input("Slake: We can encrypt any message now... too bad all this will be gone in minutes...")
    input("*sniff* Anyway... we need to tell Kriangsari to send lifeboats and okay launch.)")
    input("Way too many bluecoats for us out there.")

    m = int(input("\nSlake: Maslothsri gave you those digit patterns, right? Send 'em off: "))
    c = mod_exp(m, e) % N

    input("\n[[:***ENCRYPTION SUCCESSFUL]] " + str(c))
    input("Well... I guess that's that. "
          "Now we wipe these systems and wait for Kria▀▀▀Σ9**16291<╟╟---MEMORY__REDACTED]]]")

    input("\n\n\n\n"
          "(somewhere on a nearby moon...)")
    input("\n***TRANSMISSION RECEIVED]]")
    input("Kriangsari: Flash? Is that Slake's team?")
    input("Flash (slow): Juicing..... up..... *whirrrr*")
    input("Flash (sprightly): It's Slake, Captain K. The message is encrypted, I need to send it to Priscilla")
    input("Priscilla (sprightly): *whirrrr* Already on it, Flash. Retrieving decryption key! *klik, beep*")
    input("[[RETRIEVAL SUCCESSFUL: " + str(d) + "]]")

    input("Priscilla (sprightly): Decrypting now!")

    message = mod_exp(c, d) % N

    input("\n...\n[[:***DECRYPTION SUCCESSFUL]]" + str(message))
    input("\nKriangsari: That's a lifeboat code... and launch request...")
    input("Kriangsari: Speedy, send boats to pick up Slake's team. Alacrity, launch N-55's in 6 minutes!")
    input("Speedy & Alacrity (sprightly): Aye aye, captain!")
    input("Kriangsari: Flash, Priscilla, both of you can drop. Can't have you juiced for too long")
    input("Flash & Priscilla (slow): *bwoooo* Aye..... Captain.")
    input("\n(As Kriangsari prepares for the worse, Slake's team awaits their rescue...)")

    print("\n\n\n\n//End chapter: Inside Job")

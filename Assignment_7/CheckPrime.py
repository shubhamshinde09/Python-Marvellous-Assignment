def ChkPrime(no):
    if no <= 1:
        return False
    for n in range(2,no):
        if no % n == 0:
            return False
        if no == 2:
            return True
    return True
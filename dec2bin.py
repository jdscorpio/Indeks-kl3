def dec2bin(dec):
    if dec == 0:
        return '0'
    bin = ''
    while dec > 0:
        if dec % 2 == 0:
            bin = '0' + bin
        else:
            bin = '1' + bin
        dec //= 2
    return bin

def dec2bin_rep8(dec):
    bin = dec2bin(dec)
    n = len(bin)
    for i in range(8-n):
        bin = '0' + bin
    return bin

def dec2bin_rep_bit(dec):
    bin = dec2bin(dec)
    n = len(bin)
    if dec < 255:
        rep = 8
    elif dec < 2**16-1:
        rep = 16
    elif dec < 2**24-1:
        rep = 24
    elif dec < 2**32-1:
        rep = 32
    else:
        rep = 64
    for i in range(rep-n):
        bin = '0' + bin
    return bin


print(dec2bin(23))
print(dec2bin_rep8(23))
print(dec2bin(0))
print(dec2bin_rep8(0))
print(dec2bin(323))
print(dec2bin_rep8(323))
print(dec2bin_rep_bit(2**45))
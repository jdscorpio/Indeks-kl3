def b2d_calk(bin:str)->int:
    bin = bin[::-1]
    wynik = 0
    potega2 = 1
    for i in range(len(bin)-1):
        wynik += int(bin[i])*potega2
        potega2 *= 2
    
    return wynik + int(bin[7])*(-128)

def b2d_ulam(bin:str)->float:
    wynik = 0
    potega2 = 0.5
    for i in range(len(bin)):
        wynik += int(bin[i])*potega2
        potega2 *= 0.5
    return wynik

def bin2dec(bin:str)->float:
    bin = bin.split('.')
    cz_calk = bin[0]
    cz_ulam = bin[1]
    if b2d_calk(cz_calk) > 0:
        wynik = b2d_calk(cz_calk) + b2d_ulam(cz_ulam)
    else:
        wynik = b2d_calk(cz_calk) - b2d_ulam(cz_ulam)
    return wynik

print(bin2dec('00001011.1011'))
#print(b2d_calk('00001011'), b2d_ulam('1011'))
print(bin2dec('10001011.1011'))
#print(b2d_calk('10001011'), b2d_ulam('1011'))


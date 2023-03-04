def u2bin2dec(bin:str)->int:
    bin = bin[::-1]
    wynik = 0
    potega2 = 1
    for i in range(len(bin)-1):
        wynik += int(bin[i])*potega2
        potega2 *= 2
    
    return wynik + int(bin[7])*(-128)

bin = input("Podaj liczbę dwójkową w U2: ")
print(u2bin2dec(bin))
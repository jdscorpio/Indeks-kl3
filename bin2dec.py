def bin2dec(bin:str)->int:
    bin = bin[::-1]
    wynik = 0
    potega2 = 1
    for i in range(len(bin)):
        wynik += int(bin[i])*potega2
        potega2 *= 2
    
    return wynik

bin = input("Podaj liczbę dwójkową: ")
print(bin2dec(bin))
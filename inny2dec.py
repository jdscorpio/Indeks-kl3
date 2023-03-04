def inny2dec(inny:str, baza:int)->int:
    inny = inny[::-1]
    wynik = 0
    potega = 1
    for i in range(len(inny)):
        wynik += int(inny[i])*potega
        potega *= baza
    
    return wynik

baza = int(input("Podaj podstawę: "))
inny = input("Podaj liczbę: ")
print(inny2dec(inny,baza))
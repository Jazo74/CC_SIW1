x = 1
y = 0
z = 0
Maxlenght = 0
ActualLenght = 0
Space = " "
lista = []
Szam = 0
Szam = int(input("Szam?: "))
for i in range(Szam):
    lista.append(z)
    z = x + y
    x = y
    y = z
MaxLenght = len(str(lista[Szam-1])) + len(str(Szam))
print(MaxLenght)
for i in range(Szam):
    ActualLenght = len(str(lista[i]))
    Space = (MaxLenght - ActualLenght - (len(str(i+1)))) * " "
    print(str(i+1) + ". " + Space + str(lista[i]))
    


a = 0
b = 0
muvelet = ""
outp = 0
try:
    a = int(input("Kerem az elso szamot(vagy egy betut a kilepeshez): "))
except ValueError:
    pass
else:
    muvelet = input("Mi legyen a muvelet: ")
    b = int(input("Kerem a masodik szamot: "))
    if muvelet == "+":
        outp = a + b
    elif muvelet == "-":
        outp = a - b
    elif muvelet == "*":
        outp = a * b
    elif muvelet == "/":
        outp = a / b
    print("Az eredmeny = " + str(outp))
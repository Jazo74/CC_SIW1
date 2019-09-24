import sys
Nev = ""
try:
    Nev = sys.argv[1]
except IndexError:
    Nev = "World"
print(Nev)
print("Hello " + Nev + "!")
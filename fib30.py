x = 1
y = 0
z = 0
for i in range(30):
    print(str(i+1) + ". " + str(z))
    z = x + y
    x = y
    y = z
import sys
First = int(sys.argv[1])
Second = int(sys.argv[2])
Divider = 0
Count = 0
if First < Second:
    Divider = First
else:
    Divider = Second
for i in range(Divider,1,-1):
    if Count == 1:
        break
    if  First % i == 0 and Second % i == 0:
        print("The biggest common divider: "+ str(i))
        Count = 1
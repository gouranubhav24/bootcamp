import math
x = float(input("enter the kms "))
total = 0
base = 35
if x <=1.5:
    total = base
else:
    nob=x-1.5
    if nob > int(nob):
        total = (int(nob)+1)*25+base
    else:
        total = (nob)*25+base

    
    
print('rs ', total)
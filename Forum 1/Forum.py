import math
from fractions import Fraction

num= int(input("Enter a numerator: "))
while True:
    if (num>0):
        break
    else:
        num= int(input("Numerator must be > 0 integer. Please enter another number : "))
        continue

den= int(input("Enter a denominator: "))
while True:
    if (den>0):
        break
    else:
        den= int(input("Denominator must be > 0 integer. Please enter another number : "))
        continue

#Formula
gcd= math.gcd(num,den)
x= (num//den)
y= num%den
numgcd= num//gcd
dengcd = den//gcd
gcdnumden = math.gcd(numgcd,dengcd)

#Proper, whether reduce
while True:
    if (num<den):
        print(num,"/",den, "is a proper fraction.")
        if gcd>1:
            print("This proper fraction can be reduced: ",Fraction(num,den))
            break   
        else:
            print("This proper fraction cannot be reduced any further.")
            break
#Improper,mixed, whole, whether reduce
    if (num>den):
        print(num,"/",den, "is a improper fraction.")
        if gcd==1 and den>1:
            print("This improper fraction cannot be reduced any further.")
            print("The mixed number is ",x,"and", y,"/",den)
            break
        if gcd==1:  
            print("This improper fraction cannot be reduced any further.")
            print("The whole number is ",x)
            break
        if gcdnumden==1 and dengcd>1:
            print("This improper fraction can be reduced to: ",Fraction(num,den))
            print("The mixed number is ",x,"and",numgcd-(x*dengcd),"/",(dengcd))
            break
        else: 
            print("The improper fraction can be reduced further to become: ",numgcd,"/",(dengcd),"the whole number is ",x)
            break
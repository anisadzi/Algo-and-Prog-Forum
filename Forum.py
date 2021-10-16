import math
from fractions import Fraction

#insert a numerator
num= int(input("Enter a numerator: "))
while True:
    if (num>0):
        break
    else:
        num= int(input("Numerator must be > 0 integer. Please enter another number : "))
        continue
#insert a denominator
den= int(input("Enter a Denominator: "))
while True:
    if (den>0):
        break
    else:
        den= int(input("Denominator must be > 0 integer. Please enter another number : "))
        continue
#math modules used
gcd= math.gcd(num,den)
w= (num//den)
r= num%den
numgcd= num//gcd
dgcd = den//gcd
gcdnd = math.gcd(numgcd,dgcd)

#If it is a Proper fraction + can be reduced or not
while True:
    if (num<den):
        print(num,"/",den, "is a proper fraction.")
        if gcd>1:
            print("This proper fraction can be reduced: ",Fraction(num,den))
            break   
        else:
            print("This proper fraction cannot be reduced any further.")
            break
#If it is an improper fraction + mixed number + whole number + can be reduced or not
    if (num>den):
        print(num,"/",den, "is a improper fraction.")
        if gcd==1 and den>1:
            print("This improper fraction cannot be reduced any further.")
            print("The mixed number is ",w,"and", r,"/",den)
            break
        if gcd==1:  
            print("This improper fraction cannot be reduced any further.")
            print("The whole number is ",w)
            break
        if gcdnd==1 and dgcd>1:
            print("This improper fraction can be reduced to: ",Fraction(num,den))
            print("The mixed number is ",w,"and",numgcd-(w*dgcd),"/",(dgcd))
            break
        else: 
            print("The improper fraction can be reduced further to become: ",numgcd,"/",(dgcd),"the whole number is ",w)
            break
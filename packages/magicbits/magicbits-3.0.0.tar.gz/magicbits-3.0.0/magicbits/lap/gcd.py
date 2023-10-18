def gcd(a,b): 
    if (b == 0): 
            return a 
    return gcd(b, a%b) 
a = int(input("Enter the value of first number :- "))
b = int(input("Enter the value of second number :- "))
if(gcd(a, b)): 
    print(f'GCD of {a} and {b} is: {gcd(a, b)}') 
else: 
    print('Not found')

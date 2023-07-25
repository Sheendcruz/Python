def gmean(a,b):
    sol=((a*b)/(a+b))
    print("Your solution is: ",sol)
def compare(a,b) :   
    if (a>b):
        print("first number: ",a, "is greater than b: " ,b)
    elif (a<b):
        print("first number: ",a, "is smaller than b: " ,b)
    else:
        print("first number: ",a, "is equal to b: " ,b)
c=int(input("Enter the first number"))    
d=int(input("Enter the second number"))  
gmean(c,d)
compare(c,d)

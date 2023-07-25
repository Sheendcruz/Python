import time
t= time.strftime('%H:%M:%S')
print(t)
a= int(time.strftime('%H'))
print(a)
b= time.strftime('%M')
print(b)
c= time.strftime('%S')
print(c)
if (a<=12):
    print("GOOD MORNING")
elif (12<=a<=4):  
    print("GOOD AFTERNOON")
else :
    print ("GOOD EVENING")  
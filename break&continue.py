for i in range(20):
    if(i==10):
        print("we stop once i becomes 10")
        break
    
    print("20 X " ,i,"=" ,20*(i+1))
    
for i in range(20):
    if(i==10):
        print("we just skip the iteration where i becomes 10")
        continue
    
    print("20 X " ,i,"=" ,20*(i+1))
    
x=1
while(x<20):
    x=x+1
    if(x==10):
        print("we stop once i becomes 10")
        break 
    print("20 X " ,x,"=" ,20*(x+1))    
x=1
while(x<20):
    x=x+1
    if(x==10):
        print("we just skip the iteration where i becomes 10")
        continue
    print("20 X " ,x,"=" ,20*(x+1))     
       
       
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break
    
    
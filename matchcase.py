x= int(input("Enter your age:"))

match (x):
     case 1:
          print("NOT ALLOWED TO VOTE")

     case _ if(x>18):
           print("ALLOWED TO VOTE")

x1=float(input("Enter Value: "))
x2=str(input("Enter unit A(Centigrade) or B(Fahrenhiet):  "))
if x2!="A" and x2 != "B" :
   print("Error")
elif x2=="A":
    print( "the Value in Centigrade is: " + str((x1 - 32)*.5556))
elif x2=="B":
    print( "the Value in Fahrenhiet is: " + str((x1*1.8) + 32))
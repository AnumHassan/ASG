x1=float(input("Enter Value: "))
x2=str(input("Enter unit A(Feet) or B(Inches):  "))
if x2!="A" and x2 != "B" :
   print("Error")
elif x2=="A":
    print( "the Value in Centimeter is: " + str(x1*30.28))
elif x2=="B":
    print( "the Value in Centimeter is: " + str(x1*2.54))
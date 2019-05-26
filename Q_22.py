x1=float(input("Enter  Values of Mass: "))
x2=float(input("Enter Values of Height : "))
x3=str(input("Enter unit A(kg,M) or B(lb,Inch):  "))
if x3!="A" and x3 != "B" :
   print("Error")
elif x3=="A":
    print( "the BMI is: " + str(x1/(x2*x2)))
elif x3=="B":
   print( "the BMI is: " + str(x1/((x2*x2)*703)))
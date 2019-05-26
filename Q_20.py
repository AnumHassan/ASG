x1=float(input("Enter Value: "))
x2=str(input("Enter unit A(Hours) or B(Minutes):  "))
if x2!="A" and x2 != "B" :
   print("Error")
elif x2=="A":
    print( "the Value in Second is: " + str(x1*60*60))
elif x2=="B":
    print( "the Value in Second is: " + str(x1*60))
Dividend=float(input(" Enter a Dividend No :   " ))
Divisor=float(input(" Enter a Divisor No :   " ))
if Divisor==0:
    print("Error")
    Divisor=float(input(" Enter a Dividend No :   " ))
else:
    Rem= int(Dividend%Divisor)
    if Rem==0:
        print("Nos are divisable")
    else:
        print("Nos are not divisable")
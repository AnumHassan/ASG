St=(input(" Enter an Alphabet:  " ))
if len(St)>= 2:
    print ( "Error")
elif St=="1" or St=="2" or St=="3" or St=="4" or St=="5" or St=="6" or St=="9" or St=="8" or St=="9" or St=="0":
    print ( St + " is not an alphabet")
elif St=="a " or St=="e " or St=="i "or St=="o" or St=="u"or St=="A " or St=="E " or St=="I "or St=="O" or St=="U":
  print ( St + " is Vowel") 
else:
 print ( St + " is consonant") 
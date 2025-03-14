a = float(input("your weight/kg:"))
b = float(input("your height/m:"))
c = b**2
d = a / c
#The value of "d" is calculated by dividing the value of "a" by the square of the value of "b".
if d < 18.5 :
    print("underweight")
#The value of "d" is less than 18.5, so the string "underweight" is printed.
if d > 30 :
    print("obese")
#The value of "d" is greater than 30, so the string "obese" is printed.
else :
    print("normal weight")
#The value of "d" is not less than 18.5 and not greater than 30, so the string "normal weight" is printed.

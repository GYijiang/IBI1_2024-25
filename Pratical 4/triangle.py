a = 1
#"a" is a vairble. Its initial value is 1.
sum = 0
#"sum" is a variable. Its initial value is 0. It is used to store the sum of the numbers (accumulator).
for i in range(1,10):
#The range() function returns a sequence of numbers, starting from 1 by default, and increments by 1 (by default), and stops before a specified number.
    sum = a + sum
#The value of "a" is added to the value of "sum" and stored in the variable "sum".
    a = a + 1
#The value of "a" is incremented by 1.
    print(sum,end=" ")
#The value of "sum" is printed.
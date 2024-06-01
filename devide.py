num1=0
num2=0

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

if(num1>num2):
    quotient=num1/num2
    remainder=num1%num2
    
else:
    quotient=num2/num1
    remainder=num2%num1
    
print("quotient=", "{:.2f}".format(quotient))
print("remainder=","{:.2f}".format(remainder))
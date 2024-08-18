operations=input("enter your operations (+,-,*,/): ")
a=float(input("enter the no.1: "))
b=float(input("enter the no.2: "))
if operations=="+":
    result=a+b
    print(result)
elif operations=="-":
    result=a-b
    print(result)
elif operations=="*":
    result=a*b
    print(result)
elif operations=="/":
    result=a/b
    print(result)
else:
    print(f"{operations} is invalid")        


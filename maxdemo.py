no1=int(input("Enter the first number:"))
no2=int(input("Enter the second number:"))
no3=int(input("Enter the Third Number:"))

if no1>0 and no2>0 and no3>0:
    if no1>no2 and no1>no3:
        print("The first number is greater than the second number.")
    elif no2>no1 and no2>no3 :
        print("The second number is greater than the first number.")
    else :
        print("The Third number is a maximum")
else :
    print("Nagetive input are not allowed.")

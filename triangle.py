a = float(input("Enter the first angle1: "))
b = float(input("Enter the second angle2: "))
c = float(input("Enter the third angle3: "))
sum=a+b+c
if (sum==180) and (a>0) and (b>0) and (c>0):
    
    print("The angles can form a triangle.")
else:
    print("The angles cannot form a triangle.")
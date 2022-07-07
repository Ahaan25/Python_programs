import math
hex_value=input("Please Enter Hexadecimal Number: ")
print(hex_value);
#conversion
n=int(hex_value, 16)
binaryStr=''
while n>0:
    binaryStr=str(n%2)+binaryStr
    n=n>>1
result=binaryStr
print("Equivalent Binary Number is: " , str(result))
temp=int(input("Enter temperature in °C: "))
if temp<-273.15:
    print("Temperature is invalid")
elif temp==-273.15:
    print("Temperature is absolute zero")
elif -273.15<=temp<=0:
    print("Temperature is below freezing point")
elif temp==0:
    print("Temperature is at the freezing point")
elif 0<=temp<=100:
    print("Temperature is in normal range")
elif temp==100:
    print("Temperature is at boiling point")
elif temp>100:
    print("Temperature is above boiling point")
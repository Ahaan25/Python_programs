year=input("Enter year: ")
month=input("Enter month(number): ")
day=0
if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    day=31
elif(month==4 or month==6 or month==9 or month==11):
    day=30
elif((month==2) and (year%4==0)):
    day=29
elif(month==2):
    day=28
else: print("Invalid month count. Enter a number between 1 to 12")
print("The number of days in the month are: ",str(day))
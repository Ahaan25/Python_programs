string1=input("Enter the first string: ")
string2=input("Enter the second string: ")
def mergealternate(string1, string2):
   i=0
   j=0
   result=""
   while i<len(string1) and j<len(string2):
      result+=string1[i]+string2[j]
      i+=1
      j+=1
   while i<len(string1):
      result+=string1[i]
      i+=1
   while j<len(string2):
      result+=string2[j]
      j+=1
   return result
print(mergealternate(string1, string2))
if len(string1)!=len(string2):
    print("They are not of the same length.")
    exit()
else:
    mergealternate(string1, string2)
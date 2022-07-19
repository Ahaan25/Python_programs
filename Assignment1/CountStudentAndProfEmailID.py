no_of_lines=int(input("Enter number of inputs: "))
lines=""
for i in range(no_of_lines):
    lines+=input()+"\n"
if lines.endswith('@student.college.edu'):
    print("All emails entered are student email IDs")
else:
    print("There are some professor email IDs entered.")
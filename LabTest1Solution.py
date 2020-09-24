import string

#program to make pascals triangle

#Jade Brennan-Keane
#C18512336

def make_new_row(old_row):
    #declaring variables
    new_row = [1]
    i = 0
    length = len(old_row)
    length = length - 1
	
    #allow for special case of the first line
    if old_row == []:
        return [1]
    #allow for special case of the second line
    elif old_row == [1]:
        return [1,1]
    
    #make new rows
    while i in range (0, length):
        x = old_row[i]
        y = old_row[i + 1]
        z = x + y
        new_row.append(z)
        i = i + 1

    new_row.append(1)
    return new_row


#declaring variables
old_row = []
L = []
inp, i = 0, 0

#ask user to input height
inp = input("How many lines will the triangle be? : ")
height_of_tri = int(inp)

while i < height_of_tri:
	#call make_new_row function
	old_row = make_new_row(old_row)
	L.append(old_row)
	i = i + 1

print("List of lists : ")
print(L)
print("")

i = 0

print("Each list on different line : ")
for i in L:
    print(i)
print("")

i = 0

print("The Triangle:")
for i in L:
    row = ' '.join([str(j) for j in i])
    print(row.center(100))
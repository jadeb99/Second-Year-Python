import string

#program to make pascals triangle

#Jade Brennan-Keane
#C18512336

def make_new_row(old_row):
	#declaring variables
	new_row = [1]
	i = 0
	j = 1
	
	#allow for special case of the first line
	if old_row == []:
		return [1]
	#allow for special case of the second line
	elif old_row == [1]:
		return [1,1]
	
	#make new rows
	while i in range(len(old_row)):
		x = old_row[i]
		
		while j in range(len(old_row)):
			y = old_row[j]
			z = x + y
			new_row.append(z)
			j = j + 1
		
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

print("Each list on different line : ")
print(L)
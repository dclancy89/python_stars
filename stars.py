def stars(arr):
	for x in arr:
		output = ""

		#check the type of the list value
		if type(x) is int:
			for i in range(x):
				output += "*"
			print output
		elif type(x) is str:
			for i in range(len(x)):
				output += x[0].lower()
			print output

x = [4,6,1,3,5,7,25]

stars(x)

print ""
print ""
print ""

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

stars(x)

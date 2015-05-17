core_in=open("core_substance.csv", "r")
imputed_in=open("imputed_substance.csv", "r")
selected_in=open("selected_unedited.csv", "r")
non_in=open("non_core.csv", "r")
demographics_in=open("demographics.csv", "r")
geographic_in=open("geographic.csv", "r")

core_out=open("core_substance2.csv", "wb")
imputed_out=open("imputed_substance2.csv", "wb")
selected_out=open("selected_unedited2.csv", "wb")
non_out=open("non_core2.csv", "wb")
demographics_out=open("demographics2.csv", "wb")
geographic_out=open("geographic2.csv", "wb")

count=0
first=core_in.readline()
first="ID, " + first
core_out.write(first)
for line in core_in:
	core_out.write(str(count) + ", " + line)
	count+=1
	
count=0
first=imputed_in.readline()
first="ID, " + first
imputed_out.write(first)
for line in imputed_in:
	imputed_out.write(str(count) + ", " + line)
	count+=1
	
count=0
first=selected_in.readline()
first="ID, " + first
selected_out.write(first)
for line in selected_in:
	selected_out.write(str(count) + ", " + line)
	count+=1
	
count=0
first=non_in.readline()
first="ID, " + first
non_out.write(first)
for line in non_in:
	non_out.write(str(count) + ", " + line)
	count+=1
	
count=0
first=demographics_in.readline()
first="ID, " + first
demographics_out.write(first)
for line in demographics_in:
	demographics_out.write(str(count) + ", " + line)
	count+=1
	
count=0
first=geographic_in.readline()
first="ID, " + first
geographic_out.write(first)
for line in geographic_in:
	geographic_out.write(str(count) + ", " + line)
	count+=1



def diff(a, b):
    b = set(b)
    return [aa for aa in a if aa not in b]

non_in=open("non_core2.csv", "r")
non_in2=open("non_core2.csv", "r")
non_cols_to_keep=open("noncore_cols_to_keep.txt", "r")
non_out=open("non_core3.csv", "wb")

vars_to_keep=[]
indexes_to_keep=[]

for line in non_cols_to_keep:
	vars_to_keep.append(line.rstrip('\n'))
	
first=non_in.readline().split()
first2=[]

for x in first:
	first2.append(x.replace(',', ''))
	
indexes_to_keep.append(0)
for x in vars_to_keep:
	indexes_to_keep.append(first2.index(x))

all_indexes=range(len(first2))
print len(all_indexes)

indexes_to_delete = diff(all_indexes,indexes_to_keep)

for line in non_in2:
	temp=line.split()
	for x in indexes_to_delete:
		temp[x]=''
	#non_out.write(''.join(temp))
	non_out.write("".join(str(e) for e in temp)[:-1])
	non_out.write("\n")
	

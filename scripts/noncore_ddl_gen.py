non_in=open("non_core3.csv", "r")
non_out=open("non_core3.ddl", "wb")

first=non_in.readline()
vars=first.split(',')
vars[-1]=vars[-1].rstrip('\n')

for x in vars:
	non_out.write(x + "XXXX NUMBER, \n")
#Core Substance Abuse CIGEVER-SVDAYPWK	2 	354
#Imputed Substance Use IRCIGRC-FUIEM21	355		850
#Selected Unedited Variables CG05-SV13	851		964
#Non-core HERSMOKE-GQTYPE2	965		3056
#Demographics AGE2-II2EMST4		3057	3134
#Geographic PDEN00-MAIIN002		3135	3137

core_substance=""
imputed_substance=""
selected_unedited=""
non_core=""
demographics=""
geographic=""

infile=open("2013Data.tsv", "r")
core_out=open("core_substance.csv", "wb")
imputed_out=open("imputed_substance.csv", "wb")
selected_out=open("selected_unedited.csv", "wb")
non_out=open("non_core.csv", "wb")
demographics_out=open("demographics.csv", "wb")
geographic_out=open("geographic.csv", "wb")

for line in infile:
	split_line=line.split()
	
	#print "CORE SUBSTANCE"
	for i in range(2,354+1):
		if i==2:
			core_out.write(split_line[i])
		else:
			core_out.write(", " + split_line[i])
	core_out.write("\n")
    
	# print "IMPUTED SUBSTANCE"
	for i in range(355,850+1):
		if i==355:
			imputed_out.write(split_line[i])
		else:
			imputed_out.write(", " + split_line[i])
	imputed_out.write("\n")
	
	# print "SELECTED UNEDITED"
	for i in range(851,964+1):
		if i==851:
			selected_out.write(split_line[i])
		else:
			selected_out.write(", " + split_line[i])
	selected_out.write("\n")
	
	# print "NON CORE"
	for i in range(965,3056+1):
		if i==965:
			non_out.write(split_line[i])
		else:
			non_out.write(", " + split_line[i])
	non_out.write("\n")
	
	# print "DEMOGRAPHICS"
	for i in range(3057,3134+1):
		if i==3057:
			demographics_out.write(split_line[i])
		else:
			demographics_out.write(", " + split_line[i])
	demographics_out.write("\n")
	
	# print "GEOGRAPHIC"
	for i in range(3135,3137+1):
		if i==3135:
			geographic_out.write(split_line[i])
		else:
			geographic_out.write(", " + split_line[i])
	geographic_out.write("\n")
	

# for each line
	# add first n to core substance abuse
	# add next n to umputed
	# ...

# for line in infile:
	# linearr=line.split()
	# for word in linearr:
		# outfile.write(word)
		# outfile.write(" NUMBER, \n")
core=open("core_substance.csv", "r")
imputed=open("imputed_substance.csv", "r")
selected=open("selected_unedited.csv", "r")
non=open("non_core.csv", "r")
demographics=open("demographics.csv", "r")
geographic=open("geographic.csv", "r")
ddl_for_tables=open("table_ddl.txt", "wb")

ddl_for_tables.write("\n\nCORE SUBSTANCE XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
variables=core.readline().replace(' ','').split(',')
for variable in variables:
	ddl_for_tables.write(variable + " NUMBER, \n")

ddl_for_tables.write("\n\nIMPUTED SUBSTANCE XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
variables=imputed.readline().replace(' ','').split(',')
for variable in variables:
	ddl_for_tables.write(variable + " NUMBER, \n")

ddl_for_tables.write("\n\nSELECTED UNEDITED XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
variables=selected.readline().replace(' ','').split(',')
for variable in variables:
	ddl_for_tables.write(variable + " NUMBER, \n")

ddl_for_tables.write("\n\nNON CORE XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
variables=non.readline().replace(' ','').split(',')
for variable in variables:
	ddl_for_tables.write(variable + " NUMBER, \n")

ddl_for_tables.write("\n\nDEMOGRAPHICS XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
variables=demographics.readline().replace(' ','').split(',')
for variable in variables:
	ddl_for_tables.write(variable + " NUMBER, \n")

ddl_for_tables.write("\n\nGEOGRAPHIC XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
variables=geographic.readline().replace(' ','').split(',')
for variable in variables:
	ddl_for_tables.write(variable + " NUMBER, \n")

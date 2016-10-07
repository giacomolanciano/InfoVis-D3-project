#!/bin/python

START_YEAR = 1995
END_YEAR = 2014
INBOUND_FILE = "inbound_standalone.csv"
OUTBOUND_FILE = "outbound_standalone.csv"
OUTBOUND_DATA_START = 3
OUT_FILE = "inbound_outbound.csv"
OUT_HEADER_PREFIX = "iso3,Country Name,Unit"
SEPARATOR = ','
NULL_PLACE_HOLDER = "0"

# write header row
output = open(OUT_FILE, "w")
output.write(OUT_HEADER_PREFIX)
for i in range(START_YEAR,END_YEAR+1):
    output.write(SEPARATOR + str(i))
for i in range(START_YEAR,END_YEAR+1):
    output.write(SEPARATOR + "o" + str(i))

# read raw data files
with open(INBOUND_FILE, "r") as inbound:
    with open(OUTBOUND_FILE, "r") as outbound:
        line = inbound.readline()               # skip header line
        line = inbound.readline().strip()
        lineOUT = outbound.readline()           # skip header line
        lineOUT = outbound.readline().strip()
        
        # assume files has same length
        while line is not "":
            # append inbound data to output line
            componentsIN = str(line).split(SEPARATOR)
            
            if line[len(line)-1] == SEPARATOR:
                componentsIN.append(NULL_PLACE_HOLDER)
            output.write("\n"+componentsIN[0])
            
            for c in componentsIN[1:]:
                if c != "":
                    output.write(SEPARATOR+c.strip())
                else:
                    output.write(SEPARATOR + NULL_PLACE_HOLDER)
            
            # append outbound data to output line
            componentsOUT = str(lineOUT).split(SEPARATOR)
            
            if lineOUT[len(lineOUT)-1] == SEPARATOR:
                componentsOUT.append(NULL_PLACE_HOLDER)
            
            for c in componentsOUT[OUTBOUND_DATA_START:]:
                if c != "":
                    output.write(SEPARATOR+c.strip())
                else:
                    output.write(SEPARATOR + NULL_PLACE_HOLDER)
                        
            line = inbound.readline().strip()
            lineOUT = outbound.readline().strip()

output.write("\n")
output.close()
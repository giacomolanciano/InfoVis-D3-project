#!/bin/python

START_YEAR = 1995
END_YEAR = 2014
ISO_IN_FILE = "iso_code.csv"
ISO_COUNTRY = 0
ISO_CODE = 1
DATA_IN_FILE = "ObservationData_inbound.csv"
DATA_COUNTRY = 0
DATA_UNIT = 2
DATA_YEAR = 3
DATA_VALUE = 4
OUT_FILE = "inbound.csv"
OUT_HEADER = "iso3,Country Name,Unit"
SEPARATOR = ","

# create dictionary (country name - country code)
countries_iso_codes = {}
with open(ISO_IN_FILE, "r") as data:
    line = data.readline()              # skip header line
    line = data.readline()
    while line is not "":
        components = str(line).split(SEPARATOR)
        countries_iso_codes[str(components[ISO_COUNTRY])] = str(components[ISO_CODE])
        line = data.readline()

# write header row
output = open(OUT_FILE, "w")
output.write(OUT_HEADER)
for i in range(START_YEAR,END_YEAR+1):
    output.write(SEPARATOR + str(i))

# read raw data file
with open(DATA_IN_FILE, "r") as data:
    line = data.readline()              # skip header line
    line = data.readline()
    lastMissingYear = START_YEAR
    currentYear = 0
    
    # kick-off step (simulate do-while)
    components = str(line).split(SEPARATOR)
    countryName = components[DATA_COUNTRY]
    iso_code = countries_iso_codes[countryName]
    unit = components[DATA_UNIT]
    output.write("\n" + iso_code + SEPARATOR + countryName + SEPARATOR + unit)
    
    while line is not "":
        components = str(line).split(SEPARATOR)
        if components[DATA_COUNTRY] != countryName:
            # padd with SEPARATOR if missing values at the end of the row
            output.write(''.join([SEPARATOR]*((END_YEAR+1)-lastMissingYear)))
            countryName = components[DATA_COUNTRY]
            iso_code = countries_iso_codes[countryName]
            unit = components[DATA_UNIT]
            output.write("\n" + iso_code + SEPARATOR + countryName + SEPARATOR + unit)
            lastMissingYear = START_YEAR
        
        # padd with SEPARATOR if missing values
        currentYear = int(components[DATA_YEAR])
        output.write(''.join([SEPARATOR]*(currentYear-lastMissingYear)))
        
        # write value (removing trailing newline)
        output.write(SEPARATOR + str(components[DATA_VALUE]).strip())
        
        lastMissingYear = currentYear+1
        line = data.readline()

output.write("\n")
output.close()
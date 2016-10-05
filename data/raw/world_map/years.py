#!/bin/python

#<option value="Calculated Percentage">Percentage of slaves by inhabitants</option>
START_YEAR = 1995
END_YEAR = 2014

for i in reversed(range(START_YEAR,END_YEAR+1)):
    print "<option value=\""+ str(i) +"\">" + str(i) + "</option>"
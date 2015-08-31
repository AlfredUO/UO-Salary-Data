import csv

f=open('rawpdf.txt','r')
fo=open('thedata.csv', 'w')

##first loop reads through to the end of the intro
while True:
	line=f.readline()
	if not line: break
	if " HRIS Data Warehouse" in line: break

strings = ("UNIVERSITY OF OREGON", "RANK", "UNCLASSIFIED PERSONNEL LIST",  "may have more than one job", "Record for the Period:","UO Office of Institutional Research","Source: HRIS Data Warehouse","02/01/2015 6/11/2015")  ## These lines can be deleted
strings_with_commas = ("Journalism", "AAA","Campus Planning", "Business", "Director", "Assistant", "School of", "College of","No Rank", "Professor", "Leadership","Family", "GM", "AAA Planning", "Allied Arts")  ## these may have problematic commas


while True:
	line=f.readline()
	if not line: break
	if "HOME DEPARTMENT" in line: 
		fo.write('\n')
		continue
	if "ACADEMIC TITLE" in line:
		line=line.split("ACADEMIC TITLE")[1]
		if len(line)<2:continue
		fo.write(',')
	if any(s in line for s in strings): continue
	if "APPT STATUS" in line:
		line=line.replace('APPT STATUS', '')
	
	if "EEO CATEGORY" in line:
		line=line.replace('EEO CATEGORY', '')
	
	if "EEO CATEGORY" in line:
		line=line.replace('EEO CATEGORY', '')
	
	if "ANNUAL SALARY RATE" in line:
		line=line.replace("ANNUAL SALARY RATE",'')
		line=line.replace(',', '')
	if any(s in line for s in strings_with_commas):
		line=line.replace(',', '')
	if "Dept Head-Dec. Sci" in line:
		line=line.replace(';', '')
	if "$" in line:
		line=line.replace('$', '')
		
		
	fo.write(line.strip()) 
	fo.write(',')
	
fo.close()

## There's still some extra comma problems in the job titles - this just adds an extra line so it all lines up well
csvfile= open('thedata.csv', 'rb')
csvout=open('thedata1.csv', 'wb')
reader = csv.reader(csvfile)
writer = csv.writer(csvout)
for row in reader:
	if len(row)>6:
		if "TERM OF SVC" in row[6]:
			row.insert(5,'')
		writer.writerow(row)
		
	
	
		


		
	





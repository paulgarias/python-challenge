import os
import csv
from us_state_abbrev import us_state_abbrev as usabbr

csv_file_path1 = os.path.join('raw_data','employee_data1.csv')
csv_file_path2 = os.path.join('raw_data','employee_data2.csv')

# Original files are in the following configuration:
# Emp ID,Name,DOB,SSN,State
# 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
# 15,Samantha Lara,1993-09-08,848-80-7526,Colorado
# 411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania

# Need them to be in the following configuration
# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,12/04/1985,***-**-8166,FL
# 15,Samantha,Lara,09/08/1993,***-**-7526,CO
# 411,Stacy,Charles,12/20/1957,***-**-8526,PA

ID = ["Emp ID"]
firstName = ["First Name"]
lastName = ["Last Name"]
DoB = ["DOB"]
SSN = ["SSN"]
State = ["State"]

with open(csv_file_path1, newline="") as csvfile:
	csvreader = csv.reader(csvfile,delimiter=",")

	next(csvreader,None)
	for row in csvreader:
		ID.append(row[0])
		firstName.append(row[1].split()[0])
		lastName.append(row[1].split()[1])
		DoB.append(row[2].split("-")[1]+"/"+row[2].split("-")[2]+"/"+row[2].split("-")[0])
		SSN.append("***-**-"+row[3].split("-")[2])
		State.append(usabbr[row[4]])

with open(csv_file_path2, newline="") as csvfile:
	csvreader = csv.reader(csvfile,delimiter=",")

	next(csvreader,None)
	for row in csvreader:
		ID.append(row[0])
		firstName.append(row[1].split()[0])
		lastName.append(row[1].split()[1])
		DoB.append(row[2].split("-")[1]+"/"+row[2].split("-")[2]+"/"+row[2].split("-")[0])
		SSN.append("***-**-"+row[3].split("-")[2])
		State.append(usabbr[row[4]])

csv_file_path_new = os.path.join('results','employee_data_new.csv')

with open(csv_file_path_new,mode="w", newline="") as csvfile:
	csvwriter = csv.writer(csvfile,delimiter=",")
	for row in zip(ID,firstName,lastName,DoB,SSN,State):
		csvwriter.writerow(row)

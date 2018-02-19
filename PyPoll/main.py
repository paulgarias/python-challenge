import os
import csv
from collections import Counter

csv_file_path_1 = os.path.join("raw_data","election_data_1.csv")
csv_file_path_2 = os.path.join("raw_data","election_data_2.csv")

VoterID = []
County = []
Candidate = []

with open(csv_file_path_1,newline="") as csvfile:
	csvreader = csv.reader(csvfile,delimiter=",")
	next(csvreader,None)
	for row in csvreader:
		VoterID.append(row[0])	
		County.append(row[1])
		Candidate.append(row[2])


with open(csv_file_path_2,newline="") as csvfile:
	csvreader = csv.reader(csvfile,delimiter=",")
	next(csvreader,None)
	for row in csvreader:
		VoterID.append(row[0])	
		County.append(row[1])
		Candidate.append(row[2])

totVotes = len(Candidate)
dictCountCand = Counter(Candidate)


print("Election Results")
print("_______________________")
print("Total Votes: "+str(len(Candidate)))
print("_______________________")
for x in dictCountCand.keys():
	print(x+": "+"{:5.2f}".format(100.*dictCountCand[x]/float(totVotes))+"%"+" ("+str(dictCountCand[x])+")" )
print("_______________________")
print("Winner: " + max(dictCountCand,key=dictCountCand.get) )
print("_______________________")


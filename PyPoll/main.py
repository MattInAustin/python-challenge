### Matthew Elennis

### Import Lib ###

import csv
import os

### Variables ###

totalVotes = 0
candidateDict = {}
winningCount = 0

### Data ###

dataLoad = "Resources/election_data.csv"
dataOutput = "Resources/election_data.txt"

### Convert Excel to dictionairies ###

with open(dataLoad) as csvreader:
    reader = csv.DictReader(csvreader)
    for row in reader:
        totalVotes = totalVotes + 1
def printData():
    print ("Election Results")
    print ("----------------")
    print ("Total Votes: " + str(totalVotes))
    print ("----------------")

#Unfortunately this is all I have that works. I've run out of time. I will be meeting with a tutor to learn how to write this program.



    
    
        



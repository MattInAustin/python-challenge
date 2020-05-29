#This Python script will display info from budget_data
#Matthew Elenniss
#5/24/20

### Import libraries ##############################################

import random
import csv
import string
import os

### My Variables #################################################

monthsTotal = 0
totalProfitLoss = 0
beforeProfit = 0
changeList = []
changeMonth = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 99999]

### Create Variables that will allow a read and output of data ###

loadData = "Resources/budget_data.csv"
outputData = "Resources/budget_data.txt"

### Take data from Excel sheet and put it into dictionaries ######

with open(loadData) as financeData:
    excelReader = csv.DictReader(financeData)

    for row in excelReader:

        ### total months ###
        monthsTotal = monthsTotal + 1

        ### Figure out total Profit/Loss ###
        totalProfitLoss = totalProfitLoss + int(row["Profit/Losses"])

        ### Record the change ###
        profitChange = int(row["Profit/Losses"]) - beforeProfit
        beforeProfit = int(row["Profit/Losses"])
        changeList = changeList + [profitChange]
        changeMonth = changeMonth + [row["Date"]]

        ### Calculate increase ###
        if (profitChange > greatestIncrease[1]):
            greatestIncrease[0] = row["Date"]
            greatestIncrease[1] = profitChange

        ### Greatest decrease ###
        if (profitChange < greatestDecrease[1]):
            greatestDecrease[0] = row["Date"]
            greatestDecrease[1] = profitChange
        
### Output #######################################################
def printOutput():
    print("Finacial Analysis")
    print("-----------------")
    print("Total Months: " + str(monthsTotal))
    print("Total: " + str(totalProfitLoss))
    print("Greatest Increase in Profit: " + str(greatestIncrease[0]) + "   " + str(greatestIncrease[1]))
    print("Greatest Decrease in Revenue: " + str(greatestDecrease[0]) + "   " + str(greatestDecrease[1]))


### Print to terminal ############################################
    
printOutput()
        
          
### Send to text file ###########################################
with open(outputData, "w") as txt:
    txt.write(str(printOutput()))

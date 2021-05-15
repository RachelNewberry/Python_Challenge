import os
import csv

PyBank = os.path.join(r"C:\Users\rache\OneDrive\Documents\School\John Hopkins\Session_3_Python\Python_Challenge\PyBank\Resources", "budget_data.csv")


#Revenue Variables
Total_Months = 0
Previous_Revenue = 0
Total_Net = 0
Changes_Month = []
Changes_Revenue = []
Greatest_Increase =["",0]
Greatest_Decrease = ["", 9999999999999999]


with open(PyBank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    row = next(csvreader)

    for row in csvreader:
        
        #Totals
        Total_Months = Total_Months + 1
        Total_Net = Total_Net + int(row[1])
        
        #Changes in Revenue
        Revenue_Change = int(row[1]) - Previous_Revenue
        Previous_Revenue = int(row[1])
        Changes_Revenue = Changes_Revenue + [Revenue_Change]
        Changes_Month = Changes_Month = [row[0]]

        #Increase
        if  (Revenue_Change > Greatest_Increase[1]):
            Greatest_Increase[0] = row[1]
            Greatest_Increase[1] = Revenue_Change
       

        #Decrease
        if (Revenue_Change < Greatest_Decrease[1]):
            Greatest_Decrease[0] = row[0]
            Greatest_Decrease[1] = Revenue_Change

#Average Change
Revenue_Avg = sum(Changes_Revenue) / len(Changes_Revenue)

#Output
print([f'Total Months: {Total_Months}'])
print([f'Total Net: ${Total_Net}'])
print([f'Avg Revenue Changes: ${Revenue_Avg}'])
print([f'Greatest Increase in Revenue: {Greatest_Increase[0]} (${Greatest_Increase[1]})'])
print([f'Greatest Decrease in Revenue: {Greatest_Decrease[0]} (${Greatest_Decrease[1]})'])


#Print Output to Text
Results = os.path.join('.', 'analysis')
with open(Results, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow([f'Total Months: {Total_Months}'])
    csvwriter.writerow([f'Total Net: ${Total_Net}'])
    csvwriter.writerow([f'Avg Revenue Changes: ${Revenue_Avg}'])
    csvwriter.writerow([f'Greatest Increase in Revenue: {Greatest_Increase[0]} (${Greatest_Increase[1]})'])
    csvwriter.writerow([f'Greatest Decrease in Revenue: {Greatest_Decrease[0]} (${Greatest_Decrease[1]})'])









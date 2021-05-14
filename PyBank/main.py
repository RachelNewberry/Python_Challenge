import os
import csv

PyBank = os.path.join(r"C:\Users\rache\OneDrive\Documents\School\John Hopkins\Session_3_Python\Python_Challenge\PyBank\Resources", "budget_data.csv")


#Revenue Variables
Total_Months = 0
Total_Net = 0
Starting_Revenue = 0
Changes_Month = []
Changes_Revenue = []
Greatest_Increase =[]
Greatest_Increase_Month = 0
Greatest_Decrease = 0
Greatest_Decrease_Month = 0

with open(PyBank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    row = next(csvreader)

    for row in csvreader:
        
        #Totals
        Total_Months = Total_Months + 1
        Total_Net = Total_Net + int(row[1])
        
        #Changes
        Revenue_Change = int(row[1]) - Starting_Revenue
        Starting_Revenue = int(row[1])
        Changes_Revenue = Changes_Revenue + [Revenue_Change]
        Changes_Month = Changes_Month = [row[0]]

        #Increase
        if int(row[1]) > Greatest_Increase:
            Greatest_Increase = inc(row[1])
            Greatest_Increase_Month = row[0]

       

        #Decrease
        if (Revenue_Change < Greatest_Decrease[1]):
            Greatest_Decrease[0] = row[0]
            Greatest_Decrease[1] = Revenue_Change

#Average Change
Revenue_Avg = sum(Changes_Revenue) / len(Changes_Revenue)

#Output
print([f'Total Months: {total_months}'])
print([f'Total_Net: ${Total_Net}'])
print([f'Avg Revenue Changes: ${Revenue_Avg}'])
print([f'Greatest Increase in Revenue: {Greatest_Increase[0]} (${Greatest_Increase[1]})'])
print([f'Greatest Decrease in Revenue: {Greatest_Decrease[0]} (${Greatest_Decrease[1]})'])


#Print Output to Text
Results = os.path.join('.', 'analysis')
with open(Results, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow([f'Total Months: {total_months}'])
    csvwriter.writerow([f'Total_Net: ${Total_Net}'])
    csvwriter.writerow([f'Avg Revenue Changes: ${Revenue_Avg}'])
    csvwriter.writerow([f'Greatest Increase in Revenue: {Greatest_Increase[0]} (${Greatest_Increase[1]})'])
    csvwriter.writerow([f'Greatest Decrease in Revenue: {Greatest_Decrease[0]} (${Greatest_Decrease[1]})'])









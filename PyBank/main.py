#PyBank

#List dependencies
import csv
import os

#upload and output files
file_load = os.path.join("budget_data.csv")
file_output = os.path.join("budget_analysis.txt")

#List parameters
total_months = 0
months_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999999999999999999]
total_net = 0

#Read csv and convert to dictionary
with open(file_load) as pybank_data:
    reader = csv.reader(pybank_data)
    
    #List the header
    header = next(reader)
    #print(header)
    
    #First row
    first_row = next(reader)
    #print(first_row)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1])
    
    #Create loop
    for row in reader:
        #Track the total net
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        #print(total_net)
        
        #Track net change
        net_change = int(row[1])- previous_net
        previous_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        #print(net_change_list)
        months_of_change = months_of_change + [row[0]]
        #print(months_of_change)
        
        #Find greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row [0]
            greatest_increase[1] = net_change
        #greatest_increase = max(net_change_list)
        #print(greatest_increase)
    
        #Find greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
        #greatest_decrease = min(net_change_list)
        #print(greatest_decrease)
    
    
#Find average net change
net_monthly_avg = sum(net_change_list)/ len(net_change_list)
#print(net_monthly_avg)

#Create output file
output = (
    f"\nFinancial Analysis\n"
    f"---------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase In Profits: {greatest_increase[0]}, (${greatest_increase[1]})\n"
    f"Greatest Decrease In Profits: {greatest_decrease[0]}, (${greatest_decrease[1]})\n"
)
print(output)

#create text file
with open(file_output, "w") as txt_file:
    txt_file.write(output)
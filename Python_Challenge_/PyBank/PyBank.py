import os, csv
import array as arr

file = 'analysis/Results.txt'
csvpath = os.path.join('Resources', 'budget_data.csv')

Number_rows = 0
Total_sum = 0
Increase_list = []
values_inc = []
change_data = 0
rows_value = 0
average = 0
greatest = 0
decrease = 0
sum_change = 0

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print("Financial Analysis")
    print("-----------------------------")

    # Read each row of data after the header
    for row in csvreader:
         
        #it sums a 1 to the value of Number_rows everytime the cycle passes a row in the cvs file
        Number_rows = Number_rows + 1
        Total_sum = Total_sum + int(row[1]) 
        rows_value = int(row[1])

        if Total_sum == rows_value:
            #This is the first row
            values_inc.append(rows_value)
        else:
            change_data = rows_value - values_inc[-1]
            sum_change = sum_change + change_data
            values_inc.append(rows_value)
            Increase_list.append(change_data)
            if change_data > greatest:
                greatest = change_data
                mes = row[0]
            if change_data < decrease:
                decrease = change_data
                mes1 = row[0]
    average = sum_change/(Number_rows - 1) 
    print(f"Total months: {Number_rows}")        
    print(f"Total: ${Total_sum}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {mes} (${greatest})")
    print(f"Greatest Decrease in Profits: {mes1} (${decrease})")

Lines = [f"Financial Analysis", "-------------------",f"Total months: {Number_rows}", f"Total: ${Total_sum}", f"Average Change: ${average}", f"Greatest Increase in Profits: {mes} (${greatest})", f"Greatest Decrease in Profits: {mes1} (${decrease})"]

with open('analysis/Results.txt', 'w') as f:
    f.write('\n'.join(Lines))



import os
import csv

#create and object of csv file
input_file= os.path.join('budget_data.csv')
output_file= os.path.join('budget_output.txt')

#variables
date = []
pro_loss= []
total_date = 0
total_pro_los = 0
value = 0
prev_value = 0
greatest_increase_value = 0
greatest_increase_date = ""
greatest_decrease_date = ""
greatest_decrease_value = 0
avg_change_difference = []
difference = 0



#Open and read the csv file
with open (input_file, "r") as budget_file:
    
    csvreader = csv.reader(budget_file, delimiter=',')

    header = next(csvreader)
    
    #loop through each row of the file
    for row in csvreader:
        date.append(row[0]) 
        pro_loss.append(row[1])
       
        #The total number of months included in the dataset

        total_date = total_date + 1

        #The net total amount of "Profit/Losses" over the entire period

        total_pro_los = total_pro_los + int(row[1])
    
        #The greatest increase in profits (date and amount) over the entire period
        #To track the profit and loss changes
        value = int(row[1]) - prev_value

        #To track the previous value
        prev_value = int(row[1])
        
        if (value > greatest_increase_value):
            greatest_increase_value = value
            greatest_increase_date = row[0]

        #The greatest decrease in losses (date and amount) over the entire period
        if (value < greatest_decrease_value): 
            greatest_decrease_value = value
            greatest_decrease_date = row[0]

    #The average of the changes in "Profit/Losses" over the entire period
    for x in range(1,len(pro_loss)):
        difference = int(pro_loss[x])- int(pro_loss[x-1])
        avg_change_difference.append(difference)

    #print out the output:
    print("Financial Analysis")
    print("-----------------------------")
    print("Total Months: " + str(total_date))
    print("Total profit and loss: " + "$" + str(total_pro_los))
    print("Average Change:" + str(round(sum(avg_change_difference)/len( avg_change_difference),2)))
    print("Greatest Increase: " + str(greatest_increase_date) + " " + "($"  + str(greatest_increase_value) + ")")
    print("Greatest Decrease: " + str(greatest_decrease_date) + " " + "($"  + str(greatest_decrease_value) + ")")

#Open and write the text file
with open(output_file, "w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(total_date))
    txt_file.write("\n")
    txt_file.write("Total profit and loss: " + "$" + str(total_pro_los))
    txt_file.write("\n")
    txt_file.write("Average Change:" + str(round(sum(avg_change_difference)/len( avg_change_difference),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase_date) + " " + "($"  + str(greatest_increase_value) + ")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease_date) + " " + "($"  + str(greatest_decrease_value) + ")")





    
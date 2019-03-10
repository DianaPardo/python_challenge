#Could not open files. I struggled to open them inside the master folder, it appeared a message I could not solve the problem, marked a problem with the branches.
#In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period


#Get path
import os
import os.path
import csv

# Set paths
Bank_path = '/Users/dianapardo/Documents/GitHub/HomeWork-3/python_challenge/PyBank/Resources'
csv_path = '/Users/dianapardo/Documents/GitHub/HomeWork-3/python_challenge/PyBank/Resources/budget_data'
result_path = '/Users/dianapardo/Documents/GitHub/HomeWork-3/python_challenge/PyBank/Resources/Results'

#∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞
# At first tried to join paths and concatenate accordingly to a loop. Could not do it, looked for support at StackOverflow and changed it to a full path. It seems like I was overiterating paths.
# Set for loops
#filepaths = []
#for file in os.listdir(csv_path):
    #if file.endswith(".csv"):
        #filepaths.append(os.path.join(csv_path, file))
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# Reading CSV, previously had problems with this, did not get the proper codes for reading the files.
#Set start of calculations
filepaths='/Users/dianapardo/Documents/GitHub/HomeWork-3/python_challenge/PyBank/Resources/budget_data.csv'
for file in filepaths:
    tot_revenue = 0
    month_count = 0
    revenue = 0
    rev_change = 0
    data_dict_list = []
    with open(file, newline="") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            # Set first formula: increase/decrase
            rev_diff = {"rev_diff": int("{Revenue}".format(**row)) - revenue}
            rev_change = rev_change + int("{Revenue}".format(**row)) - revenue
            revenue = int("{Revenue}".format(**row))
            tot_revenue += revenue
            month_count += 1
            data_dict_list.append({**row, **rev_diff})

        # Set maximum and minimum values as a list
        increase_dict = dict(max(data_dict_list, key=lambda x:x["rev_diff"]))
        decrease_dict = dict(min(data_dict_list, key=lambda x:x["rev_diff"]))


        # Set increase/decrease month by month
        increase_date = increase_dict.get("Date")
        increase_revdiff = increase_dict.get("rev_diff")
        decrease_date = decrease_dict.get("Date")
        decrease_revdiff = decrease_dict.get("rev_diff")


        # Adjust start of calculations. First row as 0 (zero)
        first_row = data_dict_list[0]
        first_row_revdiff = first_row.get("rev_diff")
        rev_change = rev_change - first_row_revdiff
        avg_change = int(rev_change/(month_count - 1))
        
        # Grab the filename from the original path.
        # The _, gets rid of the path. The , _ gets rid of the .csv.
        _, filename = os.path.split(file)
        filename, _ = filename.split(".csv")     
        # Print ttable
        print(
            f"Financial Analysis - {filename}\n"
            f"----------------------------\n"
            f"Total Months: {month_count}\n" 
            f"Total: ${tot_revenue}\n"
            f"Average Change: ${avg_change}\n"
            f"Greatest Increase in Profits: {increase_date} (${increase_revdiff})\n"
            f"Greatest Decrease in Profits: {decrease_date} (${decrease_revdiff})\n"
        )

        # Export a text file with the results.
        text_path = os.path.join(output_path, filename + ".txt")
        with open(text_path, "w") as text_file:
            text_file.write(
                f"Financial Analysis: {filename}\n"
                f"----------------------------\n"
                f"Total Months: {month_count}\n" 
                f"Total: ${tot_revenue}\n"
                f"Average Change: ${avg_change}\n"
                f"Greatest Increase in Profits: {increase_date} (${increase_revdiff})\n"
                f"Greatest Decrease in Profits: {decrease_date} (${decrease_revdiff})\n"
            )
#!/usr/bin/env python
# coding: utf-8

# In[3]:


#The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period


import os
import csv


# In[4]:


csvpath = os.path.join("..", "Resources", "budget_data.csv")
analysispath = os.path.join("Resources", "budget_analysis.txt")


# In[5]:


#create variables to hold values
net_change_list = []
month_of_change = []
total_monthly_change = []

#set original values to 
total_month = 0
net_total = 0
previous_net = 867884


# In[6]:


with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #need to skip the title using next otherwise the first row[1] cannot be converted to an integer.
    header = next(csvreader)
    
    first_row = next(csvreader)
    total_month+=1
    net_total+=int(first_row[1])
#     previous_net = int(first_row[1])
    
    for row in csvreader:
        #total month
        total_month = total_month + 1
        
        #net total 
        net_total = net_total + int(row[1])
        
        #changes in "profit/losses" over entire period
        net_change = int(row[1]) - previous_net
        net_change_list.append(net_change)
        month_of_change.append(row[0])
        previous_net = int(row[1])
               
        #greatest increase in profit
        greatest_increase = max(net_change_list)
        
        #greatest decrease in profit
        greatest_decrease = min(net_change_list)
        
        #Month with greatest increase
        #find index of the greatest increase in the net change list
        #and accordingly use that index to print out the month in the month list 
        great_increase_month = month_of_change[net_change_list.index(greatest_increase)]
        
        #Month with greatest decrease
        great_decrease_month = month_of_change[net_change_list.index(greatest_decrease)]
        
     #total monthly change 
    total_monthly_change = sum(net_change_list)
        
    #find average of the changes
    average_monthly_change = (total_monthly_change) / len(month_of_change)
        


# In[7]:


print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months:{total_month}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_monthly_change}")
print(f"Greatest Increase in Profits: {great_increase_month} (${greatest_increase})")
print(f"Greatest Increase in Profits: {great_decrease_month} (${greatest_decrease})")


# In[8]:


#create txt file to store the analysis
analysispath = "pybank.txt"

with open(analysispath, "w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("-----------------------------------")
    txt_file.write(f"Total Months:{total_month}")
    txt_file.write(f"Total: ${net_total}")
    txt_file.write(f"Average Change: ${average_monthly_change}")
    txt_file.write(f"Greatest Increase in Profits: {great_increase_month} (${greatest_increase})")
    txt_file.write(f"Greatest Increase in Profits: {great_decrease_month} (${greatest_decrease})")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





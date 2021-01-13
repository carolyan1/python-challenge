#!/usr/bin/env python
# coding: utf-8

# In[169]:


import os
import csv


# In[170]:


election_csv = os.path.join("election_data.csv")


# In[171]:


#set variables
total = 0
my_dict = {}


with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    #Loop through rows. Create a dictionary. 
    #Add candidate as key if there's not yet a candidate.
    #Otherwise keep adding the votes to count
    for row in csvreader:
        total +=1
        if row[2] not in my_dict.keys():
            my_dict[row[2]]=1
        else:
            my_dict[row[2]]+=1   
    
    largest_vote = 0
    for key,value in my_dict.items():
        if value > largest_vote:
            largest_vote = value
            winner = key
    


# In[172]:


#percent of votes
kpc = "{0:.3f}".format(my_dict["Khan"]/total*100)
cpc = "{0:.3f}".format(my_dict["Correy"]/total *100)
lpc = "{0:.3f}".format(my_dict["Li"]/total*100)
opc = "{0:.3f}".format(my_dict["O'Tooley"]/total*100)


# In[173]:


a = my_dict["O'Tooley"]


# In[174]:


#print out the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")
print(f"Khan: {kpc}% ({my_dict['Khan']})")
print(f"Correy: {cpc}% ({my_dict['Correy']})")
print(f"Li: {lpc}% ({my_dict['Li']})")
print(f"O'Tooley: {opc}% ({a})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# In[175]:


#Export a text file with the results
output_path = os.path.join("election.txt")
with open (output_path, 'w', newline = '') as txtfile:
    txtfile.write("Election Results")
    txtfile.write("-------------------------")
    txtfile.write(f"Total Votes: {total}")
    txtfile.write("-------------------------")
    txtfile.write(f"Khan: {kpc}% ({my_dict['Khan']})")
    txtfile.write(f"Correy: {cpc}% ({my_dict['Correy']})")
    txtfile.write(f"Li: {lpc}% ({my_dict['Li']})")
    txtfile.write(f"O'Tooley: {opc}% ({a})")
    txtfile.write("-------------------------")
    txtfile.write(f"Winner: {winner}")
    txtfile.write("-------------------------")


# In[ ]:
#github upload version 1





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





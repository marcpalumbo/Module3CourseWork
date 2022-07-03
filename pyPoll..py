# count total number of votes casted
# find out how many candidates received votes
#what percentage of the vote did each candidate receive 
#who won the election]

import csv
from distutils import text_file 


# assign a variable for the file to load and the path 

#file_to_load = r"C:\Users\palum\OneDrive\Desktop\DataClass\Module3CourseWork\Resources\election_results.csv"


# open the election results and read the file
#
#electionData = open(file_to_load,'r')

#close the file
#electionData.close()

#alternate method to open and read the file using with statemetn

#with open(file_to_load) as electionData:
    #to-do, perform analysis
    #print(electionData)

#both methods tried and working 

#file_to_save =  r"C:\Users\palum\OneDrive\Desktop\DataClass\Module3CourseWork\Resources\election_results.csv"
#electionData = (file_to_save,"w")

#with open(file_to_save) as electionData:
    #print(file_to_save)


import os
dir(os)

file_to_load = os.path.join("Resources","election_results.csv")


#create a filename and variable to a indirect path to the file
file_to_save = os.path.join("analysis","election_results.txt")

# method two of opening a file and writing to it 

with open(file_to_load) as election_data:

    #to do: read and analyze data here

    #read the file object with the reader function

    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)

  #  for row in file_reader:
            #print(row)
  

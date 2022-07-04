# count total number of votes casted
# find out how many candidates received votes
#what percentage of the vote did each candidate receive 
#who won the election]

import csv

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
file_to_save = os.path.join("Resources","election_results.txt")
 
    #outfile =  open(file_to_save,'w')
    #outfile.write("Hello World!")
#setting total number of votes to zero, do this before opening the file so each time it opens, we are starting from zero
total_votes = 0 

#delcaring new list to reference names of candidates
candidate_options = []
#creating empty dictionary that will hold the name of candidate and votes received
candidate_votes = {}

#winning candidate and winning count tracker:

winning_candidate = ""
winning_count = 0
winning_percentage = 0 
#opening CSV file to work with and declaring it as election data for future reference
with open(file_to_load) as election_data:

    #to do: read and analyze data here

    #read the file object with the reader function

    file_reader = csv.reader(election_data)

#skips header row in datwa 
    headers = next(file_reader)
    


    for row in file_reader:
       #adds one to total vote count for every row in csv file AFTER the header
        total_votes +=1 
    # candidates name are located in 3rd row of file 
        candidate_name = row[2]

        #if the candidates name is not already in our list of candidates, add the name to the list
        if candidate_name not in candidate_options:
        
            candidate_options.append(candidate_name)

            
     #start tracking each cnadidates vote count
            candidate_votes[candidate_name] = 0
     #increment based on candidates name 
        candidate_votes[candidate_name] += 1  

#determine percentage of vote each candidate recieved by looping through the counts
# iterate through cnadidate list
# 
for candidate_name in candidate_votes:
   
    #retrieve vote count of candidate
   
    votes = candidate_votes[candidate_name] 
   
    #calculate percentage of votes
   
   
    vote_percentage = (float(votes)/float(total_votes)* 100)

    print(f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")    
   

    if (votes> winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage

        winning_candidate = candidate_name
   
winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.2f}%\n"
    f"---------------------------\n")

print(winning_candidate_summary)

 
   # print(candidate_votes)

   # print(total_votes)
  



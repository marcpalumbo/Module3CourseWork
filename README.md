# Overview of Election Audit

For this assignment, we were tasked with analyzing a CSV file of over 350,000 rows in python. We were tasked with calculating the election results with information including:
*Total Votes
*Total Votes by County
*County with the largest total turnout
*Each candidates name, percentage of votes won, and total votes received
*A table that displayed the winner's name, votes received, and percentage of votes received

There were many challenges that were presented while programming this. While the module laid the foundation of what we needed to do, creating new results for the county data proved to be more difficult than I had initially envisioned. 

## Election Audit Results 
Here are the election audit results after running our code:
![Election Audit Results](https://github.com/marcpalumbo/Module3CourseWork/blob/05870e89f50501cdee8de2a151df8853cd93da01/Resources/Analysis%20Screenshots/Analysis%20Results.png)

*How many votes were cast in this congressional election?
  
After analyzing all rows of data, it was determined that there was a total of 369,711 votes recorded across all counties. This was done by iterating through all of the rows of the CSV file and counting each row. 

*Provide a breakdown of the number of votes and the percentage of total votes for county intheprecinct.

There were three total counties that were audited in our analysis: Jefferson county, Denver county, and Arapahoe county. Denver had a far higher vote count than the others, at 306,855 while Jefferson and Arapohoe had 38,855 and 24,801 respectively. In terms of percentages, Denver accounted for 82.8 percent of all votes while Jefferson and Arapahoe accounted for 10.5% and 6.7% respectively. Gathering this information was the most challenging part of this module, given that we had to iterate through all the rows and assign new variables to lists and dictionaries. 

This part of the challenge took me the longest as I spent a good chunk of time debugging and figuring out how to print the results of the "for loop" correctly. 

*Which county had the largest number of votes?

Denver ultimately had the largest voter turnout at 306,855

*Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

The breakdown of the three candidates results is shown in the image above. Dianna DeGatte received 73.8% of the vote, with a total vote count of 272,892.
Charles Casper Stockham was the second place vote getter, at 85,213 votes which amounted to 23% of all votes casted. And Raymon Anthony Doane was third with 3.1% of the votes, or 11,606 in total. 

*Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

Dianna DeGette is the winner of this election. She received 272,892 votes which was 73.8% of all cotes casted. 
 
 ## Election Audit Summary
 
In summary, this code provided in this submission will be able to be reused for future elections. The python script is written in such a way that that the loops and iterations can be applied to other csv files if that is the file tyoe of where the other election data is located. You would need to alter which files you are using as the election data. You would need to change the file_to_load and file_to_change files and assign them to the relevant data using the same method.
Code snippted listed below:

![Code to Change for Future Elections](https://github.com/marcpalumbo/Module3CourseWork/blob/05870e89f50501cdee8de2a151df8853cd93da01/Resources/Analysis%20Screenshots/Files%20to%20load%20and%20save.png)

Keep in mind that the format of the CSV file would need to remain consistent as well. However, if the information in a different csv file was not in the same order as the data in this file, it would be a relatively minor fix to get the results and print them to a new text file. You would need to edit the numbers inside the brackets of candidate_name = row[] and county_name = row[] listed below:

![Code to Change if New csv File is Formatted Differently](https://github.com/marcpalumbo/Module3CourseWork/blob/05870e89f50501cdee8de2a151df8853cd93da01/Resources/Analysis%20Screenshots/Code%20for%20Rows.png)

It would be wise to change the location of the csv and txt files as well that way you wouldn't be overwriting this data with the results of any other election. These minor changes will allow you to use this same code provided in the future!

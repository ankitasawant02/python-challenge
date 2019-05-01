import os
import csv

from collections import Counter

#create and object of csv file
input_file= os.path.join('election_data.csv')
output_file= os.path.join('election_output.txt')

#variables

unique_candidate_names = []
votes = 0

#Open and read the csv file
with open (input_file,"r") as election_file:

    csvreader = csv.reader(election_file, delimiter=',')

    header = next(csvreader)

    #loop through each row of the file
    for row in csvreader:
        
        #The total number of votes cast
        votes = votes + 1

        unique_candidate_names.append(row[2])

    #count the unique_candidate occurances
    vote_counter = Counter(unique_candidate_names)
    
    #calculate the percent of total no of votes each candidate won 
    for candidate_vote in vote_counter:
        percent = (int(vote_counter[candidate_vote])/ int(votes) )* 100
        vote_counter[candidate_vote] = str(round(percent,2)) +"% ("+ str(vote_counter[candidate_vote]) +")"
      
        
    #print out the output:
    print()
    print()
    print("Election Results")
    print("--------------------------------------------")
    print("Total Votes: "+ str(votes))
    print("--------------------------------------------")
    
    #Print the complete list of candidates who received votes 
    for candidate_vote_percent in vote_counter:
        print(str(candidate_vote_percent) +" "+vote_counter[candidate_vote_percent])
    print("--------------------------------------------")

    #Print the winner
    for winner in sorted(vote_counter, key=vote_counter.get, reverse=True)[:1]:
        print("winner: "+ str(winner))
    print("--------------------------------------------")


#Open and write the text file
with open (output_file,"w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("--------------------------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes: "+ str(votes))
    txt_file.write("\n")
    txt_file.write("--------------------------------------------")
    txt_file.write("\n")
    for candidate_vote_percent in vote_counter:
        txt_file.write(str(candidate_vote_percent) +" "+vote_counter[candidate_vote_percent])
        txt_file.write("\n")
    txt_file.write("--------------------------------------------")
    txt_file.write("\n")
    txt_file.write("--------------------------------------------")      
    txt_file.write("\n")
    for winner in sorted(vote_counter, key=vote_counter.get, reverse=True)[:1]:
        txt_file.write("winner: "+ str(winner))   
    txt_file.write("\n")
    txt_file.write("--------------------------------------------")


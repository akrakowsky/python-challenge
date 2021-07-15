#Create variables
total_votes = 0
candidate_options = []
candidate_votes ={}
winning_candidate = " "
winning_count = 0

#Read csv and create a list
with open (election_load) as election_data:
    reader = csv.reader(election_data)

    #Show the header
    header = next(reader)
    #print(header)
    
    #Start loop
    for row in reader:
        #Load tally count
        #print("." , end = "")
        
        #Add tally to total vote count:
        total_votes = total_votes + 1
        
        #Retrieve the candidate name from rows
        candidate_name = row[2]
        
        #Find unique candidate
        if candidate_name not in candidate_options:
            #Add candidate to list
            candidate_options.append(candidate_name)
            #Tracker voter count for each candidate
            candidate_votes[candidate_name] = 0
    
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    
#Create text file
with open(election_output, "w") as txt_file:
    #Print final vote count
    election_results = (
    f"\nElection Results\n"
    f"-------------------\n"
    f"Total Votes: {total_votes}\n"
    f"---------------------\n"
    )
    print(election_results, end = " ")
    
    #Save txt_file
    txt_file.write(election_results)
    
    #Determine winner by voter count
    for candidate in candidate_votes:
        #Change vote count to percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #Find the winner
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        #Print voter count
        voter_output = f"{candidate}: {vote_percentage : .3f}% ({votes})\n"
        print(voter_output, end = " ")
        
        txt_file.write(voter_output)
        
    #Print winning candidate
    winning_candidate_result = (
    f"----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"-----------------------------\n"
    )
    
    print(winning_candidate_result)
    
    #Save as txt file
    txt_file.write(winning_candidate_result)
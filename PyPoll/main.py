import os
import csv 

PyPollcsv = os.path.join(r"C:\Users\rache\OneDrive\Documents\School\John Hopkins\Session_3_Python\Python_Challenge\PyPoll\Resources", "election_data.csv")

#Variables and Dictionaries 
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

with open(PyPollcsv) as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    
    for row in csvreader:

        total_votes = total_votes + 1
        
        candidate_name = row["Candidate"]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

election_results = os.path.join("..", "election_results")
with open(election_results, "w") as txt_file:

    election_results = (
        f"\n\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes}\n"
        f"--------------------------\n"
    )
    print(election_results)

    txt_file.write(election_results)

    for candidate in candidate_votes:
        
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)

        txt_file.write(voter_output)
    

    winning_candidate_summary = (
            f"---------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"---------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)







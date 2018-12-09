import os
import pandas as pd 

electioncsv = os.path.join("PyPoll","election_data.csv")


election_data = pd.read_csv(electioncsv)

print("Election Results")
print("----------------------------")

total_votes = len(election_data["Voter ID"].value_counts())
print(f'Total Votes: {total_votes}')

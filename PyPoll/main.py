import os
import csv

electioncsv = os.path.join("PyPoll", "election_data.csv")

voters = []
candidate = []
candidate_list = []

Khan = 0
Correy = 0
Li = 0
OTooley = 0

with open (electioncsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        voters.append(row[0])
        candidate.append(row[2])
        total_votes = len(voters)
    for i in candidate:
        if i not in candidate_list:
            candidate_list.append(i)
        elif i == 'Khan':
            Khan = Khan + 1
        elif i == 'Correy':
            Correy = Correy + 1
        elif i == 'Li':
            Li = Li + 1
        elif i == "O'Tooley":
            OTooley = OTooley + 1
        Khan_percent = Khan/total_votes
        Correy_percent = Correy/total_votes
        Li_percent =Li/total_votes    
        OTooley_percent = OTooley/total_votes

total_votes = total_votes 
candidate_list = candidate_list 
candidates = candidate 

Khan_percent = (Khan/total_votes)*100
Correy_percent = (Correy/total_votes)*100
Li_percent = (Li/total_votes)*100
OTooley_percent = (OTooley/total_votes)*100

Election_Analysis = [Khan, Correy, Li, OTooley]
Winner = max(Election_Analysis)


print("Election Results")
print("------------------------")
print("Total Votes: " + str(total_votes))
print("------------------------")
print("Khan: " + str('{:.3f}'.format(round(Khan_percent, 3)))+ "% " + "(" + str(Khan) + ")")
print("Correy: " + str('{:.3f}'.format(round(Correy_percent, 3)))+ "% " + "(" + str(Correy) + ")")
print("Li: " + str('{:.3f}'.format(round(Li_percent, 3))) + "% " + "(" + str(Li) + ")")
print("O'Tooley: " + str('{:.3f}'.format(round(OTooley_percent, 3))) + "% " + " (" + str(OTooley) + ")")
print("------------------------")
print("Winner: " + str(candidate_list[Election_Analysis.index(max(Election_Analysis))]))

pypoll_output = open("PyPoll/PyPoll_output.txt",'w')
pypoll_output.write("Election Results\n------------------------\nTotal Votes: " + str(total_votes) + "\n------------------------\nKhan: " + str('{:.3f}'.format(round(Khan_percent, 3)))+ "% " + "(" + str(Khan) + ")\nCorrey: " + str('{:.3f}'.format(round(Correy_percent, 3)))+ "% " + "(" + str(Correy) + ")\nLi: " + str('{:.3f}'.format(round(Li_percent, 3))) + "% " + "(" + str(Li) + ")\nO'Tooley: " + str('{:.3f}'.format(round(OTooley_percent, 3))) + "% " + " (" + str(OTooley) +")\n------------------------\nWinner: " + str(candidate_list[Election_Analysis.index(max(Election_Analysis))]))

pypoll_output.close()
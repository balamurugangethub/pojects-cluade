# Variables and types
name = "Bala"
age = 21
gpa = 8.5
is_student = True

print(f"My name is {name}, I am {age} years old")

# Lists
players = ["Dhoni", "Kohli", "Rohit", "Bumrah"]
print(players[0])        # first item
print(players[-1])       # last item
print(len(players))      # how many items

# Loop through list
for player in players:
    print(f"Player: {player}")

# Dictionary — this is VERY important for DE
match = {
    "team1": "CSK",
    "team2": "MI",
    "winner": "CSK",
    "runs": 180
}

print(match["winner"])
print(match.keys())
# Basic function
def calculate_run_rate(runs, overs):
    return runs / overs

rr = calculate_run_rate(180, 20)
print(f"Run rate: {rr}")

# Function with multiple returns
def match_result(team1_score, team2_score):
    if team1_score > team2_score:
        return "Team 1 wins"
    elif team2_score > team1_score:
        return "Team 2 wins"
    else:
        return "Tie"

print(match_result(180, 165))
print(match_result(150, 170))
import pandas as pd

# We'll use a small manually created dataset today
# Tomorrow we use the real IPL dataset

data = {
    "match_id": [1, 2, 3, 4, 5],
    "team1": ["CSK", "MI", "RCB", "KKR", "DC"],
    "team2": ["MI", "RCB", "KKR", "DC", "CSK"],
    "winner": ["CSK", "RCB", "KKR", "DC", "CSK"],
    "runs_scored": [180, 165, 142, 178, 190]
}

# Create a DataFrame — this is pandas' main object
df = pd.DataFrame(data)

# Look at it
print(df)
print("---")
print(df.shape)           # rows, columns
print("---")
print(df.columns)         # column names
print("---")
print(df.dtypes)          # data types

# Filter — only matches CSK played
csk_matches = df[df["team1"] == "CSK"]
print(csk_matches)

# Average runs scored
avg_runs = df["runs_scored"].mean()
print(f"Average runs: {avg_runs}")

# Who won the most?
win_counts = df["winner"].value_counts()
print(win_counts)
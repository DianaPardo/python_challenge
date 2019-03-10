import os
import pandas as pd
import numpy as np

# Stablishing paths and links
Poll_path = os.path.join(os.getcwd(), "Resources")
csv_path = os.path.join(Poll_path, "election_data.csv")
results_path = os.path.join(Poll_path, "Results")

# Looping and iterating results and, first, optimizing choosing the right path
filepaths = []
for file in os.listdir(csv_path):
    if file.endswith(".csv"):
        filepaths.append(os.path.join(csv_path, file))

for file in filepaths:
    df = file
    df_pd = pd.read_csv(df)
    # First calculation
    tot_votes = df_pd["Candidate"].count()
    # Get a dataframte
    cand_votes = df_pd["Candidate"].value_counts()
    cand_votes_df = pd.DataFrame(cand_votes)
    cand_votes_df.columns=["Votes"]
    # Make list of candidates
    candidate_list = cand_votes_df.index.tolist()
    vote_list = cand_votes_df.iloc[:, 0].tolist()
    # Calculate percentage

    percent_votes = ((vote_list/tot_votes)*100).round(1)
    percent_list = list(map("{}%".format, percent_votes))
    # Get a table for voting results
    results_df = pd.DataFrame({
        "Candidate": candidate_list,
        "Number of Votes": vote_list,
        "Percentage of Votes": percent_list
    })
    # Index votes per winner
    win_df = results_df.set_index("Number of Votes")
    win_votes = max(vote_list)
    winner = win_df.loc[win_votes].Candidate

    # Get it from the original path
    # delete csv file
    _, filename = os.path.split(file)
    filename, _ = filename.split(".csv")

    # Print final table
    print(
        f"Election Results - {filename}\n"
        f"-----------------------------------------\n"
        f"Total Votes: {tot_votes}\n"
        f"-----------------------------------------\n" 
        f"{results_df.to_string(index=False)}\n"
        f"-----------------------------------------\n" 
        f"Winner: {winner}\n"
    )
    # Export results
    text_path = os.path.join(output_path, filename + ".txt")
    with open(text_path, "w") as text_file:
        text_file.write(
            f"Election Results - {filename}\n"
            f"-----------------------------------------\n"
            f"Total Votes: {tot_votes}\n"
            f"-----------------------------------------\n" 
            f"{results_df.to_string(index=False)}\n"
            f"-----------------------------------------\n" 
            f"Winner: {winner}\n"
        )
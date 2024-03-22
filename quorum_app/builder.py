from quorum_app.map_utils import *

import quorum_app.models as models
import quorum_app.read_from_files as files

def build_legislators_summary():
    legislators = files.read("data_dir/legislators.csv", models.Legislator)
    vote_results = files.read("data_dir/vote_results.csv", models.Vote_Result)

    compute_votes_sides(legislators, vote_results, 'legislator')

    return legislators

def build_bills_summary():
    legislators = files.read("data_dir/legislators.csv", models.Legislator)
    bills = files.read("data_dir/bills.csv", models.Bill)
    votes = files.read("data_dir/votes.csv", models.Vote)
    vote_results = files.read("data_dir/vote_results.csv", models.Vote_Result)

    compute_votes_sides(votes, vote_results, 'vote')

    fill_legislators_reference(bills, legislators)
    fill_vote_reference(bills, votes)

    return bills

from quorum_app.models import Vote_Type

def compute_votes_sides(instance, vote_results, object_type):
    for _, value in vote_results.items():
        current_id = value.vote_id
        if (object_type == 'legislator'):
            current_id = value.legislator_id

        vote_side = value.vote_type
        if (vote_side == Vote_Type.SUPPORT):
            increment = instance[current_id].vote_results_support + 1
            instance[current_id].vote_results_support = increment
        elif (vote_side == Vote_Type.OPPOSE):
            increment = instance[current_id].vote_results_oppose + 1
            instance[current_id].vote_results_oppose = increment

def fill_legislators_reference(bills, legislators):
    for key, value in bills.items():
        try:
            legislator = legislators[value.sponsor_id]
            bills[key].sponsor_name = legislator.name
        except:
            bills[key].sponsor_name = "Not a legislator"

def fill_vote_reference(bills, votes):
    for key, value in votes.items():
        bills[value.bill_id].vote = value

import json

def render_legislators_as_simple_html(legislators):
    response = "Legislators Summary:<br>----------"
    for _, value in legislators.items():
        response = response + "<br>ID: " + str(value.id) + " <br>"
        response = response + "<br>Legislator: " + value.name + " <br>"
        response = response + "Supported bills: " + str(value.vote_results_support) + "<br> "
        response = response + "Opposed bills: " + str(value.vote_results_oppose) + "<br> "

    return response

def render_bills_as_simple_html(bills):
    response = "Bills Summary:<br>----------"
    for _, value in bills.items():
        response = response + "<br>ID: " + str(value.id) + " <br>"
        response = response + "<br>Title: " + value.title + "<br>"
        response = response + "Primary Sponsor: "+ value.sponsor_name + " <br><br>"
        response = response + "Supporters: " + str(value.vote.vote_results_support) + "<br> "
        response = response + "Opposers: " + str(value.vote.vote_results_oppose) + "<br>----------<br>"

    return response

def render_legislators_as_json(data):
    response = []
    for _, value in data.items():
        values = {
            'id': value.id,
            'name': value.name,
            'vote_results_support': value.vote_results_support,
            'vote_results_oppose': value.vote_results_oppose
        }
        response.append(values)

    return json.dumps(response)

def render_bills_as_json(data):
    response = []
    for _, value in data.items():
        values = {
            'id': value.id,
            'title': value.title,
            'sponsor_name': value.sponsor_name,
            'vote_results_support': value.vote.vote_results_support,
            'vote_results_oppose': value.vote.vote_results_oppose
        }
        response.append(values)

    return json.dumps(response)

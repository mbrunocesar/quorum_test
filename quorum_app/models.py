from django.db import models
from enum import Enum

class Legislator:
    def __init__(self, params):
        self.id = int(params[0])
        self.name = params[1]
        self.vote_results_support = 0 # to be filled later / lazyload
        self.vote_results_oppose = 0 # to be filled later / lazyload

class Bill:
    def __init__(self, params):
        self.id = int(params[0])
        self.title = params[1]
        self.sponsor_id = int(params[2]) # references Legislators
        self.sponsor_name = "" # to be filled later / lazyload
        self.vote = None # references Votes # to be filled later / lazyload

class Vote:
    def __init__(self, params):
        self.id = int(params[0])
        self.bill_id = int(params[1]) # references Bills
        self.vote_results_support = 0 # to be filled later / lazyload
        self.vote_results_oppose = 0 # to be filled later / lazyload

class Vote_Result:
    def __init__(self, params):
        self.id = int(params[0])
        self.legislator_id = int(params[1]) # references Legislators
        self.vote_id = int(params[2]) # references Votes
        self.vote_type = Vote_Type(int(params[3])) # 1 for Agree, 2 for disagree
    
class Vote_Type(Enum):
    SUPPORT = 1
    OPPOSE = 2

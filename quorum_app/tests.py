from django.test import TestCase
from quorum_app.models import *
from quorum_app.builder import *


class QuorumTestCase(TestCase):
    def setUp(self):
        self.legislators = build_legislators_summary()
        self.bills = build_bills_summary()

    def test_build_legislators_as_expected(self):
        self.assertEqual(len(self.legislators), 20)

        # legislators can't have a empty name
        for _, value in self.legislators.items():
            self.assertTrue(value.name is not None)

        # legislators can't have more votes than the number of bills
        for _, value in self.legislators.items():
            self.assertTrue(value.vote_results_support + value.vote_results_oppose <= len(self.bills))
    
    def test_build_bills_as_expected(self):
        self.assertEqual(len(self.bills), 2)

        # bills can't have a empty title
        for _, value in self.bills.items():
            self.assertTrue(value.title is not None)

        # bill can't have a empty sponsor
        for _, value in self.bills.items():
            self.assertTrue(value.sponsor_name is not None)

        # no bill can have more votes than the number of legislators
        for _, value in self.bills.items():
            self.assertTrue(value.vote.vote_results_support + value.vote.vote_results_oppose <= len(self.legislators))

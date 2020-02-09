import json
import unittest
import pytest_check as check

from search_app import create_app, config


# test object is the first restaurant in the data
with open("restaurants.json", 'r') as f:
    test_restaurant = json.load(f)["restaurants"][0]


class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app(config.TestingConfig)
        cls.client = cls.app.test_client()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_config(self):
        self.assertEqual(self.app.config["TESTING"], True)

    def test_index(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["restaurants"][0], test_restaurant)

    def test_valid_query_params(self):

        # case 1: the example from the instruction (have checked that the matched restaurants exist)
        res = self.client.get("/restaurants/search?q=sushi&lat=60.17045&lon=24.93147")
        check.equal(res.status_code, 200)
        check.is_true(res.get_json()["matched_restaurants"])

        # case 2: input is from the first restaurant in the data
        test_url = "/restaurants/search?q={0}&lat={2}&lon={1}".format(test_restaurant["tags"][0],
                                                                      test_restaurant["location"][0],
                                                                      test_restaurant["location"][1])
        res = self.client.get(test_url)
        check.equal(res.status_code, 200)
        check.is_true(res.get_json()["matched_restaurants"])
        check.equal(res.get_json()["matched_restaurants"][0], test_restaurant)

        # case 3: input that no restaurants match
        res = self.client.get("/restaurants/search?q=machine_learning&lat=60.17045&lon=24.93147")
        check.equal(res.status_code, 200)
        check.is_false(res.get_json()["matched_restaurants"])

    def test_invalid_query_params(self):
        # query string is smaller than one character (empty string)
        res = self.client.get("/restaurants/search?q=&lat=60.17045&lon=24.93147")
        check.equal(res.status_code, 400)
        # latitude is invalid (wrong type)
        res = self.client.get("/restaurants/search?q=&lat=test&lon=24.93147")
        check.equal(res.status_code, 400)
        # latitude is invalid (wrong range)
        res = self.client.get("/restaurants/search?q=&lat=100&lon=24.93147")
        check.equal(res.status_code, 400)
        # longitude is invalid (wrong range)
        res = self.client.get("/restaurants/search?q=&lat=60.17045&lon=-200")
        check.equal(res.status_code, 400)

    def test_lack_query_params(self):
        # lack query string
        res = self.client.get("/restaurants/search?lat=60.17045&lon=24.93147")
        check.equal(res.status_code, 400)
        # lack latitude
        res = self.client.get("/restaurants/search?q=sushi&lon=24.93147")
        check.equal(res.status_code, 400)
        # lack longitude
        res = self.client.get("/restaurants/search?q=sushi&lat=60.17045")
        check.equal(res.status_code, 400)

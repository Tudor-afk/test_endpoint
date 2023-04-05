import unittest
import requests

class TestGetData(unittest.TestCase):

    def test_travel_connection(self):
        url = 'http://127.0.0.1:8088/get_data?data_type=travel&snippet=false'
        
        response = requests.get(url)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_travel_get_meta(self):
        url = 'http://127.0.0.1:8088/get_meta'

        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("travel-index", data)
        column_names = data["travel-index"][:].split(",")
        print("Table Name: travel")
        print("Column Names: ")
        for column in column_names:
            print(column)
    
    def test_travel_integrity(self):
        url = 'http://127.0.0.1:8088/get_data?data_type=travel&snippet=false'

        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        travels = data["@list"][:]
        for travel in travels:
            self.assertIsNotNone(travel["@id"])
            self.assertIsNotNone(travel["Accomodation cost"])
            self.assertIsNotNone(travel["Accomodation type"])
            self.assertIsNotNone(travel["Destination"])
            self.assertIsNotNone(travel["Duration(days)"])
            self.assertIsNotNone(travel["End Date"])
            self.assertIsNotNone(travel["Start date"])
            self.assertIsNotNone(travel["Transportation cost"])
            self.assertIsNotNone(travel["Transportation type"])
            self.assertIsNotNone(travel["Traveler age"])
            self.assertIsNotNone(travel["Traveler gender"])
            self.assertIsNotNone(travel["Traveler name"])
            self.assertIsNotNone(travel["Traveler nationality"])

    def test_travel_get_data_snippet_false(self):
        url = 'http://127.0.0.1:8088/get_data?data_type=travel&snippet=false'

        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()

        travels = data["@list"][:]
        for travel in travels:
            print(f"id: {travel['@id']}, Accomodation cost: {travel['Accomodation cost']},Accomodation type: {travel['Accomodation type']},Destination: {travel['Destination']},Duration(days): {travel['Duration(days)']},End Date: {travel['End Date']},Start date: {travel['Start date']},Transportation cost: {travel['Transportation cost']},Transportation type: {travel['Transportation type']},Traveler age: {travel['Traveler age']},Traveler gender: {travel['Traveler gender']},Traveler name: {travel['Traveler name']},Traveler nationality: {travel['Traveler nationality']}")

    def test_travel_get_data_snippet_true(self):
        url = 'http://127.0.0.1:8088/get_data?data_type=travel&snippet=true'

        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        travels = data["@list"][:]
        for travel in travels:
            print(f"id: {travel['@id']}, Accomodation cost: {travel['Accomodation cost']},Accomodation type: {travel['Accomodation type']},Destination: {travel['Destination']},Duration(days): {travel['Duration(days)']},End Date: {travel['End Date']},Start date: {travel['Start date']},Transportation cost: {travel['Transportation cost']},Transportation type: {travel['Transportation type']},Traveler age: {travel['Traveler age']},Traveler gender: {travel['Traveler gender']},Traveler name: {travel['Traveler name']},Traveler nationality: {travel['Traveler nationality']}")


if __name__ == '__main__':
    unittest.main()
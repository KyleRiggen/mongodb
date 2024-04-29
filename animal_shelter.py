from pymongo import MongoClient
from bson.objectid import ObjectId
import json

class AnimalShelter(object):

    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, password):
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31580
        DB = 'AAC'
        COL = 'animals'
	    
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username, password, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]
           
    def create(self, data):
        if isinstance(data, dict):
            if data:  # check if data is not empty
                self.collection.insert_one(data)
                return True
            raise ValueError("data is empty?")
        elif isinstance(data, str):  # check if data is a string
            try:
                data_dict = json.loads(data)  # try to convert string to dictionary
                if data_dict:
                    self.collection.insert_one(data_dict)
                    return True
                raise ValueError("data is empty?")
            except json.JSONDecodeError:
                raise ValueError("data conversion error to json (dictionary)")
        raise TypeError("data something besides dictionary or string")

    def retrieve_all(self):
        try:
            result = list(self.collection.find({}))
            return result
        except Exception as e:
            print("an error occurred:", e)
            return []

    def read(self):
        # find random document
        randomDoc = [{"$sample": {"size": 3}}]
        result = list(self.collection.aggregate(randomDoc))

        if result:
            print("found document:", result)
            return result
        else:
            print("not found, check query.")
            return []

    def update(self, filter, update_data):
        try:
            result = self.collection.update_many(filter, {"$set": update_data})
            return result.modified_count
        except Exception as e:
            print("an error occurred:", e)
            return 0

    def delete_doc(self, filter):
        try:
            result = self.collection.delete_many(filter)
            return result.deleted_count
        except Exception as e:
            print("an error occurred:", e)
            return 0
        
    def retrieve_water_filtered(self):
        water_rescue_breeds = [
            "Labrador Retriever",
            "Golden Retriever",
            "Newfoundland",
            "Portuguese Water Dog",
            "Saint Bernard",
            "Irish Water Spaniel",
            "Chesapeake Bay Retriever"
        ]
            
        max_age_in_weeks = 104

        try:
            filter_query = {
                'breed': {'$in': water_rescue_breeds},
                'age_upon_outcome_in_weeks': {'$lt': max_age_in_weeks}
            }

            result = list(self.collection.find(filter_query))
            return result
        except Exception as e:
            print("an error occurred:", e)
            return []
        
    def retrieve_mountain_filtered(self):
        mountain_rescue_breeds = [
            "Saint Bernard", 
            "Bernese Mountain Dog", 
            "German Shepherd", 
            "Border Collie", 
            "Labrador Retriever", 
            "Bloodhound", 
            "Australian Shepherd", 
            "Golden Retriever"
        ]
            
        max_age_in_weeks = 104
        
        try:
            filter_query = {
                'breed': {'$in': mountain_rescue_breeds},
                'age_upon_outcome_in_weeks': {'$lt': max_age_in_weeks}
            }

            result = list(self.collection.find(filter_query))
            return result
        except Exception as e:
            print("an error occurred:", e)
            return []

    def retrieve_disaster_filtered(self):
        disaster_rescue_breeds = [
            "German Shepherd", 
            "Labrador Retriever", 
            "Belgian Malinois", 
            "Border Collie", 
            "Golden Retriever", 
            "Bloodhound", 
            "Rottweiler", 
            "Collie"
        ]
            
        max_age_in_weeks = 104
        
        try:
            filter_query = {
                'breed': {'$in': disaster_rescue_breeds},
                'age_upon_outcome_in_weeks': {'$lt': max_age_in_weeks}
            }

            result = list(self.collection.find(filter_query))
            return result
        except Exception as e:
            print("an error occurred:", e)
            return []

from us_visa.pipeline.training_pipeline import TrainingPipeline

#from dotenv import load_dotenv

#load_dotenv()

import os
from pymongo import MongoClient

#mongo_url = os.environ.get("MONGODB_URL")
#client = MongoClient(mongo_url)
#db = client.get_database("visa_db")
#print(db.list_collection_names())
pipeline = TrainingPipeline()
pipeline.run_pipeline()
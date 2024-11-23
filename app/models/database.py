from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson import ObjectId

mongo = PyMongo()

def init_db(app):
    mongo.init_app(app)

client = MongoClient('mongodb://localhost:27017')
db = client.sensitive_data

scans_collection = db.scans

def save_scan(filename, extracted_data):
    scans_collection.insert_one({'filename': filename, 'data': extracted_data})

def get_all_scans():
    return list(scans_collection.find())

def get_scan_by_filename(filename):
    return scans_collection.find_one({'filename': filename})

def delete_scan(scan_id):
    scans_collection.delete_one({'_id':  ObjectId(scan_id)})

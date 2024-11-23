from app.models.database import mongo

def save_scan(filename, sensitive_data):
    mongo.db.scans.insert_one({'filename': filename, 'sensitive_data': sensitive_data})

def get_all_scans():
    return list(mongo.db.scans.find())

from  pymongo import MongoClient

def find_one(mongodb_username, mongodb_password, mongodb_host, mongodb_port, database_name, collection_name, filter):
    client = MongoClient(f"mongodb://{mongodb_username}:{mongodb_password}@{mongodb_host}:{mongodb_port}/?authMechanism=DEFAULT")
    db = client[database_name]
    collection = db[collection_name]

    try:
        result = collection.find_one(filter=filter)
        return result
    except Exception as e:
        raise


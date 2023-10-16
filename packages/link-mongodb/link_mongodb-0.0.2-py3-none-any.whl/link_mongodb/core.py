from  pymongo import MongoClient

def find_one(mongodb_username, mongodb_password, mongodb_host, mongodb_port, database_name, collection_name, filter):
    client = MongoClient(f"mongodb://{mongodb_username}:{mongodb_password}@{mongodb_host}:{mongodb_port}/?authMechanism=DEFAULT")
    db = client[database_name]
    collection = db[collection_name]

    try:
        result = collection.find_one(filter=filter)
        print(result)
        return result
    except Exception as e:
        raise

if __name__ == "__main__":
    find_one(
        mongodb_username="admin",
        mongodb_password="152447as",
        mongodb_host="143.42.213.40",
        mongodb_port="27017",
        database_name="master_auth",
        collection_name="users",
        filter={"username": "admin"}
    )
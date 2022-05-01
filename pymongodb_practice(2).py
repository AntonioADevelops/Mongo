from bson import ObjectId
import pymongo
import os
import sys
import pprint
import datetime

def main():
    connection_string = os.environ["MONGO_CONNECTION_STRING"]
    db_name = os.environ["MONGO_DBNAME"]
    
    client = pymongo.MongoClient(connection_string)
    db = client[db_name]
    collection = db['test'] #1. put the name of your collection in the quotes
    
    post = {"author": "Mike", #2. add a document to your collection using the insert_one method
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
    posts = db.posts
    post_id = posts.insert_one(post).inserted_id
    post_id
    ObjectId('...') 
    
    db.list_collection_names() #3. print the number of documents in the collection
    ['posts']
    
    pprint.pprint(posts.find_one()) #4. print the first document in the collection
    {'_id': ObjectId('...'),
    'author': 'Mike',
    'date': datetime.datetime(...),
    'tags': ['mongodb', 'python', 'pymongo'],
    'text': 'My first blog post!'}
    
    #5. print all documents in the collection
    
    #6. print all documents with a particular value for some attribute
    #ex. print all documents with the birth date 12/1/1990
    
    
if __name__=="__main__":
    main()
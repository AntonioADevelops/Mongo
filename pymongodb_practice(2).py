from bson import ObjectId
import pymongo
import os
import sys
import pprint

def main():
    connection_string = os.environ["MONGO_CONNECTION_STRING"]
    db_name = os.environ["MONGO_DBNAME"]
    
    client = pymongo.MongoClient(connection_string)
    db = client[db_name]
    collection = db['test'] #1. put the name of your collection in the quotes
    
    post = {'name':"Jane Doe", #2. add a document to your collection using the insert_one method
        'birthday':"12/3/1990",
        'birthplace':"test town",}
    posts = db.posts
    post_id = posts.insert_one(post).inserted_id
    post_id
    ObjectId()
    
    db.list_collection_names() #3. print the number of documents in the collection
    ['posts']
    
    pprint.pprint(posts.find_one()) #4. print the first document in the collection
    {'_id': ObjectId(),
    'name':"Jane Doe",
    'birthday':"12/3/1990",
    'birthplace':"test town",}
    
    pprint.pprint(posts.find_many()) #4. print the first document in the collection
    {'_id': ObjectId(),
    'name':"Jane Doe",
    'birthday':"12/3/1990",
    'birthplace':"test town",}
     
    #5. print all documents in the collection
    
    pprint.pprint(posts.find_one({"name": "John Doe"}))#6. print all documents with a particular value for some attribute
    {'_id': ObjectId(), #ex. print all documents with the birth date 12/1/1990
    'name':"Jane Doe",
    'birthday':"12/3/1990",
    'birthplace':"test town",}
    
    # db.collection.deleteMany({'author': 'Mike'})
    
if __name__=="__main__":
    main()
import pymongo
import os
import pprint

def main():
    connection_string = os.environ["MONGO_CONNECTION_STRING"]
    db_name = os.environ["MONGO_DBNAME"]
    
    client = pymongo.MongoClient(connection_string)
    db = client[db_name]
    collection = db['posts'] #1. put the name of your collection in the quotes
    
    # 2. add a document to your collection using the insert_one method
    post = {'name':"Jane Doe", 'birthday':"12/3/1990", 'birthplace':"test town",}, {'name':"John Doe", 'birthday':"11/3/1987", 'birthplace':"test town",}, {'name':"Jarquevias Doe", 'birthday':"4/19/2009", 'birthplace':"new test town",}
    collection.insert_many(post).inserted_ids
    
    #3. print the number of documents in the collection
    count = collection.count_documents({})
    print(count)
    
    # 4. print the first document in the collection
    pprint.pprint(collection.find_one()) 
    
    # 5. print all documents in the collection
    for i in collection.find(): 
        pprint.pprint(i)
    
    #6. print all documents with a particular value for some attribute
    for i in collection.find({'birthplace':"test town"}):
        pprint.pprint(i)
    
    # 7. Extension: Research another PyMongo function. This function deletes all documents with a value for some attribute
    collection.delete_many({ 'name': 'Jane Doe'});
    
    
if __name__=="__main__":
    main()
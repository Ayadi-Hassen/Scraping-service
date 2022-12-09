from facebook_scraper import get_posts
from pydantic import BaseModel
from fastapi import FastAPI,Response
from pymongo import MongoClient

app = FastAPI()

class Facebook(BaseModel):
    page_name: str
    pages: int

def get_collection_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")

    db = client["fb_database"]
    collection=db["facebooke_page"]
    return collection


@app.post("/fb/posts")
def fb_posts(facebook: Facebook, response: Response):
    
    list_posts=[]
    collection=get_collection_db()
    try:
        for post in get_posts(facebook.page_name, pages=facebook.pages):
            list_posts.append(post)
        list_posts=[dict(post) for post in list_posts ]
        if len(list_posts)==0:
            response.status_code = 404
            return f"No results found for {facebook.page_name}"      
        else:
            collection.insert_many(list_posts)
    except Exception:
        response.status_code = 500
        return "Internal Server Error"
        
    response.status_code = 200
    return f"{len(list_posts)} posts has been collected from {facebook.page_name} Facebook page and inserted in the database"


from pymongo import MongoClient
from configparser import ConfigParser
from datetime import datetime

config = ConfigParser()
config.read('config.ini')

connection_string = config.get('481-db','connection_string')

client = MongoClient(connection_string)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

print("-----------------")  



def connect_to_db():
    try:
        client = MongoClient(connection_string)
        db = client.mydatabase
        return db
    except Exception as e:
        print(f"Error: {e}")
        return None

def connect_to_collection(collection_name):
    try:
        db = connect_to_db()
        if db is None:
            raise Exception("Database bağlantısı kurulamadı.")
        
        collection = db[collection_name]
        print(f"Number of documents in {collection_name} collection: {collection.count_documents({})}")
        print(f"Connected to {collection_name} collection.")
        return collection
    except Exception as e:
        print(f"Error: {e}")
        return None

def create_review(review):
    try:
        collection = connect_to_collection('reviews')
        if collection is None:
            raise Exception("Collection bağlantısı kurulamadı.")
        
        result = collection.insert_one(review)
        return result.inserted_id
    except Exception as e:
        print(f"Error: {e}")
        return None

sample_reviews = [
    {
        "company_name": "TechCorp",
        "review_text": "Great learning experience with supportive team members.",
        "rating": 4.5,
        "salary_info": "Paid internship with $2000/month stipend.",
        "transportation_info": "Transportation allowance provided.",
        "remote_work_option": "Yes",
        "department": "Software Development",
        "internship_role": "Backend Developer Intern",
        "project_rating": 4.8,
        "meal_card": "Yes",
        "technologies_used": ["Python", "Django", "PostgreSQL"],
        "feedback_date": datetime(2024, 10, 12),
        "like_count": 25
    },
    {
        "company_name": "DataSolutions",
        "review_text": "Worked on exciting data projects. Learned a lot!",
        "rating": 4.2,
        "salary_info": "Unpaid internship.",
        "transportation_info": "Not provided.",
        "remote_work_option": "No",
        "department": "Data Science",
        "internship_role": "Data Analyst Intern",
        "project_rating": 4.0,
        "meal_card": "No",
        "technologies_used": ["SQL", "Pandas", "Tableau"],
        "feedback_date": datetime(2024, 9, 15),
        "like_count": 15
    },
    {
        "company_name": "InnovateX",
        "review_text": "Amazing work culture with a focus on growth and development.",
        "rating": 4.7,
        "salary_info": "Paid internship with $1500/month.",
        "transportation_info": "Company shuttle service provided.",
        "remote_work_option": "Hybrid",
        "department": "Product Management",
        "internship_role": "Product Manager Intern",
        "project_rating": 4.6,
        "meal_card": "Yes",
        "technologies_used": ["Excel", "JIRA", "Confluence"],
        "feedback_date": datetime(2024, 8, 20),
        "like_count": 30
    }
]



for review in sample_reviews:
    review_id = create_review(review)
    print(f"Review with ID {review_id} added successfully.")
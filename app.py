from flask import Flask, render_template, request
import pymongo
import ssl
import os
from dotenv import load_dotenv
import certifi

load_dotenv()

app = Flask (__name__)
app.secret_key=os.environ.get('SECRET_KEY')

MONGO_URI=os.environ.get('MONGO_URI')
DB_NAME="movies_reviews"

client = pymongo.MongoClient(MONGO_URI, tlsCAFile=certifi.where())

@app.route('/')
def index():
    return "Hello world"

# if this file is being ran as main:
if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)

import configparser
import os
from pymongo import MongoClient

config = configparser.ConfigParser()
config.read('app/config.ini')

if os.environ.get("HEROKU"):
    uri = os.environ.get("MONGODB_URI")
    database = os.environ.get("DATABASE_NAME")
    client = MongoClient(uri)
    GIT_URL = os.environ.get("GIT_URL")
    GIT_BRANCH = os.environ.get("GIT_BRANCH")
    GIT_SSH_KEY = os.environ.get("GIT_SSH_KEY")
else:
    #database = 'ccdaExamples'
    #client = MongoClient('localhost', 27017)
    database = 'heroku_brpn0kqd'
    client = MongoClient("mongodb://heroku_brpn0kqd:ji373v99tdvndpb3ccpvhg0sqe@ds155091.mlab.com:55091/heroku_brpn0kqd")
    GIT_URL = "https://github.com/schmoney/C-CDA-Examples.git"
    #GIT_BRANCH = 'permalinksHashObject'
    GIT_BRANCH = 'master'
    GIT_SSH_KEY = ''

db = client[database]

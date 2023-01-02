
import firebase_admin
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {"databaseURL":"https://web-app-372312-default-rtdb.firebaseio.com/"})


ref = db.reference("/")

# import json
# with open("countries_1.json", "r") as f:
# 	file_contents = json.load(f)
# ref.set(file_contents)

trav = db.reference("/countries/country")




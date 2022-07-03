import pyrebase
from distance import distance


config = {
  "apiKey": "AIzaSyAVHoVDvvZ-xxxxxxxxxxxxxxxxxxxxxxx",
  "authDomain": "raspxxxxxxx.firebaseapp.com",
  "databaseURL": "https://raspxxxxxx-default-rtdb.firebaseio.com",
  "projectId": "raspxxxxxxx",
  "storageBucket": "raspxxxxxxx.appspot.com",
  "messagingSenderId": "28590xxxxxx",
  "appId": "1:285906238651:web:74eccxxxxxxxxxxxxxx",
  "measurementId": "G-WPxxxxxxxxxx"
};


firebase = pyrebase.initialize_app(config)



storage = firebase.storage()
database = firebase.database()
a = distance()
print (a)
database.child("DB object name")
data = {"key1": a}
database.set(data)

from tinydb import TinyDB, Query, where

db = TinyDB('data1.json', indent=4)

users = db.table("Users")
roles = db.table("Roles")

users.insert({'name': "Patrick", "salary": 25000})
users.insert({'name': "Herman", "salary": 50000})
users.insert({'name': "Ingrid", "salary": 48000})

roles.insert_multiple([
	{'name': "Pythonista"},
	{'name': "Javaista"},
	{'name': "JavaScripta"},
])


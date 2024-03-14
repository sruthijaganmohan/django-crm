# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'djangocrmcompany',
#         'USER': 'root',
#         'PASSWORD': 'Ughbhsy#017',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Ughbhsy#017'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE djangocrmcompany")

print("Database created")
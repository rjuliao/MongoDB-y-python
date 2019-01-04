# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 19:56:29 2019

Script para conectar python a mongodb
Para el correcto funcionamiento de este código, en el cmd
debe esta corriendo el servidor de mongodb.

@author: raulh
"""

#import pymongo
#Creamos una instancia con MongoDB
from pymongo import MongoClient
import datetime as dt
import pprint as ppm

client = MongoClient('localhost', 27017) #Nos conectamos direcramenre al puerto del servidor

#Accedemos a una base de datos y una collección

db = client['test-database']
collection = db['testcollection']
 
#Document representado por un objeto tipo JSON
post = {"name": "lavi",
         "age": 80,
         "date": dt.datetime.utcnow()}
 
#Insertamos un elemento en la colección "test-collection"
#collection.insert_one(post)

print(post_n = collection.insert_one(post)) nos regresa el id de la transacción
print(db.list_collection_names())


#---------------------------------------------------------------------------------

#Obtener un solo documento
#v = ppm.pprint(collection.find_one())

#Obtenemos todos los documentos que se encuentran en una colección

for i in collection.find({'age':{'$lt':50}}):
    ppm.pprint(i)
 
 
 
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId



app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb://marcus:rugby4me@ds221003.mlab.com:21003/recipes'


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
    recipes=mongo.db.the_recipes.find())


    

@app.route('/recipe_content')    
def recipe_content():
    return render_template("recipe_content.html",
    recipes=mongo.db.the_recipes.find())



@app.route('/categories', methods=['GET'])  
def search_by_category():
    return render_template("categories.html",
    recipes=mongo.db.categories.find())



    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

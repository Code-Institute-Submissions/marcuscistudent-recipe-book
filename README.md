recipe-book

The recipe-book was created so that users could use CRUD for food recipes.
users can also search the database for recipes by name and by category.

The recipe-book app uses Python, javascript, html and css and some frameworks
within the languages stated.

The website is for anyone who wants to keep track of recipes they have found by adding them
to the database and also for people who dont have any ideas of what to cook so they
can come to the app for some insporation. It is also useful for people who have a 
product/meal in mind but dont know of a recipe. they can search for a recipe for that meal.

The Features of this app are the view all recipes page which displays all recipes that have been added to the database,
the  add recipe page which allows users to create a new recipe and add it to the databse.
The edit recpie function so that any existing recipe can be changed and updated
the edit category and add category pages are useful to help users search for recipes by category
which is useful if the cant find the correct name of a recipe
The main function of the recipe-book is the search function,
users can query the databse and search by recipe name or by category.

I would like to implement a register, login and logout function and then also improve
the search function to search for many items and also query letters in a recipe name

The technologies used are HTML CSS and Python. I used the flask framework to render my templates, 
pymongo to access my mongodb databse on Mlab using python.

I used JINJA to render my python code on my html page and then I used materialize to syle my
recipe book and the googleapi icons to make the navigation bar look more proffessional

I used UnitTest to test the the pages are rendered correcly using flask and I have tested extensively the search
and display fucntions to make sure that the ID matches and that no errors occur.

The app has been pushed to gihub and delpoyed in Heroku. I created a requirements.txt file a Procfile
and I scaled my dynos and inserted the IP and PORT into the config vars in heroku so that the app would push correcty.


Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

The app is run by entering python3 app.y into the terminal or hitting the run button on the app.py page.


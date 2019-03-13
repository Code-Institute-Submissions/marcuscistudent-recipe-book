# Recipe Book

The website is a recipe book that enables users to use CRUD functionality for food recipes.

The website enables users to search the database for recipes as well as view them,
edit them and delete them.


## The site can be viewed [here](https://recipebook-project.herokuapp.com/).

## UX

The website is designed to look appealing to users and to be an interactive community
where users can share their recipes and find new ones that the havent used before.

The ingredients background was used to draw the users attention while the menu
was designed for ease of access and to be respinsive on multiple devices.

![Mobile](https://github.com/marcuscistudent/recipe-book/blob/master/static/assets/mobile2.png "Mobile")
![Desktop](https://github.com/marcuscistudent/recipe-book/blob/master/static/assets/desktop2.png "Desktop")

## Technologies used
1. HTML
2. CSS
3. Python
4. Flask
5. MongoDB
6. Materialize
7. Jquery


## Features

The website uses Materialize and Jquery for the responsive menu and the responsive grid
layout.

Google API icons were used to style the menu.

The search, edit, delete and add functions were coded using Flask and have seperate pages.

There is a search function and the option to search by recipe name or by
category name.

When the CRUD functions are used, the Mlab databse is update and the functions are stored.


### Features left to implement

The ability to upload images to each recipe is needed to add to the visuals of the website.

The ability to register, login and logout would be useful so that it is visible who
has created each recipe and to be able to remove CRUD functionality from all recipes
except your own.

## Testing

Unittest was used to test that all pages render correctly. To run the Unittest
enter ```python3 test.py``` into the terminal to see that all 7 tests pass.

The tests run can be found in the test.py file inside the home directory.

The load time was reduced by redicing the background image size on GIMP and
minifying the file on [CompressJPG](https://compressjpeg.com/).

The site is responsive on Mobile, Ipad and Desktop devices and also functions on multiple
browsers including FireFox, IE and Chrome.

User input errors have been tested by entering different values into the search
functions and by following links to navigate through the website and using the previous
and next page browser functions.


## Deployment

The app has been pushed to GitHub and delpoyed in Heroku. A requirements.txt file, a Procfile
and dynos were scaled. The IP and PORT used to run the website was
inserted into the config vars in heroku so that the app would push correcty.

The app is run by entering python3 app.py into the terminal or pressing the run button 
on the app.py page and then clicking on the link generated in the terminal.

To run the repository locally, you can download the files and upload them
to the editor of your choice or enter this into your terminal
```git clone https://github.com/marcuscistudent/recipe-book.git```.
Then install the requirements by entering this into your terminal ```pip install -r requirements.txt```.

## Credits

### Content
All written content is original with the exception of the 
recipe data which was taken from [here](https://www.bbcgoodfood.com/).

### Media
The Image was taken from [Pxhere](https://pxhere.com/).

GIMP was used to resize the background image and to reduce the image opacity.


### Acknowledgements

The responsive menu was found [here](https://materializecss.com/).

I used [CSS Tricks](https://css-tricks.com) to create a sticky footer.



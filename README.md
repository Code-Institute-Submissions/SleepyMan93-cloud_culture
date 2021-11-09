Cloud Culture

#### Code Institute Full Stack Development Dipoloma: Milestone Project 4 - Fullstack Framework
##### Created by William Donovan

![Project Displays](static/images/cover_photo.png)


# Table of Contents 

1. [UX Development](#uxdev)
   - Project Manifesto and Aim
   - User Stories 
   - Design Principles 
     * Fonts
     * Icons
     * Colours
     * Layout
   - Sitemap and Wireframes
   - Features and Future Implementations 
2. [Testing](#testing)
   - App Functionality Testing
      * Setting up Django Environment
      * Python App Views
      * Life Cycle
   - HTML, CSS and Python checks
      * HTML
      * CSS
      * Python
   - User Testing
   - Manual Testing
   - Automatic Testing
3. [Mongo Databse](#mongodb)
4. [Bugs / De-bugging / Syntax Issues](#bugs)
5. [Technologies Used](#languages)
   - Languages Utilised
   - Online Material
   - Tools and Databases Used
6. [Project Deployment](#deployment)
   - Process of Deployment
   - How to create Local Version
7. [References](#references)
8. [Acknowledgements](#acknowledge)


# UX Development <a name="uxdev"></a>

## Project Manifesto and Aim 
With a recent influx in vaping culture, especially over in the US, I decided to base my final project; an E-Commerce shop, around this culture. Over the last five years, not just myself but my Dad esepcially, has given up smoking in place of using E-cigarettes. Although they haven't been around for long enough to have done extensive research on them, the difference health wise it has done for us is incredible. I want Cloud Culture to not just be a place for buying vapes but put emphasis on the blog side, allowing users to post stories, information and awareness to help keep the culture growing but also safe. 

## User Stories
The target audience for this will be predominantly 18-50. Vaping in the UK is not illegal under the age of 18 but it is however illegal to sell to anyone under the age of 18.
## As an Unregistered User I want to:
* be able to browse through all the products and blog posts
* have the ability to add items to my bag
* be able to remove, ammend and update the bag
* be able to contact the site

## As a Registered User I want to:
* be able to fast checkout seeing as my details will already be stored/saved
* access my basic account details
* have the ability to make blog posts as my username
* have the ability to log in with my details
* be able to update my shipping and billing details
* be able to contact the site regarding an order

## As the Site Owner I want to:
* be able to log in to the Admin Panel
* be able to add, update or remove products, without vistiting the admin panel
* receive email notifications when a user submits through the contact page

# Design Principles

## Overall Feel
I wanted to create a site that reflects the name Cloud Culture but also the overall vape asthetic. To achieve this, my overall site will be based on white, which is a difference to my usual black/dark style. Hopefully this will make it feel more open and airy. 

## Fonts
   
## Icons

## Layout

# Sitemap / Wireframes

# Features / Future Implementations

--------------------

# Testing <a name="testing"></a>

## App Functionality Testing

### **Setting up Django environment**
To setup my Django framework and begin developmnent, I checked through four stages:
* Installed Django using **pip3 install django**
* Created the admin folders inside the main directory using **django-admin startproject (project name)**
* Made sure the server was working by starting it with **python3 manage.py runserver**
* Once I was shown a success Django message on Port8000, I made the inital database migrations with **python3 manage.py migrate**

### **Python App Views**
Process of setting up views with Django and Python:
* First setp was to initiate a home app using **manage.py startapp home** and insert a templates folder
* After creating the basic blocks ie. {% block content %} inside **index.html**, the next step is to create a view for this template inside the 'home' **views.py** - insert photo of basic first view
* From here, the **urls.py** content was copied from the main directory into another **urls.py** file inside the 'home' app template, to be used as a shell
* Once the path has been created in the 'home' **urls.py** file, a path to the shell is needed inside the project level **urls.py** file
* The last thing to do is add the 'home' app into **settings.py** and wire up the template directories (root and the custome allauth)

## Life Cycle
Upon setting up my Django environment and establising allauth is functional, the first step was to copy accross the allauth templates into my directory for customisation.
Inside the 'templates' folder is where these and my other frontend templates are stored. 

The next step was to create the 'home' app in which my 'index' and other frontend page views would be rendered from. After setting up my first app view, if working, the 'index.html' should render 'We Are Working' as a bootstrap success class. This helped with making sure not only the app view was working but also Bootstrap and the JS script tags.
- Insert screen shot of We Are Working

After setting up all my functionality, I could start to build the homepage. My first stage was to create a basic template using Bootstrap and some basic HTML. The process started by making a header for nav links, search bar and logo, the main banner image container and the basic 'Shop Now' button. Once all these components were working and in place, I linked my **base.css** style sheet to the **base.html** file and styled the content. Below is an image of the groundwork used to build the homepage:
- insert image homepage_basic

The next process of my build was to create some "json" fixtures for my products and categpories to go. At first I was slightly confused how to make these from scratch but after making my mentor Gerry explained the "many to one" and "one to many" theory with database structure, the schema made sense which in turn, helped build the models and fixtures. After making the initial 7 categories, I tried adding my products via the admin panel on the site. Unfortuantely, only the images uplaoded transferred into the project directory, the "json" file was not updated with product information. From here, I manually built the product fixture and input, two sets of item data to test it was pulling through. Following the cmd "python3 manage.py loaddata products", on the products page I was met with two product query sets as text, which indicated success, see image below:
- insert image of query set product page

Once I knew the product query sets were loading, I could move on to creating the products in the "products.json" and render the fixtures on to the "all_products" template page. Bar the uncentered line, everything pulled through well from the backend and all the product images, price and other information were displayed on the page as should be:
- insert image of all products page

## HTML CSS and Python validation checks

### HTML

### CSS

### Python

## User Testing 

## Manual Testing

✔️ Navigation links: All redirect to the correct pages.

✔️ Footer links: All redirect to the correct pages.

✔️ Try deleting Posts when not logged in: A 403 error page appears asking user to log in/register.

✔️ Try loading an unrecognised link page: A 404 error page appears sending the user back to the homepage.

✔️ Submit registration form with a user/email that already exists in database: User is prevented from signingin. A flash message is produced stating the username already exists.

✔️ Submit registration form with one of the fields not filled in: An error message appears asking user to fill in the field.

✔️ Submit registration form with a new user/email that doesn't exist in database: Successfully sends user data to MongoDB and redirects user to the Home page. 

✔️ Submit Log In form if no username exists in database that matches entered username: Error message appears stating incorrect username and/or password.

✔️ Submit Log In form if username is correct but password doesn't match: User is prevented from signing in. An Error message appears stating incorrect username and/or password.

✔️ Submit Log In form with one of the fields not filled in: An error message appears asking user to fill in the field.

✔️ Submit log in form with correct username and password: Starts session and takes user to the Home page. 

✔️ Press the Sign Out button when logged in: Ends the session and sends user back to login.html. 

✔️ Try adding a post when logged in: Successfully creates a post and redirects user to their Profile page only if all the fields are filled in correctly. 

✔️ Try editing a post on the My Account page: Successfully renders in original game information, updates post and renders the new information on the edit page only if all the fields are filled in correctly. If not, an error message appears.

✔️ Try deleting a post while on the Profile page: User successfully deletes post and is taken back to their profile with the post removed

✔️ Search posts on site: If results found, post is rendered on the home page. If no results, message stating no results found and a return to home page button produced. 

✔️ Try logging in with the credentials from the deleted account: Get an error message. 

## Automatic Tetsing

# Bugs / De-Bugging / Syntax Issues<a name="bugs"></a>

## Errors
After initialising my **index.html** file and adding the installed view/app, I was met with a 'TemplateDoesNotExist' page. The server started correctly but the path I made seemed to cause the error:
- photo of error page
   To resolve the issue, I understood the error was not arising from the Python App View or code because the server ran with no issue. The problem lied within my filepath. The **index.html** file was not in the 'templates/home' folder but actually just inside 'templates'. The filepath should be **app_name > templates > app_name > index.html**

Found an error with my filter query functionality. The 'mods' category was correctly displaying all items in category pk1 / mods but none of the other categories displayed their products correctly. By deleting all the product urls but copying the mods syntax because I knew this one was rendering correctly, I was able to resolve the issue. I pasted "{% url 'products' %}?category=mods" back into the anchor href, reloaded the page and the **mods** product page was rendering correctly. Then by pasting in this syntax to the other anchor links, just changing the category name, I was able to determine that the "accessory" page was the only one not working. I left this out from the "All Products" query and this page now loaded successfully with all the "Mod" and "Disposbale" vape products. 

When creating a pathfile in **setting.py** for my static folder, the "STATICFILES_DIR" produced this error:
- insert static_dir_error
To rectify the issue, as per the error message, I made the "STATICFILES_DIR" os.path into a tuple with this syntax | **STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)**

## Bugs
Encountered my first bug when building the homepage template. Everything appeared on screen as expted, with the search fucntion returning "q='search input'" signalling success but the dropdown functionality wasn't present. 
- insert photo dropdown_bug
The bug fix was due to JS and using Bootstrap 4 classes when I installed Bootstrap 5 with this project. To correct the issue, in Bootstrap 5, the "data-toggle" class has now been changed to "data-bs-toggle", the dropdown functionality is now working. 

When testing the responivness of my current elements, mainly the navbar section, I found two scaling issues. Using 'includes' I made a seperate HTML file for the navbar on mobile, essentially collapsing the content into icons. Using **d-block** and **d-lg-none**, the idea was to use template literals and inject the seperate HTML file after the standard navbar and for it to only show on small sizes and below. However, the ul was still showing as block, pushing the main-nav links right of center. Also when using dev tools, the icon and content appeared on a seperate line from the main-nav expandable dropdown. The image below demonstrates this:
- insert responsive-bug image

Found an issue when first rendering the "all products" page. As you can see from the image, the parent div has a class of "text-center" which should include line breaks. However, even with this class the line break wouldn't center under the page title: 
- insert screen shot of off center hr rule

Encountered a bug when trying to render an individual product page. I was met with a NameError, I believe to be originating from the product.views file:
- insert screen shot single_product_bug
The bug fix was found on line 24 as the error suggested. As I used the "all_products" view as the shell for the "product_details" view, I forgot to remove the s from the line "product = get_object_or_404(Product, pk=product_id)" meaning **'product': product,** could not be defined.



# Technologies Used <a name="languages"></a>

1. [jQuery](https://jquery.com/)
2. [Materialize](https://https://materializecss.com/)
3. [CSS 4](https://www.w3schools.com/w3css/)
5. [HTML 5](https://en.wikipedia.org/wiki/HTML5)
6. [JavaScript](https://www.javascript.com/)
7. [Dev Tools](http://ami.responsivedesign.is/)
8. [jQuery](https://jquery.com/)
9. [Python](https://www.python.org/)
10. [MongoDB](https://www.mongodb.com/)
11. [Heroku](https://heroku.com)
12. [Flask](https://flask.palletsprojects.com/en/2.0.x/)

# Project Deployment <a name="deployment"></a>
## Process of deployment

#### Heroku:  

1. _For the Heroku app to successfully understand what **Framework Requirements** and Python applications to run, a **Procfile** and **requirements.txt** are a must..._  

Using the command **pip3 freeze --local > requirements.txt** in the terminal will create a requirements.txt file with all the dependencies listed to run the Heroku App. Whenever new packages are installed, remeber to update the .txt file | Using the command **echo web: python app.py > Procfile** in ther terminal will create a Procfile, which Heroku uses to know which Python App to run when the site is loaded.  

2. _After initial set up of the Flask app, our next step is to get Heroku to update, recognise and connect with our site..._  

To do this, you need to make an account on Heroku, upon signing in, click **New** to create the app. On the next screen, produce a name for the app, making sure to use lowercase and the region closest to you. If the domain name is available, finish by clicking **Create App**.  

3. _Next we need to have our code update on Heroku automatically. The easiest way to do this is linking the sites repo in Github with the Heroku app..._  

Navigate to the **Deploy** tab and choose **github** as the **Deployment Menthod**. Sign in and Search for the repo name. Once found, choose **connect**.  

4. _Due to the fact we have hidden KEY Environment Variables in the **env.py** file, that Heroku won't be able to retrieve from the **GitHub Repo**, we need to store this in Herkou's **Config Vars**..._  

Under the settings tab you will find the **Config Vars** section. Reveal the section and copy all the **KEY** and **VALUE** pairs from the **env.py** file. Making sure not to include any of the **quotation marks**.  

5. _For the last stage, it is key to make sure the **requirements.txt** and **Procfile** are pushed to the GitHub Repo..._   

Once these files are successfully pushed to GitHub, make sure to **Enable Automatic Deploy**. You can then click **Deploy Branch**, generally **main** or **master**. The Heroku app will take a few minutes to set up the connection. Once successful, every commit pushed to GitHub will update the Heroku app and Live Site.

## How to create Local Version

#### Clone the repository and run locally:

1. Navigate to the repository from the Github Dashboard
1. Select the "Code" button, top right of the frame 
1. Click on the clipboard icon to the right of the URL to copy it
1. Open an Integrated Development Environment (IDE) and head over to the terminal
1. Change the directory to where you want to clone the repository to
1. Execute the following command by pasting in the URL you copied in step 3: git clone https://github.com/SleepyMan93/escro-games
1. Press Enter
1. The site will then be cloned
1. Install all the project dependencies by typing `pip install -r requirements.txt`

#### Set Up Environment Variables:

1. Create an env.py file in your root directory. **touch env.py** in the terminal.
1. Type env.py into the.gitignore file and click save.
1. Add the following to your env.py file with the applicable variables: 
```
import os
os.environ["MONGO_URI"] = "mongodb+srv://username:password@myfirstcluster-strtg.mongodb.net/plant_swap?retryWrites=true&w=majority"
os.environ["IP"] = "0.0.0.0"
os.environ["PORT"] = "5000"
os.environ["SECRET_KEY"] = "Your Secret Key"
```

[Back to Top](#table-of-contents)


# References <a name="references"></a>
- Aside from [StackOverflow](htttps://www.stackoverflow.com) and some basics from the Code Institute Mini Project, all the code was produced by me.

# Acknowledgements <a name="acknowledge"></a>
I'd really love to thank Gerry my Tutor for helping me with my project. He gave me some great insight into principles, structure and 
overall any problems I had. 

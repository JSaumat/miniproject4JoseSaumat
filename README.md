# miniproject4JoseSaumat

### INF601 - Advanced Programming in Python
### Jose Saumat
### Mini Project 4


# Mini Project 4

## Description

This project will be using a combination of Django, BootStrap, HTML/Jinja, and CSS to create a mini website.

## Getting Started

First clone the repository into your preferred IDE. Make sure to also create a virtual environment for the project if 
your IDE does not automatically create one for you.

### Dependencies

Step 1: Install required packages using the requirements.txt file. Copy and paste the code below into the terminal.

```
pip install -r requirements.txt
```
Step 2: Initialize the SQL database. Copy and paste the code below into the terminal.

```
python manage.py makemigrations (this will create any SQL entries that need to go into the database)
python manage.py migrate (this will apply the migrations)
python manage.py createsuperuser (this will create the administrator login for your /admin side of the project)
```

### Executing program

Step 3: Run the program. Copy and paste the code below into the terminal.

```
python manage.py runserver

or

Click the Play button in your IDE.
```

Step 4: In your terminal you should now see a hyperlink with the address below. Click that link to launch website in browser.

```
http://127.0.0.1:8000
```

### Output

For The Regular User:

This website should take you to the home page where you should be able to vote on movies. In order to vote, you must register.
The site also contains a fully functional registration, log in, and log out page. You can also read the about page which contains a 
brief description of the site along with credit for TMDB's use of their API, and it doubles as a link to their site. The search bar
in the navigation menu allows you to use TMDB's API to search for movies in their API without adding them to the home page for voting.

For Admin User:

You have access to everything above, but you also gain access to the Add Movie and Admin pages. The Add Movie page will allow you
to add movies that the regular users can vote on. The Admin page will let you see a list of movies, the users, and set access for
different groups.

## Authors

Contributors names and contact info

- Jose Saumat
- Jason Zeller (via Tutorials)

## Acknowledgments

Inspiration, code snippets, etc.
* [Jason Zeller](https://www.youtube.com/watch?v=lo5atoJdNX8)
* [Jason Zeller](https://www.youtube.com/watch?v=piyfP2NLp9A)
* [Jason Zeller](https://www.youtube.com/watch?v=UB7XFf0Q_M4)
* [Jason Zeller](https://www.youtube.com/watch?v=lSqCJqnwCb8&list=PLE5nOs3YmC2RqZfmOSoOM4iqmed2pudrg&index=17)
* [Jason Zeller](https://www.youtube.com/watch?v=KPx2F812vGc&list=PLE5nOs3YmC2RqZfmOSoOM4iqmed2pudrg&index=20)
* [Jason Zeller](https://www.youtube.com/watch?v=VHkIzFJCU-0&list=PLE5nOs3YmC2RqZfmOSoOM4iqmed2pudrg&index=20)

API and Package documentation
* [TMDB API](https://www.themoviedb.org/)
* [Django](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)
* [Jinja](https://jinja.palletsprojects.com/en/stable/)
* [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [W3 Schools HTML](https://www.w3schools.com/html/default.asp)
* [W3 Schools CSS](https://www.w3schools.com/css/default.asp)
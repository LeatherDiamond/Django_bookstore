## Project description.

Web applicaton of a bookstore intended for the sale of paper books online. 
The bookstore is a showcase of available products (catalogue) and provides all necessary information and tools for choosing and ordering goods.
The bookstore enables shop personnel to receive and process orders and provides the possibility for the customers to follow the status of their orders.

Applied technologies: Python, SQLite, Django, HTML, CSS, JavaScript.


## How to start?

**1. Clone current repository on your local machine:**
```
git clone https://github.com/LeatherDiamond/ITacademy.git
```

**2. Install all requirements from "requirements.txt".**
```
pip install -r requirements.txt
```
**3. Apply all migrations:**
```
python manage.py migrate
```
**4. Collect static files:**
```
python manage.py collectstatic
```

**5. Provide mandatory data in rhe following files:**
 - [x] settings.py:
    - Django SECRET_KEY;
    - SOCIAL_AUTH_GOOGLE_OAUTH2_KEY;
    - SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET;
    
*The last two options will allow users to login with google without additional registrations.*

***Note that *"SOCIAL_AUTH_GOOGLE_OAUTH2_KEY"* and *"SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET"* will be available only after following a few steps in Google API console. For more details please check [documentation](https://developers.google.com/identity/protocols/oauth2?hl=en).***

   - [x] src -> order -> views.py:
      - line 34 - client ("Courier" secret token that will allow the application to send notification mails to managers group when someone is creating an order);
      - line 38 - email (Enter an email address where notifications will be sent);
      - line 47 - link (Enter link that you want to be displayed in text of notification mail);
      
***Note that *"Courier secret token"* will be available only after following a few steps on [Courier website](https://www.courier.com/).***

**6. Create a superuser to have access to the admin panel.**
```
python manage.py createsuperuser
```

***7. Launch the project on a development server to see all the functionality before deploying it on real server.***
```
python manage.py runserver
```


## Detailed functionality description.

![This is an image](https://github.com/LeatherDiamond/ITacademy/blob/master/Diagram%20of%20the%20ordering%20process.drawio.svg)


## Why should you try it?

***It's a great project that will meet most customer needs, is simple and easy to use, and has the rich functionality that an online shop so desperately needs.***

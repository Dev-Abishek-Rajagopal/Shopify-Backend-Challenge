# Shopify-Backend-Challenge

<b><h2>||     DB Structure/Models    ||</b></h2>

<b><h3>     RepUser    </b></h3>

 |------------|
 | email      |  
 | username   |  
 | firstname  |
 | lastname   |
 | is_staff   |     ----->  RepUser if is_staff = "Yes" ==> Can access Django Admin 
 | is_active  |
 |____________|
 
 <b><h3>     ImgRep    </b></h3>

 |----------------|
 | img            |  
 | name           |  
 | user           |    ----->  RepUser foreign key
 | scope          |
 | price          |
 | discount       |
 | color_palette  |    ----->  colors that are dectected from the Uploaded Image
 |________________|
 
  <b><h3>     ImgCart    </b></h3>

 |----------|
 | img      |    ----->  ImgRep foreign key
 | user     |    ----->  RepUser foreign key
 | quantity |
 |__________|


<b><h2>||     Django/Framework Configuration    ||</b></h2>

<b><h3>Python 3.6 :</b></h3> https://www.python.org/downloads/

<b><h3>Django 3.latest :</b></h3> pip3 install Django

<b><h3>Django Rest framework :</b></h3> pip3 install djangorestframework

<b><h3>Django Rest framework JSON API:</b></h3> pip3 install djangorestframework-jsonapi

<b><h3>Pillow :</b></h3> pip install Pillow ( Python Imaging Library )

<b><h3>Webcolors :</b></h3> pip install webcolors ( webcolors is a module for working with HTML/CSS color definitions. )


<b><h2>||     Searching Image    ||</b></h2>

--->  with IMAGE_NAME and SCOPE = "public"
--->  with IMAGE_NAME, SCOPE = "private" and USER_NAME
--->  with COLOR_PALETTE and SCOPE = "public"
--->  with COLOR_PALETTE, SCOPE = "private" and USER_NAME

<b><h2>||     Directory Structure    ||</b></h2>

\---imgrep
    |   .coverage
    |   db.sqlite3
    |   manage.py
    |   
    +---App                                                 ------> App Folder
    |   |   admin.py                                        ------> Python/Django Admin configrations
    |   |   apps.py
    |   |   models.py                                       ------> DB models are defined here
    |   |   serializers.py                                  ------> Allow complex data such as querysets and model instances to be converted to native Python datatypes
    |   |   tests.py
    |   |   urls.py                                         ------> Sub url folder for API
    |   |   views.py
    |   |   __init__.py
    |   |   
    |   +---migrations
    |   |      0001_initial.py
    |   |      0002_repuser_is_superuser.py
    |   |      0003_auto_20210919_0245.py
    |   |      0004_imgcart_imgrep.py
    |   |      0005_imgrep_color_palette.py
    |   |      0006_alter_imgcart_img.py
    |   |      0007_remove_imgcart_img.py
    |   |      0008_imgcart_img.py
    |   |      __init__.py  
    +---imgrep                                              ------> Project Folder
    |   |   asgi.py
    |   |   settings.py                                     ------> File contains Django config/settings
    |   |   urls.py                                         ------> Main url folder for API
    |   |   wsgi.py
    |   |   __init__.py
    |   |   
    |   \---__pycache__
    |           settings.cpython-39.pyc
    |           urls.cpython-39.pyc
    |           wsgi.cpython-39.pyc
    |           __init__.cpython-39.pyc
    |           
    +---logs                                                ------> log Folder                     
    |       debugger.log
    |       system.log
    |       task.log
    |       
    +---media                                               ------> Uploaded images are stored here 
    |   \---ImgRep
    |           1.jpg
    |           12.jpg
    |           12_3CPqN3C.jpg


<b><h2>||     Run Django Framework    ||</b></h2>

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

<b><h2>||     API Collections    ||</b></h2>

GET request : http://{HOST}/repapp/user/ --> List of all Users
POST request : http://{HOST}/repapp/user/ --> Register Users

GET request : http://{HOST}/repapp/user/{id} --> Get particular User
PUT request : http://{HOST}/repapp/user/{id} --> Update particular User
DELETE request : http://{HOST}/repapp/user/{id} --> Delete particular User


GET request : http://{HOST}/repapp/img/ --> List of all Images
POST request : http://{HOST}/repapp/img/ --> Register Images

GET request : http://{HOST}/repapp/img/{id} --> Get particular Images
PUT request : http://{HOST}/repapp/img/{id} --> Update particular Images
DELETE request : http://{HOST}/repapp/img/{id} --> Delete particular Images

GET request : http://{HOST}/repapp/cart/ --> List of all Cart
POST request : http://{HOST}/repapp/cart/ --> Register Cart

GET request : http://{HOST}/repapp/cart/{id} --> Get particular Cart
PUT request : http://{HOST}/repapp/cart/{id} --> Update particular Cart
DELETE request : http://{HOST}/repapp/cart/{id} --> Delete particular Cart

GET request : http://{HOST}/repapp/search/ --> Filter Images based on Query Params search( search text ) and user (User requested) 




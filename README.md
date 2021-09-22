# Shopify-Backend-Challenge

<b><h2>||     DB Structure/Models    ||</b></h2>

<b><h3>     RepUser    </b></h3>

 |------------| <br>
 | email      |  <br>
 | username   |  <br>
 | firstname  |<br>
 | lastname   |<br>
 | is_staff   |     ----->  RepUser if is_staff = "Yes" ==> Can access Django Admin<br> 
 | is_active  |<br>
 |____________|<br>
 
 <b><h3>     ImgRep    </b></h3>

 |----------------|<br>
 | img            |  <br>
 | name           |  <br>
 | user           |    ----->  RepUser foreign key<br>
 | scope          |<br>
 | price          |<br>
 | discount       |<br>
 | color_palette  |    ----->  colors that are dectected from the Uploaded Image<br>
 |________________|<br>
 
  <b><h3>     ImgCart    </b></h3>

 |----------|<br>
 | img      |    ----->  ImgRep foreign key<br>
 | user     |    ----->  RepUser foreign key<br>
 | quantity |<br>
 |__________|<br>


<b><h2>||     Django/Framework Configuration    ||</b></h2>

<b><h3>Python 3.6 :</b></h3> https://www.python.org/downloads/

<b><h3>Django 3.latest :</b></h3> pip3 install Django

<b><h3>Django Rest framework :</b></h3> pip3 install djangorestframework

<b><h3>Django Rest framework JSON API:</b></h3> pip3 install djangorestframework-jsonapi

<b><h3>Pillow :</b></h3> pip install Pillow ( Python Imaging Library )

<b><h3>Webcolors :</b></h3> pip install webcolors ( webcolors is a module for working with HTML/CSS color definitions. )


<b><h2>||     Searching Image    ||</b></h2>

--->  with IMAGE_NAME and SCOPE = "public"<br>
--->  with IMAGE_NAME, SCOPE = "private" and USER_NAME<br>
--->  with COLOR_PALETTE and SCOPE = "public"<br>
--->  with COLOR_PALETTE, SCOPE = "private" and USER_NAME<br>

<b><h2>||     Directory Structure    ||</b></h2>

\---imgrep<br>
    |   .coverage<br>
    |   db.sqlite3<br>
    |   manage.py<br>
    |   <br>
    +---App                                                 ------> App Folder<br>
    |   |   admin.py                                        ------> Python/Django Admin configrations<br>
    |   |   apps.py<br>
    |   |   models.py                                       ------> DB models are defined here<br>
    |   |   serializers.py                                  ------> Allow complex data such as querysets and model instances to be converted to native Python datatypes<br>
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




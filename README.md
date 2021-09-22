# Shopify-Backend-Challenge

<b><h2>||     DB Structure/Models    ||</b></h2>

<b><h3>     RepUser    </b></h3>

 |------------| <br>
 <p>| email      |</p>  <br>
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
    |   |   tests.py<br>
    |   |   urls.py                                         ------> Sub url folder for API<br>
    |   |   views.py<br>
    |   |   __init__.py<br>
    |   |   <br>
    |   +---migrations<br>
    |   |      0001_initial.py<br>
    |   |      0002_repuser_is_superuser.py<br>
    |   |      0003_auto_20210919_0245.py<br>
    |   |      0004_imgcart_imgrep.py<br>
    |   |      0005_imgrep_color_palette.py<br>
    |   |      0006_alter_imgcart_img.py<br>
    |   |      0007_remove_imgcart_img.py<br>
    |   |      0008_imgcart_img.py<br>
    |   |      __init__.py  <br>
    +---imgrep                                              ------> Project Folder<br>
    |   |   asgi.py<br>
    |   |   settings.py                                     ------> File contains Django config/settings<br>
    |   |   urls.py                                         ------> Main url folder for API<br>
    |   |   wsgi.py<br>
    |   |   __init__.py<br>
    |   |   <br>
    |   \---__pycache__<br>
    |           settings.cpython-39.pyc<br>
    |           urls.cpython-39.pyc<br>
    |           wsgi.cpython-39.pyc<br>
    |           __init__.cpython-39.pyc<br>
    |           <br>
    +---logs                                                ------> log Folder <br>                    
    |       debugger.log<br>
    |       system.log<br>
    |       task.log<br>
    |       <br>
    +---media                                               ------> Uploaded images are stored here <br>
    |   \---ImgRep<br>
    |           1.jpg<br>
    |           12.jpg<br>
    |           12_3CPqN3C.jpg<br>


<b><h2>||     Run Django Framework    ||</b></h2>

python manage.py makemigrations<br>

python manage.py migrate<br>

python manage.py runserver<br>

<b><h2>||     API Collections    ||</b></h2>

GET request : http://{HOST}/repapp/user/ --> List of all Users<br>
POST request : http://{HOST}/repapp/user/ --> Register Users<br>

GET request : http://{HOST}/repapp/user/{id} --> Get particular User<br>
PUT request : http://{HOST}/repapp/user/{id} --> Update particular User<br>
DELETE request : http://{HOST}/repapp/user/{id} --> Delete particular User<br>


GET request : http://{HOST}/repapp/img/ --> List of all Images<br>
POST request : http://{HOST}/repapp/img/ --> Register Images<br>

GET request : http://{HOST}/repapp/img/{id} --> Get particular Images<br>
PUT request : http://{HOST}/repapp/img/{id} --> Update particular Images<br>
DELETE request : http://{HOST}/repapp/img/{id} --> Delete particular Images<br>

GET request : http://{HOST}/repapp/cart/ --> List of all Cart<br>
POST request : http://{HOST}/repapp/cart/ --> Register Cart<br>
<br>
GET request : http://{HOST}/repapp/cart/{id} --> Get particular Cart<br>
PUT request : http://{HOST}/repapp/cart/{id} --> Update particular Cart<br>
DELETE request : http://{HOST}/repapp/cart/{id} --> Delete particular Cart<br>

GET request : http://{HOST}/repapp/search/ --> Filter Images based on Query Params search( search text ) and user (User requested) <br>




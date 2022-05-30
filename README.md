# django_photo_gallery
## Description
It is a Django app to show and manage images grouped in galleries(inspired by pintrest).
It is a web application that let you do the previous. Perfect option for people who just need a simple portfolio page and only want to focus on their work (artists, photographers, designers, painters).


#### Features
1. Python: programming language.
2. Django: web framework.
3. Bootstrap: front-end framework.
4. Javascript -programming language


### Directory tree
web
   - django-photo_gallery
    - deploy - contains sample files used when deploying on apache server.
   - gallery- base application folder.
        * settings.py - the configuration file.
    - photos.
    - static- where the pictures you upload and their miniatures are stored.

### Installation
1. Clone this Github repository:
''' 
    git clone https://github.com/kmollee/gallery.git

     cd Django_photo_gallery


'''
2. Install the pre-requisites:

''' 
      
      pip install -r requirements.txt

'''


3. Copy the settings template to create your local settings:

''' 
    cp gallery/settings_local.template gallery/settings_local.py


'''


4. Edit the local settings file with your settings:
''' 
     vi gallery/settings_local.py


'''


5. Create the database and admin user:
''' 
    python manage.py syncdb


'''



6. Collect static files:
''' 
   python manage.py collectstatic

'''


Configure your web server to serve static files from the directory specified in the local settings file. See the following Django documentation 



Launch the application using the built-in runserver, or deploy using gunicorn, which is the application server of choice:

'''
web: gunicorn gallery.wsgi --log-file -

'''

#### Known Bugs
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.

### Author
~ julia Mwangi

### Licence
Click this [link](LICENSE) to view licence information.

### Contact Information
juliahwambui3@gmail.com
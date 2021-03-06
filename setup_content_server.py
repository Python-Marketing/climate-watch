#!/usr/bin/env python

import glob
import os
import shutil
from datetime import datetime
try:
    from django.conf import settings
    import django

    # Initialise django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_server.settings")
    django.setup()
    database = getattr(settings, 'DATABASE_NAME')
    # Need to see if at least one user is added

except:
    pass


# timestamp used
timestamp = str(datetime.now()).replace(" ", "")
# Get name from settings




def setup_server():
    # Setup the django handling
    # only use this if not using Pycharm or another way of running the server
    runserver = False
    # Do you need to migrate the database? Safer to leave True
    # if you have changed models it must be True
    migrate = True
    # Do you need to backup the database? Safer to leave True (We are using sqlight)
    backup = False
    # How many as in how many copies since script is run.
    no_backups = 1
    # Get pip involved?
    install_requirements = True
    # This deletes the database creating a reset copy on the last database
    # Use wisely...
    reset = True
    # This runs the custom script in site_server/management initialize_cms.py
    add_default_content = True
    add_web_content = True
    """
    No need to edit anything further down unless you are expanding
    """
    # need to install django before we can access it install requirements
    if install_requirements:
        # Its a large application might take time
        os.system("pip install -r requirements.txt")

    # NB development only
    if reset:
        # Lets save that database just in case, we are removing them and backups
        try:
            shutil.copyfile(database, database + timestamp + '.reset')
        except:
            os.system('echo "Error : {}"'.format('No database yet...'))

        # Bye Bye data
        os.system("rm *.back")
        os.system("rm *.db")
        # Force migrate
        migrate = True

    if migrate:
        # Check API for makemigrations and migrate skips sometimes
        os.system("python3 manage.py makemigrations")
        os.system("python3 manage.py makemigrations api")
        os.system("python3 manage.py migrate")
        os.system("python3 manage.py migrate api")
        os.system("python3 manage.py collectstatic")
        # Edit these details for you use cas
        superuser = 'developer'
        superuser_email = 'django.python.pro@gmail.com'
        superuser_password = 'password'
        from django.contrib.auth.models import User
        if User.objects.count() == 0:
            # Create superuser
            User.objects.create_superuser(superuser, superuser_email, superuser_password)

    if backup:
        # We get the current dir count the backups
        path = str(os.getcwd())
        backup_counter = len(glob.glob1(path, "*.back"))
        # lets the user know what going on
        os.system('echo "Path : {}"'.format(path))
        os.system('echo "Backups : {}"'.format(backup_counter))
        # If their are to many backups, rm them
        if backup_counter > no_backups:
            os.system("rm *.back")
        # Make the backup
        shutil.copyfile(database, database + timestamp + '.back')

    # Easy way to add content
    if add_default_content:
        # Adds image options and some blogs for display.
        # Can be used to add more content
        os.system("python3 manage.py initialize_cms")

    # Web Content
    if add_default_content:
        # Adds image options and some blogs for display.
        # Can be used to add more content
        os.system("python3 manage.py search_web")
        os.system("python3 manage.py process_search_web_results")

    # Run this baby?
    if runserver:
        os.system("python3 manage.py runserver")


setup_server()

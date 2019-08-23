#!/usr/bin/env python

# backup_script.py
"""
To be excecuted once per day for data backup.
Note: This kind of works in the same space/ dir as manage, so you need to add
the subdir weher this needs saved in. Otherwise it will be like you saved
in the project folder after running manage.py
https://docs.djangoproject.com/en/2.2/topics/settings/#either-configure-or-
django-settings-module-is-required
Explains why you need to have the two setup statements below.

"""
### ISSUES ###
"""
Not working,. I think the settings is the issue, but the documemntation makes it
seem like it should be pulling in the default info. I am getting no errors. Just
completely empty data.

test: remove the std out and print to the terminal? Or just dump anywhere else.
Nothing, prints blank

TWO: os.environ.set_default().  Check the cwd first.

WORKING!! Setting the environ var fixed the issue. 
"""
### ###



import os
from datetime import date
from django.core.management import call_command
from django.conf import settings
# from my_app import myapp_defaults
import django

# test two
import sys

if __name__ == '__main__':

    ## TWO
    print(sys.path)
    # Append to this to look for the files to work on.
    path_to_settings = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #path_to_settings = os.path.join(path_to_settings, 'recap')
    sys.path.append(path_to_settings)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recap.settings')

    # Setup
    #settings.configure()
    # setup_environ(settings)
    django.setup()


    # Create the filename
    add_date = date.strftime(date.today(), '%m%d%Y')
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filename = 'datadump' + add_date + '.json'
    filename = os.path.join(base_dir, filename)

    # call_command to creaete the file from the stdout
    # Currently written as a complete backup of the DB
    with open(filename, 'w') as fileObject:
        call_command('dumpdata', stdout = fileObject)

    #call_command('dumpdata')

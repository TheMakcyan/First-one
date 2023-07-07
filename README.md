For detailed installation instructions, consult the docs.
First of all you need to install Django. To do this run:
pip install django
To install and start the local server for development, simply run:

cd django
py -m venv mysite

And put files from archive into mysite directory and then type:
Scripts\Activate.ps1

Then inside your virtual envirement install other requried packages:
pip install djangorestframework 
pip install drf-spectacular

After that type:
py manage.py runserver 
And go to http://localhost:8000 to see content

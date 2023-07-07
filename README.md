For detailed installation instructions, consult the docs.
First of all you need to install Django. To do this run:
```shell
python3 -m pip install -r requirements.txt
```
To install and start the local server for development, simply run:
```shell
cd django
py -m venv mysite
```
And put files from archive into mysite directory and then type:
```shell
Scripts\Activate.ps1
```
Then inside your virtual envirement install other requried packages:
```shell
pip install djangorestframework 
pip install drf-spectacular
```
After that type:
```shell
py manage.py runserver
```
And go to http://localhost:8000 to see content

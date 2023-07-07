For detailed installation instructions, consult the docs.
To install and start the local server for development, simply run:
```shell
py -m venv mysite
```
And put files from archive into mysite directory and then type:
```shell
Scripts\Activate.ps1
```
Then you need to install required packages. To do this run:
```shell
python3 -m pip install -r requirements.txt
```

After that type:
```shell
py manage.py runserver
```
And go to http://localhost:8000 to see content

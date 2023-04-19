UNIX/MAC OS:
Run `source sourcevenv.sh` script to initialize the python virtual environment

Windows:
1. At ./Delivery4, Run `py -m venv myworld`
2. Run `sourcevenv.bat` script to initialize the python virtual environment

Run `deactivate` to exit the python venv

Upon first time installing Django in  venv, do `py manage.py makemigrations` and  `py manage.py migrate`\
To run the server, navigate to the TAMonitor folder and run `py manage.py runserver`

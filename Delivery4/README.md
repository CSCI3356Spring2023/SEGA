UNIX/MAC OS:
Run `source sourcevenv.sh` script to initialize the python virtual environment

Windows:
1. At ./Delivery4, Run `py -m venv myworld`
2. Run `sourcevenv.bat` script to initialize the python virtual environment

Run `deactivate` to exit the python venv

To run the server, navigate to the TAMonitor folder and run `python3 manage.py runserver`


Fixes:
1. Restructured views so that now we can customize login to allow student, instructors, and admins to login to their own landing page.
2. urls for accounts are reorganized to behave more properly on navigating among login, logout, and landing pages
3. deleted useless directories

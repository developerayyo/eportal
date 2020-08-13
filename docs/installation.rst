============
Installation
============

1. fork this `Repo <https://github.com/developerayyo/eportal/>`_  to your github account

2. Clone the forked version on your system  by running the following command from the command line ``git clone https://github.com/<your-username>/eportal``

3. Go into the repo dir : ``cd eportal``

4. Create and activate your python virtual environment on linux ``python3 -m virtualenv myenv && source myenv/bin/activate``. If you are on windows ``virtualenv myenv && myenv\Scripts\activate``

5. while in the project directory, Install the requirements with the following command: ``pip3 install -r requirements.txt``

6. Then create a superuser for django: on linux run: ``python manage.py createsuperuser``. On windows ? run: ``py manage.py createsuperuser`` then follow the on-screen prompts.

7. Finally run: on linux: ``python manage.py runserver``. On windows: ``py manage.py runserver`` boom! you have the project up and running.
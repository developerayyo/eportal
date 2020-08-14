=============================================================
Django Powered University Course and Result Management System
=============================================================

Installation
============

1. fork this `Repo <https://github.com/developerayyo/eportal/>`_  to your github account

2. Clone the forked version on your system  by running the following command from the command line ``git clone https://github.com/your-username/eportal``

3. Go into the repo dir : ``cd eportal``

4. Create and activate your python virtual environment on linux ``python3 -m virtualenv myenv && source myenv/bin/activate``. If you are on windows ``virtualenv myenv && myenv\Scripts\activate``

5. while in the project directory, Install the requirements with the following command: ``pip3 install -r requirements.txt``

6. Then create a superuser for django: on linux run: ``python manage.py createsuperuser``. On windows ? run: ``py manage.py createsuperuser`` then follow the on-screen prompts.

7. Finally run: on linux: ``python manage.py runserver``. On windows: ``py manage.py runserver`` boom! you have the project up and running.

Staying up-to date with this repo
=================================

1. kindly *watch* this repo by clicking the watch button above so as to get notified whenever commits are made or when new issues are raised and so on.

2. on your local machine, run ``git remote add upstream git@github.com/developerayyo/eportal.git``

3. lastly, run ``git pull``

Want to Contribute
==================

1. create and switch to your branch by running: ``git checkout -b <your-name>``

2. after you've made some changes, add and commit your changes ``git add . && git commit -m "<your-commit-message>"``

3. push the commits to your branch ``git push origin <your-branch-name>``

4. Nice work. so go to your github page and make pull request, wait for some time while the admin reviews and merge your pull request.

Documentation
=============

Click `here <https://eportalproject.readthedocs.io/en/latest/index.html>`_ to dive into project documentation.

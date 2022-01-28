====================================================================
Automated Result Processing System (ARPS)
====================================================================

|repo-size| |licence| |website| |docs| |build| |codecov|

**ARPS** is a Project I developed *(with Python and Django Web Framework)* in partial fulfilment of the requirements for the award of Bachelor's degree in Computer Science of **Adeleke University Ede, Nigeria**.



Documentation
=============

I make use of Readthedocs.io to manage the documentation and you can click `docs <https://eportalproject.readthedocs.io/en/latest/index.html>`_ to dive into the project documentation.


Installation
============

1. fork this `Repo <https://github.com/developerayyo/eportal/>`_  to your github account

2. Clone the forked version on your system  by running the following command from the command line ``git clone https://github.com/your-username/eportal``

3. Go into the repo dir : ``cd eportal``

4. Create and activate your python virtual environment on linux ``python3 -m virtualenv myenv && source myenv/bin/activate``. If you are on windows ``virtualenv myenv && myenv\Scripts\activate``

5. while in the project directory, Install the requirements with the following command: ``pip3 install -r requirements.txt``

6. rename ``.env_example`` file in the project root directory to ``.env`` and insert correct values for SECRET_KEY and EMAIL Credentials in the ``.env`` file.

7. Then create a superuser for django: on linux run: ``python manage.py createsuperuser``. On windows ? run: ``py manage.py createsuperuser`` then follow the on-screen prompts.

8. Finally run: on linux: ``python manage.py runserver``. On windows: ``py manage.py runserver`` boom! you have the project up and running.

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

.. |repo-size| image:: https://img.shields.io/github/repo-size/developerayyo/eportal?style=flat
    :alt: repo size
    
.. |licence| image:: https://img.shields.io/github/license/developerayyo/eportal?style=flat
    :alt: licence
    :target: https://eportalproject.readthedocs.io/en/latest/getting%20started.html#licences

.. |website| image:: https://img.shields.io/website?up_message=eportalproject.ml&url=https%3A%2F%2Feportalproject.ml
    :alt: Website
    :target: https://eportalproject.ml

.. |docs| image:: https://img.shields.io/readthedocs/eportalproject
    :alt: Read the Docs
    :target: https://docs.eportalproject.ml 

.. |codecov| image:: https://codecov.io/gh/developerayyo/eportal/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/developerayyo/eportal

.. |build| image:: https://travis-ci.com/developerayyo/eportal.svg?branch=master
    :target: https://travis-ci.com/developerayyo/eportal


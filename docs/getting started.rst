===============
Getting Started
===============

Installation
============

1. fork this `Repo <https://github.com/developerayyo/eportal/>`_  to your github account

2. Clone the forked version on your system  by running the following command from the command line ``git clone https://github.com/<your-username>/eportal``

3. Go into the repo dir : ``cd eportal``

4. Create and activate your python virtual environment on linux ``python3 -m virtualenv myenv && source myenv/bin/activate``. If you are on windows ``virtualenv myenv && myenv\Scripts\activate``

5. while in the project directory, Install the requirements with the following command: ``pip3 install -r requirements.txt``

6. rename ``.env_example`` file in the project root directory to ``.env`` and insert correct values for SECRET_KEY and EMAIL Credentials in the ``.env`` file.

7. Then create a superuser for django: on linux run: ``python manage.py createsuperuser``. On windows ? run: ``py manage.py createsuperuser`` then follow the on-screen prompts.

8. Finally run: on linux: ``python manage.py runserver``. On windows: ``py manage.py runserver`` boom! you have the project up and running.

Licences
========

MIT License

Copyright (c) 2020 Babalola Peter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Contact
=======
Question? Please contact peterbabalola@eportalproject.ml

Need Help?
==========

If you have any trouble with the Project please email help@eportalproject.ml

Need Further Help?
^^^^^^^^^^^^^^^^^^

Please join our Slack Channel on https://eportalproject.slack.com
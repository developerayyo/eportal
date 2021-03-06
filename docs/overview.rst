==================================
Brief Overview of How ACRRPS Works
==================================

Intro
=====

Like I said before, this project is still in development, But quite people of 
testers requested that I should write a short overview on how the project works to give them
an insight on how to aproach the project.

Users
=====

So currently there are three categories of users on ACRRPS:

* Administrator
* Lecturer
* Student

Well lets start with how the each users get access to the site:

Administrator
^^^^^^^^^^^^^

The Administrator was created by the developer.

Lecturers
^^^^^^^^^

The Administrator is responsible for uploading the lecturers to the site.
`How?`: The Administrator creates a ``csv file`` that contains the profile details of lecturers,
and then upload it to the site. After the upload is successful, the lecturer receives a mail containing 
an autogenerated username and password which they can use to access the site.
As you might have guessed, the Administrator is not supposed to be the one to generate the csv file that contains the 
lecturer datails, of course you're right, but the idea here is that the school will provide the details that will be used by the administrator.

Student
^^^^^^^

Students gets access to the site similarly to the way lecturersgot their access. the only difference is that the
Students can choose to either log-in with their username or Natric_number.

Roles of Users
==============

Now, lets talk about specific roles of each users on ACRRPS

Students
^^^^^^^^

* Finished:
    * Course registration.
    * Viewe registered courses and print course registration form.
    * View and print result.
    * Change password.
* ToDo:
    * Wizard to introduce students to all the components of their view.
    * Documentation on how student view works.

Lecturers
^^^^^^^^^

* Finished:
    * View List of allocated Courses in the `Profile Section`
    * Upload Scoresheet for each course allocated to them.
    * Download the scoresheet template for each courses allocated to them.
    * Change their password.
* ToDo:
    * Wizard to introduce lecturers to all the components of their view.
    * Documentation on how lecturer view works.

Administrator
^^^^^^^^^^^^^

* Finished:
    * View Demographic Dashboard that shows the overall performance of students in the school and also
        contains shortcuts to specific parts of the page.
    * Upload students and lecturers to the site from a `csv file`, View and edit users of the site(Students, and Lecturers).
    * Upload Courses to the site from a `csv file`.
    * Upload course allocation list to the site from a `csv file` or allocate courses directly on the site. 
    * Change password.
    * Change current Session/Semester for the whole school.
    * Add a toggle button to Administrator view that allows him to reveal or hide Result.
    * Upload old students results for each course.
    * Download Result mastersheet for a selected Department and level for the current semester.
    * Export data from the site to various formats e.g pdf, csv, etc.
    * filter data
* ToDo:
    * Upload old students results from a mastersheet for a particular deparment, level and semester.
    * Promote all students with a single button.
    * Wizard to introduce administrators to all the components of their view.
    * Documentation on how administrator view works.

Proposed Enhancements
=====================
    I learnt recently, that the DEAN of Faculties, Head Of Departments, And The Exams & Records also has an important role to play on ACRRPS. I planned to learn and research more on ACRRPS for better Understanding and Implementation of this Project.

Contribution
============
    If you would like to contrbute in anyway, either by sharing your ideas , resourses, research notes, similar projects on this Topic with me, or you want to explore or test the site for, send me mail developer@eportalproject.ml or DM me  `Live-chat <https://tawk.to/2eb8621a65f5ea02010345519f534eec9ced3231>`_ .
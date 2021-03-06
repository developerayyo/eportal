from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/', views.profile, name='profile'),
    path('profile/view/<int:id>/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.profile_update, name='edit_profile'),
    path('password/', views.change_password, name='change_password'),
        path('staff/', views.staff_list, name="staff_list"),
    path('staff/add/new/', views.StaffAddView, name="add_new_staff"),
    path('staff/edit/<int:pk>/', views.edit_staff, name="edit_staff"),
    path('staff/delete/<int:pk>/', views.delete_staff, name="delete_staff"),
    path('courses/', views.course_list, name="course_list"),
    path('courses/add/new',
         views.CourseAddView,
         name="add_new_course"),
    path('course/delete/<int:pk>/', views.delete_course, name="delete_course"),
    path('course/edit/<int:pk>/', views.course_edit, name="course_edit"),
    path('students/', views.student_list, name="student_list"),
    path('student/add/new/', views.StudentAddView, name="add_new_student"),
    path('student/delete/<int:pk>/',
         views.delete_student,
         name="delete_student"),
    path('student/edit/<int:pk>/', views.edit_student, name="edit_student"),
    path('session/', views.session_list_view, name="manage_session"),
    path('session/add/new', views.session_add_view, name="create_new_session"),
    path('session/edit/<int:pk>/',
         views.session_update_view,
         name="edit_session"),
    path('session/delete/<int:pk>/',
         views.session_delete_view,
         name="delete_session"),
    path('semester/', views.semester_list_view, name="manage_semester"),
    path('semester/add/new',
         views.semester_add_view,
         name="create_new_semester"),
    path('semester/edit/<int:pk>/',
         views.semester_update_view,
         name="edit_semester"),
    path('semester/delete/<int:pk>/',
         views.semester_delete_view,
         name="delete_semester"),
    path('course/assign/',
         views.CourseAllocationView.as_view(),
         name='course_allocation'),
    path('course/allocated/',
         views.course_allocation_view,
         name='course_allocation_view'),
    path('course/allocated/me/',
         views.allocated_courses,
         name='allocated_courses'),
    path('course/allocation/upload/',
          views.course_allocation_upload,
          name='course_allocation_upload'),
    path('course/deallocate/<int:pk>/',
         views.withheld_course,
         name='withheld_course'),
    path('students/carry-over-list/', views.carry_over, name='carry_over'),
    path('students/repeat-list/', views.repeat_list, name='repeat_list'),
    path('students/1st_class_list/',
         views.first_class_list,
         name='first_class_list'),
    path('api/data/', views.get_chart, name='chart'),
    path('result/', views.view_result, name="view_results"),
    path('course/registration/',
         views.course_registration,
         name='course_registration'),
    path('course/registered/',
         views.registered_courses,
         name='registered_courses'),
    path('course/drop/', views.course_drop, name='course_drop'),
    path('coursepdf/',
         views.course_registration_pdf,
         name='course_registration_pdf'),
    path('resultpdf/',
          views.result_pdf,
          name='result_pdf'),
    path('score/', views.add_score, name='add_score'),
    path('score/<int:id>/', views.add_score_for, name='add_score_for'),
    path('scoresheet/download/<int:id>/', views.scoresheet_download, name='scoresheet_download'),
    path('toggles/', views.toggles),
    path('mastersheet/', views.mastersheet, name='mastersheet')
]

from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'portal'

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)
router.register('students', views.StudentViewSet)
router.register('lecturers', views.LecturerViewSet)
router.register('courseallocation', views.CourseAllocationViewSet)
router.register('sessions', views.SessionViewSet)
router.register('semesters', views.SemesterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'portal'

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

urlpatterns = [
    # path('courses/', views.CourseListView.as_view(), name='course_list'),
    # path('courses/<pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    # path('courses/<pk>/enroll/', views.CourseRegistrationView.as_view(), name='course_enroll'),
    path('', include(router.urls)),
]

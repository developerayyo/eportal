from .serializers import (
    UserSerializer, CourseSerializer, StudentSerializer, SemesterSerializer,
    CourseAllocationSerializer, SessionSerializer, 
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from ..models import (
    Course, TakenCourse, Student, User, CourseAllocation, Session, Semester
)

from rest_framework import viewsets
from rest_framework.decorators import action

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..decorators import admin_required


# @method_decorator([login_required, admin_required], name='dispatch')
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# @method_decorator([login_required, admin_required], name='dispatch')
class LecturerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_lecturer=True)
    serializer_class = UserSerializer

# @method_decorator([login_required, admin_required], name='dispatch')
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# @method_decorator([login_required, admin_required], name='dispatch')
class CourseAllocationViewSet(viewsets.ModelViewSet):
    queryset = CourseAllocation.objects.all()
    serializer_class = CourseAllocationSerializer

# @method_decorator([login_required, admin_required], name='dispatch')
class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all().order_by('-session')
    serializer_class = SessionSerializer

# @method_decorator([login_required, admin_required], name='dispatch')
class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all().order_by('-session')
    serializer_class = SemesterSerializer
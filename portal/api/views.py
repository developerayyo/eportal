from rest_framework import generics
from ..models import Course
from .serializers import CourseSerializer

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from ..decorators import student_required
from ..models import TakenCourse, Student

from rest_framework import viewsets
from rest_framework.decorators import action

# from .serializers import

# Intro
# class CourseListView(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

# class CourseDetailView(generics.RetrieveAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
    
# Custom Api View
# class CourseRegistrationView(APIView):
#     authentication_classes = (BasicAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, pk=pk)
#         try:
#             student = Student.objects.get(user__pk=request.user.id)
#         except:
#             return Response({'Error': 'Make sure your details are correct and make sure you are a student'})
#         taken_course = TakenCourse.objects.create(student=student, course=course)
#         taken_course.save()
#         return Response({'enrolled': True})

# Using viewsets which is an improvement over # Intro
# class CourseViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

# Lets change CourseRegistrtionView to Custom ViewSets by modifying  CourseViewSet7
class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    @action(
        detail=True,
        methods=['post'],
        authentication_classes=[BasicAuthentication],
        permission_classes=[IsAuthenticated]
    )
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        try:
            student = Student.objects.get(user__pk=request.user.id)
        except:
            return Response({'Error': 'Make sure your details are correct and make sure you are a student'})
        taken_course = TakenCourse.objects.create(student=student, course=course)
        return Response({'enrolled': True})
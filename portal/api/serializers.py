from rest_framework import serializers
from ..models import Course, Result

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        # fields = ['id', 'courseCode', 'courseTitle']
        fields = '__all__'

# class ResultSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Result
#         fields = []
from rest_framework import serializers
from ..models import Course, Student, User, CourseAllocation, Session, Semester

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id', 'courseCode', 'courseTitle', 'courseUnit', 'semester', 'level',
            )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'username', 'phone', 'address', 
        )

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Student
        fields = (
            'id', 'id_number', 'user', 'level', 'faculty', 'department',
        )

class CourseAllocationSerializer(serializers.ModelSerializer):
    lecturer = UserSerializer(required=True)
    courses = CourseSerializer(required=True, many=True)
    class Meta:
        model = CourseAllocation
        fields = (
            'id', 'lecturer', 'courses',
        )


class SessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = '__all__'

class SemesterSerializer(serializers.ModelSerializer):
    session = SessionSerializer(required=True)
    class Meta:
        model = Semester
        fields = '__all__'
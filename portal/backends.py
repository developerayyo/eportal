from django.contrib.auth.backends import ModelBackend

from .models import Student

class StudentBackend(ModelBackend):
    """
    Custom authentication backend for students that inherits from  django 
    BodelBackend. This allow student to sign-in with their matric no order than 
    their username.
    """
    def authenticate(self, request, **kwargs):
        id_number = kwargs['username']
        password = kwargs['password']
        try:
            student = Student.objects.get(id_number=id_number)
            if student.user.check_password(password) is True:
                return student.user
        except Student.DoesNotExist:
            pass

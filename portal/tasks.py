from celery import task
from django.core.mail import send_mail

from .models import Student
from .models import User


@task
def student_reg(id_number, pwd):
    """
    Task to send login details to student's e-mail upon student bulk upload.

    Quick tip: it is most likely that the administrator can upload thousands of 
    students all at once, mailing each students their login details(which 
    probably was generated in the process) is a very expensive task and its 
    possible that not all the students might have their login details delivered 
    to their email, So here's where Celery comes in. In simple terms, Celery 
    monitors the process and treat each email to be sent a job and adds it to 
    the job queue, thereby ensures that all job are done one after ther other.
    Isn't this a much nice approach to handle such expensive tasks huh??
    """
    student = Student.objects.get(id_number=id_number)
    subject = f'Matric Number: {id_number}'
    message = f'Dear {student.user.get_full_name},\n\n' \
              f'You have been successfully registered to University Eportal.' \
              f'Your Matric Number is: {id_number} ' \
              f'and your Password is: {pwd}'
    mail_sent = send_mail(
        subject, message, 'registration@eportalproject.ml', [student.user.email])

    return mail_sent

@task
def staff_reg(username, pwd):
    """
    Task to send login details to staff's e-mail upon staff bulk upload.
    """
    staff = User.objects.get(username=username)
    subject = f'Username: {username}'
    message = f'Dear {staff.get_full_name},\n\n' \
              f'You have been successfully registered to University Eportal.' \
              f'Your ssername is: {username} ' \
              f'and your password is: {pwd}'
    mail_sent = send_mail(
        subject, message, 'registration@eportalproject.ml', [staff.email])

    return mail_sent

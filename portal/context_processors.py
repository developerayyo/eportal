import datetime

from .models import Session, Semester, FIRST, ResultRender

y = datetime.datetime.today()
session = str(y.year) + " / " + str(y.year + 1)

try:
    s = Session.objects.get(is_current_session=True)
except Session.DoesNotExist:
    s = Session.objects.create(session=session, is_current_session=True)
    s.save()

try:
    sem = Semester.objects.get(is_current_semester=True)
except Semester.DoesNotExist:
    sem = Semester.objects.create(semester=FIRST, is_current_semester=True)
    sem.save()


def session_processor(request):
    current_session = Session.objects.get(is_current_session=True)
    return {"current_session": current_session}


def semester_processor(request):
    current_semester = Semester.objects.get(is_current_semester=True)
    return {"current_semester": current_semester}

def result_render_processor(request):
    w, created = ResultRender.objects.get_or_create(id=1)
    return {"result_render": w}
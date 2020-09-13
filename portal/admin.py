from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import (
    User, Student, CarryOverStudent, RepeatingStudent, Course,
    TakenCourse, Result, Semester, CourseAllocation, Session, ResultRender
)


@admin.register(CourseAllocation)
class AllocationAdmin(ImportExportModelAdmin):
    list_display = ['lecturer', ]


@admin.register(Result)
class ResultAdmin(ImportExportModelAdmin):
    list_display = ['student', 'gpa', 'semester', 'level', 'cgpa']


@admin.register(TakenCourse)
class TakenCourseAdmin(ImportExportModelAdmin):
    list_display = ['student', 'course', 'ca',
                    'exam', 'total', 'grade', 'comment']

admin.site.register(User)
admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(Student)
admin.site.register(CarryOverStudent)
admin.site.register(RepeatingStudent)
admin.site.register(Course)
admin.site.register(ResultRender)

from django.contrib import admin

from core.models import Person, Course, Grade


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")

    class Meta:
        ordering = ("last_name", "first_name")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass
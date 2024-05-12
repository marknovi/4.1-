from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Student, SchoolClasses
from django.shortcuts import render
from django.urls import path

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender', 'age', 'name', 'surname', 'grade')

class SchoolClassesAdmin(admin.ModelAdmin):
    list_display = ('id', 'schoolClass', 'view_students_link')
    list_display_links = ('schoolClass',)  # Поле 'schoolClass' будет ссылкой

    def view_students_link(self, obj):
        url = reverse('admin:schoolclasses_students', args=[obj.id])
        return format_html('<a href="{}">View students</a>', url)

    view_students_link.allow_tags = True
    view_students_link.short_description = "Students"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:school_class_id>/students/', self.admin_site.admin_view(self.school_class_students_view), name="schoolclasses_students")
        ]
        return custom_urls + urls

    def school_class_students_view(self, request, school_class_id):
        school_class = SchoolClasses.objects.get(pk=school_class_id)
        students = Student.objects.filter(grade=school_class)
        return render(request, 'school_class_students.html', {'school_class': school_class, 'students': students})

admin.site.register(Student, StudentAdmin)
admin.site.register(SchoolClasses, SchoolClassesAdmin)

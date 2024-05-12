from django.shortcuts import render
from .models import SchoolClasses, Student

def home(request):
    # Получаем список всех классов
    all_classes = SchoolClasses.objects.all()
    # Подсчитываем общее количество учеников
    total_students = Student.objects.count()
    return render(request, 'home.html', {'classes': all_classes, 'total_students': total_students})

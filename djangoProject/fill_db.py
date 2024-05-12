# seed_data.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

from djangoProject.models import Student, SchoolClasses

def create_or_get_class(class_name):
    class_instance, created = SchoolClasses.objects.get_or_create(schoolClass=class_name)
    return class_instance

def create_or_get_student(name, surname, age, gender, class_name):
    class_instance = create_or_get_class(class_name)
    student_instance, created = Student.objects.get_or_create(
        name=name, surname=surname, age=age, gender=gender, grade=class_instance
    )
    return student_instance

def seed_data():
    classes = [
        "1A", "1Б", "1В",
        "2A", "2Б", "2В",
        "3A", "3Б", "3В",
        "4A", "4Б", "4В",
        "5A", "5Б", "5В",
        "6A", "6Б", "6В",
        "7A", "7Б", "7В",
        "8A", "8Б", "8В",
        "9A", "9Б", "9В",
        "10A", "10Б", "10В",
        "11A", "11Б", "11В",
    ]

    for class_name in classes:
        create_or_get_class(class_name)

    create_or_get_student(name="John", surname="Doe", age=7, gender="M", class_name="1A")
    create_or_get_student(name="Jane", surname="Smith", age=8, gender="W", class_name="2Б")
    create_or_get_student(name="Никита", surname="Ковалев", age=16, gender="М", class_name="9A")
    create_or_get_student(name="Мария", surname="Мачулина", age=14, gender="W", class_name="8В")

if __name__ == "__main__":
    seed_data()

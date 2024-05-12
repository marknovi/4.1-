# seed_data.py
import os
import django
import random
from faker import Faker

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

def generate_random_students(num_students, order_by=None):
    fake = Faker()
    students = []
    for _ in range(num_students):
        name = fake.first_name()
        surname = fake.last_name()
        age = random.randint(7, 18)
        grade = (age - 7) + 1
        class_name = f"{grade}A"
        gender = random.choice(["М", "Д"])
        student = create_or_get_student(name, surname, age, gender, class_name)
        students.append(student)

    if order_by:
        students = students.order_by(order_by)

    return students

if __name__ == "__main__":
    students = generate_random_students(1000, order_by='surname')
    for student in students:
        print(student.surname, student.name)

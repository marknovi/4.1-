from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse


def validate_age(value):
    if value is None or value < 5 or value > 100:
        raise ValidationError("Age must be a positive number between 5 and 100.")


class SchoolClasses(models.Model):
    schoolClass = models.CharField(max_length=2)

    class Meta:
        verbose_name: str = 'Class'
        verbose_name_plural = 'Classes'
        ordering = ['id']

    def __str__(self):
        return self.schoolClass


class Student(models.Model):
    GENDER_CHOICES = (
        ('М', 'Мальчик'),
        ('Д', 'Девочка'),
    )
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField(validators=[validate_age])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    grade = models.ForeignKey(SchoolClasses, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('student-id', kwargs={'pk': self.pk})

    class Meta:
        verbose_name: str = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['age', 'gender', 'name']

    def __str__(self):
        return f"{self.name} {self.surname}"



from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    hobby = models.TextField()
    actions = models.TextField()

    def __str__(self):
        return self.name
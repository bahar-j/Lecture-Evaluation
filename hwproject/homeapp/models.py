from django.db import models
from django.contrib.auth.models import User

class Lecture(models.Model):
    professor = models.CharField(max_length=50)
    rq_year = models.IntegerField()
    rq_semester = models.IntegerField()
    department = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    instruction_number = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    credit = models.IntegerField()
    time = models.IntegerField()

    def __str__(self):
        return self.title
class Post(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    body = models.TextField()
    rating = models.IntegerField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
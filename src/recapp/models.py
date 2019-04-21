from django.db import models
from django.urls import reverse
# Create your models here.


class Candidate(models.Model):
    first_name  = models.CharField(max_length=120)
    last_name   = models.CharField(max_length=120)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    # def get_absolute_url(self):
    #     return reverse("articles:article-detail", kwargs={"id": self.id})


class Recruter(models.Model):
    first_name  = models.CharField(max_length=120)
    last_name   = models.CharField(max_length=120)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Task(models.Model):
    title = models.CharField(max_length=120,default='New Task', unique=True)


    def __str__(self):
        return self.title

class Grade(models.Model):
    value     = models.PositiveSmallIntegerField(default=0)
    task      = models.ForeignKey(Task, on_delete=models.PROTECT)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruter, on_delete=models.PROTECT)

    # def __str__(self):
    #     return self.task

    def get_absolute_url(self):
        return reverse("recapp:recap_add-mark", kwargs={"id": self.id})





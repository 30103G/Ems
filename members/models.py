from django.db import models

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=20)
    unm = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    spec = models.CharField(max_length=20)

class Student(models.Model):
    name = models.CharField(max_length=20)
    unm = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    prog = models.CharField(max_length=20)

class Exam(models.Model):
    exam = models.CharField(max_length=10)
    create = models.DateField(auto_now_add=True)
    startdate = models.DateField()
    enddate = models.DateField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

class Question(models.Model):
    que = models.TextField(max_length=200)
    marks = models.IntegerField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

class Assesment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    # que = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField()
    is_attempt = models.BooleanField(default=False)

class AssementAnswer(models.Model):
    exam= models.ForeignKey(Exam,on_delete=models.DO_NOTHING)
    answer=models.TextField(max_length=500)
    scored=models.IntegerField()
    def __str__(self):
        return f'{self.exam}'
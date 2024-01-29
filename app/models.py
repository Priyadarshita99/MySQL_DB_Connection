from django.db import models

# Create your models here.
class Student(models.Model):
    Sid=models.BigIntegerField(primary_key=True)
    Sname=models.CharField(max_length=50)
    Scourse=models.CharField(max_length=50)

    def __str__(self):
        return self.Sname
    
class Grade(models.Model):
    Sid=models.ForeignKey(Student,on_delete=models.CASCADE)
    Smockrating=models.CharField(max_length=1)

    def __str__(self):
        return self.Smockrating
    

    
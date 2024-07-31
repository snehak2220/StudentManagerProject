from django.db import models

# Create your models here.
class Students(models.Model):
    Student_Id=models.IntegerField(primary_key=True)
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Course=models.CharField(max_length=100)
    Address=models.CharField(max_length=500)
    Location=models.CharField(max_length=200)
    Phone=models.IntegerField()

    def __str__(self):
        return self.First_Name

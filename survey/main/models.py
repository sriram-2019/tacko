from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=264)
    email=models.CharField(max_length=264)
    batch=models.CharField(max_length=264)
class student1(models.Model):
    name = models.CharField(max_length=264)
    email = models.CharField(max_length=264)
    batch= models.CharField(max_length=264)
    vision= models.CharField(max_length=264)
    mission= models.CharField(max_length=264)
    peo= models.CharField(max_length=264)
    pos= models.CharField(max_length=264)
class staff(models.Model):
    staff_name=models.CharField(max_length=264)
class staff1(models.Model):
    staff_name=models.TextField()
    staff_email=models.TextField()
class staff2(models.Model):
    staff_name=models.TextField()
    staff_email=models.TextField()
    vision= models.TextField()
    mission= models.TextField()
    peo= models.TextField()
    pos= models.TextField()
class parent(models.Model):
    sd=models.TextField()
    batch=models.TextField()
    occupation=models.TextField()
    vision= models.TextField()
    mission= models.TextField()
    peo= models.TextField()
    pos= models.TextField()
class parent1(models.Model):
    parent_name=models.TextField()
    sd=models.TextField()
    batch=models.TextField()
    occupation=models.TextField()
    vision= models.TextField()
    mission= models.TextField()
    peo= models.TextField()
    pos= models.TextField()
class emails(models.Model):
    email1=models.EmailField()
    email2=models.EmailField()
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import User, Group
from tinymce.models import HTMLField
# from Instructors.models import *

class Instructor(models.Model):
    User = models.OneToOneField(User)
    Followers = models.ManyToManyField('Athlete', default="")
    Name = models.CharField(default="", max_length=100)
    Bio = HTMLField()

class Athlete(models.Model):
    User = models.OneToOneField(User)
    Following = models.ManyToManyField(Instructor, default="")
    Courses = models.ManyToManyField('Course')
    Products = models.ManyToManyField('Product', default="")
    Name = models.CharField(default="", max_length=100)

class Product(models.Model):
    Owner = models.ForeignKey(Instructor, default="", related_name="Products", null=True)
    Buyers = models.ManyToManyField('Athlete', default="", null=True)
    Type = models.CharField(default="", max_length=20)
    Title = models.CharField(default="", max_length=100)
    Description = models.CharField(default="", max_length=1000)
    # Price = models.IntegerField(default=0)
    Price = models.DecimalField(max_digits=10, decimal_places=1, default=0)    
    File = models.FileField(upload_to='Products', max_length=100, default="")
    Thumbnail = models.FileField(upload_to='Products/Thumbnails', max_length=100, default="")
    Has_Thumbnail = models.BooleanField(default=False)

class Transaction(models.Model):
    Seller = models.OneToOneField(Instructor, default="")
    Buyer = models.OneToOneField(Athlete, default="")

class E_Book(models.Model):
    Owner = models.ForeignKey(Instructor, default="", related_name="E_Books")
    Buyers = models.ManyToManyField(Athlete, default="")

class Video_Product(models.Model):
    Owner = models.ForeignKey(Instructor, default="", related_name="Video_Products")
    Buyers = models.ManyToManyField(Athlete, default="")

class Course(models.Model):
    Owner = models.ForeignKey(Instructor, default="", related_name="Courses")
    Title = models.CharField(default="", max_length=100)
    Price = models.DecimalField(max_digits=10, decimal_places=1, default=0)    
    Description = models.CharField(default="", max_length=1000)
    Topic = models.CharField(default="", max_length=20)
    Buyers = models.ManyToManyField(Athlete, default="")
    Confirmed = models.BooleanField(default=False)

class Course_Item(models.Model):
    Title = models.CharField(default="", max_length=100)
    Course = models.ForeignKey(Course, related_name="Items")
    Type = models.CharField(default="", max_length=20)
    Ordered_ID = models.IntegerField(default=0)
    Description = models.CharField(default="", max_length=1000)
    File = models.FileField(upload_to='Course_Items', max_length=100, default="")

class Course_Files(models.Model):
    Course = models.OneToOneField(Course, default="")

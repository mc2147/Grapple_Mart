# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import User, Group
# from tinymce.models import HTMLField

class Instructor(models.Model):
	User = models.OneToOneField(User)
	Followers = models.ManyToManyField('Athlete', default="")
	Name = models.CharField(default="", max_length=100)
	# Bio = HTMLField(blank = True)
	# Awards = HTMLField(blank = True)
	# need to add profile pic

class Athlete(models.Model):
	User = models.OneToOneField(User)
	Following = models.ManyToManyField(Instructor, default="")
	Courses = models.ManyToManyField('Course')
	Products = models.ManyToManyField('Product', default="")
	Name = models.CharField(default="", max_length=100)

class Product(models.Model):
	Owner = models.OneToOneField(Instructor, default="", null=True)
	Buyers = models.ManyToManyField(Athlete, default="", null=True)
	Type = models.CharField(default="", max_length=20)
	Title = models.CharField(default="", max_length=100)
	Description = models.CharField(default="", max_length=1000)
	# Price = models.IntegerField(default=0)
	Price = models.DecimalField(max_digits=10, decimal_places=1, default=0)	
	File = models.FileField(upload_to='Products', max_length=100, default="")
	Thumbnail = models.FileField(upload_to='Products/Thumbnails', max_length=100, default="")
	Has_Thumbnail = models.BooleanField(default=False)

class E_Book(models.Model):
	Owner = models.OneToOneField(Instructor, default="")
	Buyers = models.ManyToManyField(Athlete, default="")

class Video_Product(models.Model):
	Owner = models.OneToOneField(Instructor, default="")
	Buyers = models.ManyToManyField(Athlete, default="")

class Course(models.Model):
	Owner = models.OneToOneField(Instructor, default="")
	Buyers = models.ManyToManyField(Athlete, default="")

class Course_Files(models.Model):
	Course = models.OneToOneField(Course, default="")

class Transaction(models.Model):
	Seller = models.OneToOneField(Instructor, default="")
	Buyer = models.OneToOneField(Athlete, default="")

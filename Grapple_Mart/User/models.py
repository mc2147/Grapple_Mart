# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import User, Group
from tinymce.models import HTMLField

##############################

class Instructor(models.Model):
	# this should be derived from AbstractUser
	User = models.OneToOneField(User)
	Followers = models.ManyToManyField('Athlete', default="")
	Name = models.CharField(default="", max_length=100)
	Bio = HTMLField()

class Athlete(models.Model):
	# this should be derived from AbstractUser
	User = models.OneToOneField(User)
	Following = models.ManyToManyField(Instructor, default="")
	# courses should be moved over to "courses" app
	Courses = models.ManyToManyField('Course')
	# products should be moved over to "products" app
	Products = models.ManyToManyField('Product', default="")
	Name = models.CharField(default="", max_length=100)

# in general we should have one common User model derived from AbstractUser
# since each Instructor is an Athlete and can purchase from other Instructors
# and vise versa( there is no need to to separate functionality this way )

#############################

class Product(models.Model):
	# this should be derived from SingleOwnerMixin as well
	Owner = models.OneToOneField(Instructor, default="", null=True)
	# buyers should be moved over to separate "orders" app
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
	# this is just a kind of product and shouldn't have a separate model
	Owner = models.OneToOneField(Instructor, default="")
	Buyers = models.ManyToManyField(Athlete, default="")

class Video_Product(models.Model):
	# this is just a kind of product and shouldn't have a separate model
	Owner = models.OneToOneField(Instructor, default="")
	Buyers = models.ManyToManyField(Athlete, default="")

class Course(models.Model):
	# this could probably be treated as a product for the first version
	Owner = models.OneToOneField(Instructor, default="")
	Buyers = models.ManyToManyField(Athlete, default="")

class Course_Files(models.Model):
	# each Product can have files attached
	Course = models.OneToOneField(Course, default="")

class Transaction(models.Model):
	# this will be an Order model in "orders" app
	Seller = models.OneToOneField(Instructor, default="")
	Buyer = models.OneToOneField(Athlete, default="")

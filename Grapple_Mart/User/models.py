# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import User, Group

class Instructor(models.Model):
	User = models.OneToOneField(User)
	Followers = models.ManyToManyField('Athlete', default="")
	Name = models.CharField(default="", max_length=100)

class Athlete(models.Model):
	User = models.OneToOneField(User)
	Following = models.ManyToManyField(Instructor, default="")
	Courses = models.ManyToManyField('Course')
	Products = models.ManyToManyField('Product', default="")
	Name = models.CharField(default="", max_length=100)

class Product(models.Model):
	Owner = models.OneToOneField(Instructor, default="")
	Buyers = models.ManyToManyField(Athlete, default="")
	Type = models.CharField(default="", max_length=20)

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

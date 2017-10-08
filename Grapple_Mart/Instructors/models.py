# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import User, Group
from tinymce.models import HTMLField
# from User.models import *
from django.db import models

# Test = {}

# # Create your models here.
# class Instructor(models.Model):
# 	User = models.OneToOneField(User)
# 	# Followers = models.ManyToManyField('Athlete', default="")
# 	Name = models.CharField(default="", max_length=100)
# 	Bio = HTMLField()

# class E_Book(models.Model):
# 	Owner = models.OneToOneField(Instructor, default="")
# 	# Buyers = models.ManyToManyField(Athlete, default="")

# class Video_Product(models.Model):
# 	Owner = models.OneToOneField(Instructor, default="")
# 	# Buyers = models.ManyToManyField(Athlete, default="")

# class Course(models.Model):
# 	Owner = models.OneToOneField(Instructor, default="")
# 	Title = models.CharField(default="", max_length=100)
# 	Description = models.CharField(default="", max_length=1000)
# 	Topic = models.CharField(default="", max_length=20)
# 	Owner = models.OneToOneField(Instructor, default="")
# 	# Buyers = models.ManyToManyField(Athlete, default="")
# 	Confirmed = models.BooleanField(default=False)

# class Course_Item(models.Model):
# 	# Course = models.ForeignKey(Course, related_name="Items")
# 	Type = models.CharField(default="", max_length=20)
# 	Ordered_ID = models.IntegerField(default=0)

# class Course_Files(models.Model):
# 	Course = models.OneToOneField(Course, default="")

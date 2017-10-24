from django import forms
from tinymce.models import HTMLField


class Instructor_Bio_Form(forms.Form):
    Bio = HTMLField()

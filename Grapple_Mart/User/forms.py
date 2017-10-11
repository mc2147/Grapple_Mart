from django import forms

from .models import Instructor

class InstructorEditForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = ('Bio', 'Awards','Highlights')
        # reference: https://stackoverflow.com/questions/19489699/how-to-add-class-id-placeholder-attributes-to-a-field-in-django-model-forms
        widgets = {
        	'Bio': forms.TextInput(attrs = {'class':'richTextEditor'}),
            'Awards': forms.TextInput(attrs = {'class':'richTextEditor'}),
            'Highlights': forms.TextInput(attrs = {'class':'richTextEditor'})
        }  
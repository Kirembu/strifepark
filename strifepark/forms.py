from strifepark.models import Entry
from django.forms import fields_for_model
from django import forms
import datetime
##mEntryForm = fields_for_model(Entry)

##class EntryForm(forms.ModelForm):
##    class Meta:
##        model = Entry
        
class EntryForm(forms.Form):
    title = forms.CharField(required=True)
    markdown = forms.CharField(required=True,label='Title',
                               widget=forms.Textarea())
    pub_date = forms.DateTimeField(required=True,)

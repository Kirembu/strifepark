from django import forms

class UpdateForm(forms.Form):
    status = forms.CharField(widget=forms.Textarea(attrs={"style":"width:95%; max-width: 400px;",
                                                          "rows":"3"}),required=True)

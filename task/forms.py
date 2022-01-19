from django import modelform
from django import course



class courseForm(ModelForm):
    class Meta:
        model = course
        fields='__all__'
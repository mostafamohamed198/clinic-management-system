from django import forms
from .models import *

class Druginfo(forms.ModelForm):
    class Meta:
        model = medications
        fields = ['name', 'concentration', 'dosage']

# class Glasses(forms.ModelForm):
#     class Meta:
#         model = client
#         fields = ['leftleft', 'leftmiddle','leftright', 'rightleft', 'rightmiddle', 'rightright' ]

# class Medicalhistory(forms.ModelForm):
#     class Meta:
#         model= client
#         fields = ['diabetesmellitus', 'deabetesnumber', 'hypertension', 'ihd', 'cvs', 'asthma', 'atopy', 'liver', 'kidney']

# class Ophthalmichistory(forms.ModelForm):
#     class Meta:
#         model = client
#         fields = ['cataract', 'glucoma', 'glucomasurgery', 'refractive', 'medication']

# class Complain(forms.ModelForm):
#     class Meta:
#         model = client
#         fields = ['bov', 'diplopia', 'headache', 'burning', 'foreign', 'epiphoria', 'glare', 'note']
                                                        
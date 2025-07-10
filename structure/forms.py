from .models import Governorate,CentralUnit
from django import forms
from accounts.models import User

class GovernorateForm(forms.ModelForm):
    class Meta:
        model = Governorate
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        allowed_head_roles = ['governorate_head']
        allowed_vice_roles = ['governorate_vice']
        self.fields['head'].queryset = User.objects.filter(role__in=allowed_head_roles)
        self.fields['vice'].queryset = User.objects.filter(role__in=allowed_vice_roles)
        
        
class CentralUnitrateForm(forms.ModelForm):
    class Meta:
        model = CentralUnit
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        allowed_head_roles = ['central_unit_head']
        allowed_vice_roles = ['central_unit_vice']
        self.fields['head'].queryset = User.objects.filter(role__in=allowed_head_roles)
        self.fields['vice'].queryset = User.objects.filter(role__in=allowed_vice_roles)
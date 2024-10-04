from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from webapp.models import *


class UsuarioLoginForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']


class UsuarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('first_name',)


class BautizoForm(forms.ModelForm):
    class Meta:
        model = Bautizo
        fields = '__all__'
        widgets = {
            'libro': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 40px;'}),
            'fojas': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 40px;'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 40px;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].widget = forms.DateInput(format='%Y-%m-%d', attrs={
            'type': 'date',
            'class': 'form-control'
        })
        self.fields['fecha_bautizo'].widget = forms.DateInput(format='%Y-%m-%d', attrs={
            'type': 'date',
            'class': 'form-control'
        })


class MatrimonioForm(forms.ModelForm):
    class Meta:
        model = Matrimonio
        fields = '__all__'
        widgets = {
            'libro': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 40px;'}),
            'fojas': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 40px;'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 40px;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_matrimonio'].widget = forms.DateInput(format='%Y-%m-%d', attrs={
            'type': 'date',
            'class': 'form-control'
        })


class ConfirmacionForm(forms.ModelForm):
    class Meta:
        model = Confirmacion
        fields = [
            'nombre',
            'ex_monsenor',
            'parroquia',
            'fecha',
            'padres',
            'padrinos'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].widget = forms.DateInput(format='%Y-%m-%d', attrs={
            'type': 'date',
            'class': 'form-control'
        })


class ComunionForm(forms.ModelForm):
    class Meta:
        model = priComunion
        fields = [
            'nombre',
            'parroquia',
            'fecha',
            'padre',
            'madre',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].widget = forms.DateInput(format='%Y-%m-%d', attrs={
            'type': 'date',
            'class': 'form-control'
        })

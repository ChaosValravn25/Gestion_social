from django import forms
from .models import Division

class Crear_Area(forms.Form):
	titulo = forms.CharField(label="Titulo de area", max_length=200)
	descripcion = forms.CharField(widget=forms.Textarea)
	division = forms.ModelChoiceField(
        queryset=Division.objects.all(),  
        label="Division",
        empty_label="Seleccione una division"
    )
	archivo = forms.FileField(
        label="Documentos",
        required=False
    )
	
class Crear_Division(forms.ModelForm):
	class Meta:
		model = Division
		fields = ['nombre', 'fotografia']
		
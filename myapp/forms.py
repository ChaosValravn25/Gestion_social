from django import forms
from .models import Division, Documento

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

# class Crear_Area(forms.Form):
#     titulo = forms.CharField(label="Titulo de area", max_length=200)
#     descripcion = forms.CharField(widget=forms.Textarea)
#     division = forms.ModelChoiceField(
#         queryset=Division.objects.all(),
#         label="Division",
#         empty_label="Seleccione una division"
#     )
    #archivo = MultipleFileField()  # Para manejar múltiples archivos
    
class Crear_Area(forms.Form):
    titulo = forms.CharField(label="Título de área", max_length=200)
    descripcion = forms.CharField(widget=forms.Textarea)


class Crear_Division(forms.ModelForm):
	class Meta:
		model = Division
		fields = ['nombre', 'fotografia']
		
class Crear_Documento(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['nombre_documento', 'documento', 'descripcion_documento']  # No incluir el campo 'area_trabajo'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configurar placeholder o estilos adicionales si es necesario
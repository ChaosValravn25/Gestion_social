from .models import Division, AreaTrabajo, Documento
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Crear_Area, Crear_Division, Crear_Documento
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def division(request):
	divisiones = Division.objects.all()
	return render(request, 'Divisiones/divisiones.html', {
		'divisiones': divisiones
	})

def area_trabajo(request):
	areas_trabajo = AreaTrabajo.objects.all()
	return render(request, 'Areas_trabajo/area_trabajo.html', {
		'areas_trabajo': areas_trabajo
	})

def crear_area(request, division_id):
    division = get_object_or_404(Division, pk=division_id)  # Obtiene la división actual por su ID

    if request.method == 'POST':
        form = Crear_Area(request.POST)
        if form.is_valid():
            # Crear el área de trabajo y asignar la división automáticamente
            area = AreaTrabajo(
                titulo=form.cleaned_data['titulo'],
                descripcion=form.cleaned_data['descripcion'],
                division=division  # Asignar la división actual
            )
            area.save()
            return redirect('division_detalle', division_id=division.id)

    else:
        form = Crear_Area()

    return render(request, 'Areas_trabajo/crear_area.html/', {'form': form, 'division': division})

def eliminar_area(request, area_id):
    if request.method == 'POST':
        area = get_object_or_404(AreaTrabajo, id=area_id)
        division_id = area.division.id  # Obtener la ID de la división antes de eliminar el área
        area.delete()
        messages.success(request, 'El área ha sido eliminada exitosamente.')
        return redirect('division_detalle', division_id=division_id)
    
# def eliminar_areas_seleccionadas(request):
#     if request.method == "POST":
#         areas_ids = request.POST.getlist('areas_seleccionadas')  # Obtiene las áreas seleccionadas
#         division_id = request.POST.get('division_id')  # Obtiene el division_id del formulario
#         print("Áreas seleccionadas:", areas_ids)  # Agrega esto para depuración
#         print("ID de división:", division_id)  # Agrega esto para depuración
#         if areas_ids:
#             AreaTrabajo.objects.filter(id__in=areas_ids).delete()  # Elimina las áreas seleccionadas
#             messages.success(request, "Áreas eliminadas correctamente.")
#         else:
#             messages.error(request, "No se seleccionó ninguna área.")
#         print("ID de división antes del redirect:", division_id)
#         return redirect('division_detalle', division_id=division_id)
#     return redirect('division_detalle', division_id=division_id)


def crear_documento(request, area_id):
    area_trabajo = get_object_or_404(AreaTrabajo, id=area_id)
    division = area_trabajo.division  # Obtener la división asociada al área

    if request.method == 'POST':
        form = Crear_Documento(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save(commit=False)
            documento.area_trabajo = area_trabajo  # Asignar el área de trabajo al documento
            documento.save()
            return redirect('division_detalle', division_id=division.id)
    else:
        form = Crear_Documento()

    # Agregar 'division' al contexto
    return render(request, 'Documentos/crear_documentos.html', {'form': form, 'area_trabajo': area_trabajo, 'division': division})


def eliminar_documento(request, documento_id):
    documento = get_object_or_404(Documento, id=documento_id)  # Obtiene el documento

    if request.method == 'POST':
        division_id = documento.area_trabajo.division.id  # Obtener el ID de la división desde el área de trabajo
        documento.delete()
        messages.success(request, 'El documento ha sido eliminado exitosamente.')
        return redirect('division_detalle', division_id=division_id)  # Redirigir a la vista de detalle de la división

    # En caso de que no sea una solicitud POST, puedes redirigir a otra parte o mostrar un mensaje de error
    return redirect('divisiones')

def crear_division(request):
	if request.method == 'GET':
		return render(request, 'Divisiones/crear_division.html',{
			'form': Crear_Division()
		})
	else:
		Division.objects.create(nombre=request.POST['nombre'], fotografia=request.FILES['fotografia'])
		return redirect('divisiones')
        
def divisiones_view(request):
    divisiones = Division.objects.all().prefetch_related('areatrabajo_set')  # Prefetch las áreas relacionadas
    return render(request, 'divisiones.html', {'divisiones': divisiones})

def division_detalle(request, division_id):
    division = get_object_or_404(Division, id=division_id)  
    documentos = Documento.objects.filter(area_trabajo__division=division)  # Obtener documentos relacionados
    form = Crear_Documento()
    context = {
        'division': division,
        'form': form,
        'documentos': documentos,  # Agregar documentos al contexto
    }
    return render(request, 'Divisiones/contenido.html', context)

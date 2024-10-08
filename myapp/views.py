from .models import Division, AreaTrabajo
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Crear_Area, Crear_Division

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

def crear_area(request):
    if request.method == 'GET':
        return render(request, 'Areas_trabajo/crear_area.html', {
            'form': Crear_Area()
        })
    else:
        form = Crear_Area(request.POST, request.FILES)  # Asegúrate de incluir request.FILES aquí
        if form.is_valid():  # Validar el formulario
            area_trabajo = AreaTrabajo.objects.create(
                titulo=form.cleaned_data['titulo'],
                descripcion=form.cleaned_data['descripcion'],
                division=form.cleaned_data['division'],
                archivo=form.cleaned_data['archivo']  # Agregar el archivo aquí
            )
            return redirect('divisiones')
        # Si el formulario no es válido, vuelve a mostrar el formulario con errores
        return render(request, 'Areas_trabajo/crear_area.html', {
            'form': form
        })

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
    return render(request, 'Divisiones/contenido.html', {
        'division': division
})
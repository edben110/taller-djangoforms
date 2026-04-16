from django.shortcuts import render, redirect

from .forms import AsistenciaForm


def registrar_asistencia(request):
    """Vista para mostrar y procesar el formulario de asistencia."""
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asistencia:confirmacion')
    else:
        form = AsistenciaForm()

    return render(request, 'asistencia/formulario.html', {'form': form})


def confirmacion(request):
    """Vista que muestra el mensaje de éxito tras registrar asistencia."""
    return render(request, 'asistencia/confirmacion.html')

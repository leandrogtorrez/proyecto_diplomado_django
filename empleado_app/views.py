from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#from django.shortcuts import render

from rest_framework import viewsets
from .models import Empleado, Departamento, Proyecto, Asignacion

from .serializers import(
    DepartamentoSerializer,
    EmpleadoSerializer,
    ProyectoSerializer,
    AsignacionSerializer,
)

# Create your views here.
class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer


class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer


# API personalizada para listar empleados por departamento
@api_view(['GET'])
def empleados_por_departamento(request, departamento_id):
    try:
        departamento = Departamento.objects.get(id=departamento_id)
        empleados = Empleado.objects.filter(departamento=departamento)
        serializer = EmpleadoSerializer(empleados, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Departamento.DoesNotExist:
        return Response(
            {'error': 'Departamento no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )

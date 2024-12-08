from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import(
    DepartamentoViewSet,
    EmpleadoViewSet,
    ProyectoViewSet,
    AsignacionViewSet,
    empleados_por_departamento,
)

router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'empleados', EmpleadoViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'asignaciones', AsignacionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('empleados/departamento/<int:departamento_id>/', empleados_por_departamento, name='empleados_por_departamento'),
]
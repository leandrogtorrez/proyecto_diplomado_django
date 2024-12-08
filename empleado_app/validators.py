import re #Que es re regular expression
from django.core.exceptions import ValidationError #Para validaciones personalizadas

def validar_solo_letras(valor):
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', valor):
        raise ValidationError(
            f'El campo "{valor}" solo puede contener letras y espacios ERROR.'
        )

def validar_dominio_correo(valor):
    dominio_permitido = "byhappystudio.com" #Correo de la empresa corporativa
    if not valor.endswith(f"@{dominio_permitido}"):
        raise ValidationError(
            f'El correo debe ser corporativo {dominio_permitido}.'
        )
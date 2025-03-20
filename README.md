# Catálogos del SAT en Python

Este repositorio contiene los catálogos del SAT convertidos en módulos de Python con enumeraciones (`StrEnum`), organizados dentro del paquete `sat.catalogos`.

## Instalación

Puedes instalar este paquete en tu proyecto utilizando `pip`:

```sh
uv add git+https://github.com/isaacasancheza/sat
```

## Uso

Una vez instalado, puedes importar los catálogos en tu código de la siguiente manera:

```python
from sat.catalogos.forma_pago import FormaPago

print(FormaPago.FP_01)  # Ejemplo de uso
```

## Estructura del Paquete

El paquete `sat.catalogos` contiene módulos individuales para cada catálogo, generados a partir del archivo de Excel del SAT. Cada módulo incluye una enumeración (`StrEnum`) con los valores del catálogo correspondiente.

Ejemplo de estructura:

```
sat/
  catalogos/
    __init__.py
    forma_pago.py
    moneda.py
    tipo_de_comprobante.py
    ...
```

## Pruebas

Para verificar que los módulos se importan correctamente, puedes ejecutar las pruebas:

```sh
pytest tests/test_imports.py
```

Esto validará que cada módulo de catálogo se importe sin errores.

## Notas

- Los catálogos fueron generados a partir del archivo de Excel del SAT y pueden actualizarse en futuras versiones.
- Si el SAT cambia el formato de los catálogos, se requerirá una nueva generación de los archivos.

## Licencia

Este proyecto se distribuye bajo la licencia LGPL-3.0.


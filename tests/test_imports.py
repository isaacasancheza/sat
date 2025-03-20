import importlib

import pytest


@pytest.mark.parametrize(
    'module_name',
    [
        'sat.catalogos.forma_pago',
        'sat.catalogos.moneda',
        'sat.catalogos.tipo_de_comprobante',
        'sat.catalogos.exportacion',
        'sat.catalogos.metodo_pago',
        'sat.catalogos.peridiocidad',
        'sat.catalogos.meses',
        'sat.catalogos.tipo_relacion',
        'sat.catalogos.regimen_fiscal',
        'sat.catalogos.pais',
        'sat.catalogos.uso_cfdi',
        'sat.catalogos.clave_unidad',
        'sat.catalogos.objeto_imp',
        'sat.catalogos.impuesto',
        'sat.catalogos.aduana',
        'sat.catalogos.tipo_factor',
    ],
)
def test_import_catalogos(
    module_name,
):
    """Verifica que los módulos de catálogo puedan importarse sin errores."""
    importlib.import_module(module_name)

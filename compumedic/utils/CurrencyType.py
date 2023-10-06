import locale
from decimal import Decimal

def format_money(value):
    # Establece el locale apropiado
    locale.setlocale(locale.LC_ALL, 'es_PE.UTF-8')

    # Configura la localización para Perú
    # Convierte la cadena de texto en un valor numérico
    value = Decimal(value)
    
    # Formatea el valor como una cadena de moneda
    formatted_currency = locale.currency(value, symbol=True, grouping=True)
    
    return formatted_currency

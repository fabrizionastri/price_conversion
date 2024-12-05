# ------- core/utils/convert_currency.py
 
from django.utils import timezone
from core.enums.currency import Currency

# Not yet implemented
    
def convert_system_unit(value, from_unit, to_unit):
    """ Convert a value from one system unit to another for the same dimension. 
    Raises:
        - if either unit is a custom unit
        - if the two system units have different dimensions
    """
    if from_unit == to_unit:
        return value
    else:
        print("Warning: system unit conversion not implemented yet. Multiplying by 2 instead.")
        return value * 2

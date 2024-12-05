# ------- core/utils/convert_currency.py
 
from django.utils import timezone
from core.enums.currency import Currency

# Not yet implemented
def convert_currency(value, from_currency: Currency = None, to_currency: Currency = None, date=None) -> Decimal:
    """ - Convert a value (price or amount) from one currency to another. 
    - Args:
        - value: The value to convert.
        - from_currency: The currency to convert from.
        - to_currency: The currency to convert to.
        - date: The date to use for the conversion rate. If None, the current date is used.
    - Returns:
        - The converted value if both currencies are different
        - The original value if either currency is None, or if they are the same.
    """
    if from_currency is None or to_currency is None or from_currency == to_currency:
        return value
    else:
        print("Warning: currency converion not implemented yet. Multiplying by 2 instead.")
        if not date: 
            date = timezone.now()
            
        return value * 2

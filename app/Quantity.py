from fhirclient.models import (
    quantity as qty
)

class Quantity:
    def __init__(self, value, comparator, unit, system, code):
        self.value = value
        self.comparator = comparator
        self.unit = unit
        self.system = system
        self.code = code

    def to_fhir(self):
        quantity = qty.Quantity()

        value = self.value
        quantity.value = value

        comparator = self.comparator
        quantity.comparator = comparator

        unit = self.unit
        quantity.unit = unit

        system = self.system
        quantity.system = system

        code = self.code
        quantity.code = code

        return quantity
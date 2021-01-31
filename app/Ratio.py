from fhirclient.models import (
    ratio as r
)

class Ratio:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def to_fhir(self):
        ratio = r.Ratio()

        numerator = self.numerator
        ratio.numerator = numerator

        denominator = self.denominator
        ratio.denominator = denominator

        return ratio
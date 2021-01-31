from fhirclient.models import (
    dosage as do
)

class Dosage:
    def __init__(self, route, rateRatio):
        self.route = route
        self.rateRatio = rateRatio

    def to_fhir(self):
        dosage = do.Dosage()

        route = self.route
        dosage.route = route

        doseAndRate = do.DosageDoseAndRate()
        rateRatio = self.rateRatio
        doseAndRate.rateRatio = rateRatio
        dosage.doseAndRate = [doseAndRate]

        return dosage
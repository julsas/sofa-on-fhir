from fhirclient.models import (
    identifier as idf,
    fhirreference as fr,
)

class Identifier:

    def __init__(self, use, idfType, system, value, period, assigner):
        self.use = use
        self.idfType = idfType
        self.system = system
        self.value = value
        self.period = period
        self.assigner = assigner

    def to_fhir(self):
        identifier = idf.Identifier()

        use = self.use
        identifier.use = use

        idfType = self.idfType
        identifier.type = idfType

        system = self.system
        identifier.system = system

        value = self.value
        identifier.value = value

        period = self.period
        identifier.period = period

        assigner = self.assigner
        identifier.assigner = assigner

        if self.assigner == None:
            pass
        else:
            assigner = fr.FHIRReference()
            assigner.reference = 'Organization/' + str(self.assigner)
            identifier.assigner = assigner

        return identifier
        
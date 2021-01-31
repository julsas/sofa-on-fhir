from fhirclient.models import (
    observation as obx,
    fhirdate as fd
)

class Component:
    def __init__(self, code, valueQuantity, valueCodeableConcept, valueString, valueDateTime, valueInteger):
        self.code = code
        self.valueQuantity = valueQuantity
        self.valueCodeableConcept = valueCodeableConcept
        self.valueString = valueString
        self.valueDateTime = valueDateTime
        self.valueInteger = valueInteger

    def to_fhir(self):
        component = obx.ObservationComponent()

        code = self.code
        component.code = code
        
        if self.valueQuantity == None:
            pass
        else:
            valueQuantity = self.valueQuantity
            component.valueQuantity = valueQuantity

        if self.valueCodeableConcept == None:
            pass
        else:
            valueCodeableConcept = self.valueCodeableConcept
            component.valueCodeableConcept = valueCodeableConcept

        if self.valueString == None:
            pass
        else:
            valueString = self.valueString
            component.valueString = valueString

        if self.valueDateTime == None:
            pass
        else:
            valueDateTime = fd.FHIRDate(self.valueDateTime)
            component.valueDateTime = valueDateTime

        if self.valueInteger == None:
            pass
        else:
            valueInteger = self.valueInteger
            component.valueInteger = valueInteger

        return component
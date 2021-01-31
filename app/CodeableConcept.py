from fhirclient.models import (
    codeableconcept as cc,
)

class CodeableConcept:

    def __init__(self, coding, text, extension):
        self.coding = coding
        self.text = text
        self.extension = extension

    def to_fhir(self):
        codeableConcept = cc.CodeableConcept()
        if self.coding == None:
            pass
        else:
            codeableConcept.coding = self.coding
        if self.text == None:
            pass
        else:
            codeableConcept.text = self.text
        if self.extension == None:
            pass
        else:
            codeableConcept.extension = [self.extension]

        return codeableConcept
        
from fhirclient.models import(
    coding as co,
)

class Coding:

    def __init__(self, system, version, code, display):
        self.system = system
        self.version = version
        self.code = code
        self.display = display

    def to_fhir(self):
        coding = co.Coding()
        coding.system = self.system
        coding.version = self.version
        coding.code = self.code
        coding.display = self.display

        return coding
import uuid

from fhirclient.models import (
    procedure as pcr,
    meta as ma,
    fhirdate as fd,
    fhirreference as fr
)

from app import (
    Coding,
    CodeableConcept
)

class Procedure:
    def __init__(self, resourceId, profile, status, category, code, subject, performedDateTime, performedPeriod, bodySite, report, note, usedCode):
        self.resourceId = resourceId
        self.profile = profile
        self.status = status
        self.category = category
        self.code = code
        self.subject = subject
        self.performedDateTime = performedDateTime
        self.performedPeriod = performedPeriod
        self.bodySite = bodySite
        self.report = report
        self.note = note
        self.usedCode = usedCode

    def to_fhir(self):
        procedure = pcr.Procedure()

        resourceId = self.resourceId
        procedure.id = str(resourceId)

        meta = ma.Meta()
        meta.profile = self.profile
        procedure.meta = meta

        status = self.status
        procedure.status = status

        category = self.category
        procedure.category = category

        code = self.code
        procedure.code = code

        subject = fr.FHIRReference()
        subject.reference = 'Patient/' + str(self.subject)
        procedure.subject = subject

        if self.performedDateTime == None:
            pass
        else:
            performedDateTime = fd.FHIRDate(self.performedDateTime)
            procedure.performedDateTime = performedDateTime

        if self.performedPeriod == None:
            pass
        else:
            performedPeriod = self.performedPeriod
            procedure.performedPeriod = performedPeriod

        bodySite = self.bodySite
        procedure.bodySite = bodySite

        if self.report == None:
            pass
        else:
            report = fr.FHIRReference()
            report.reference = 'DiagnosticReport/' + str(self.report)
            procedure.report = [report]

        note = self.note
        procedure.note = note

        if self.usedCode == None:
            pass
        else:
            usedCode = self.usedCode
            procedure.usedCode = usedCode

        return procedure

def create_vasopressor_therapy(patId, performedDateTime):
    
    resourceId = uuid.uuid4()

    profile = ['https://www.medizininformatik-initiative.de/fhir/core/modul-prozedur/StructureDefinition/Procedure']

    status = 'in-progress'

    respThpyCategorySystem = 'http://snomed.info/sct'
    respThpyCategoryCode = '18629005'
    respThpyCategoryDisplay = 'Administration of drug or medicament (procedure)'
    respThpyCategoryCoding = Coding.Coding(system=respThpyCategorySystem, version=None, code=respThpyCategoryCode, display=respThpyCategoryDisplay)
    respThpyCategoryCoding = [respThpyCategoryCoding.to_fhir()]
    respThpyCategory = CodeableConcept.CodeableConcept(coding=respThpyCategoryCoding, text=None, extension=None)
    respThpyCategory = respThpyCategory.to_fhir()

    respThpyCodeCode = '870386000'
    respThpyCodeSystem = 'http://snomed.info/sct'
    respThpyCodeDisplay = 'Vasopressor therapy (procedure)'
    respThpyCodeCoding = Coding.Coding(system=respThpyCodeSystem, version=None, code=respThpyCodeCode, display=respThpyCodeDisplay)
    respThpyCodeCoding = [respThpyCodeCoding.to_fhir()]
    respThpyCode = CodeableConcept.CodeableConcept(coding=respThpyCodeCoding, text=None, extension=None)
    respThpyCode = respThpyCode.to_fhir()

    subject = patId

    # need to implement how to handle data-absent on performedDateTime
    performedDateTime = performedDateTime

    vasopressor_therapy = Procedure(
        resourceId = resourceId,
        profile=profile,
        status=status,
        category=respThpyCategory,
        code=respThpyCode,
        subject=subject,
        performedDateTime=performedDateTime,
        performedPeriod=None,
        bodySite=None,
        report=None,
        note=None,
        usedCode=None
        )

    vasopressor_therapy = vasopressor_therapy.to_fhir()

    return vasopressor_therapy
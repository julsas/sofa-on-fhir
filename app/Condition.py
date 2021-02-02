import uuid

from fhirclient.models import (
    condition as cdn,
    meta as ma,
    fhirreference as fr,
    fhirdate as fd
)

from app import (
    Coding,
    CodeableConcept
)

class Condition:

    def __init__(self, resourceId, profile, presenceExtension, clinicalStatus, verificationStatus, category, severity, code, bodySite, subject, onsetDateTime, recordedDate, stage, note):
        self.resourceId = resourceId
        self.profile = profile
        self.presenceExtension = presenceExtension
        self.clinicalStatus = clinicalStatus
        self.verificationStatus = verificationStatus
        self.category = category
        self.severity = severity
        self.code = code
        self.bodySite = bodySite
        self.subject = subject
        self.onsetDateTime = onsetDateTime
        self.recordedDate = recordedDate
        self.stage = stage
        self.note = note

    def to_fhir(self):
        condition = cdn.Condition()

        resourceId = self.resourceId
        condition.id = str(resourceId)

        meta = ma.Meta()
        meta.profile = self.profile
        condition.meta = meta

        presenceExtension = self.presenceExtension
        condition.modifierExtension = presenceExtension
        
        clinicalStatus = self.clinicalStatus
        condition.clinicalStatus = clinicalStatus

        verificationStatus = self.verificationStatus
        condition.verificationStatus = verificationStatus

        category = self.category
        condition.category = [category]

        severity = self.severity
        condition.severity = severity

        code = self.code
        condition.code = code

        bodySite = self.bodySite
        condition.bodySite = bodySite

        subject = fr.FHIRReference()
        subject.reference = 'Patient/' + str(self.subject)
        condition.subject = subject

        if self.onsetDateTime == None:
            pass
        else:
            onsetDate = fd.FHIRDate(self.onsetDateTime)
            condition.onsetDateTime = onsetDate

        recordedDate = fd.FHIRDate(self.recordedDate)
        condition.recordedDate = recordedDate

        stage = self.stage
        condition.stage = stage

        note = self.note
        condition.note = note

        return condition

def create_dependence_on_ventilator(patId, present, recordedDate):
        
        profile = ['https://www.netzwerk-universitaetsmedizin.de/fhir/StructureDefinition/dependence-on-ventilator']

        resourceId = uuid.uuid4()

        # category
        categoryCode = '404989005'
        categorySystem = 'http://snomed.info/sct'
        categoryDisplay = 'Ventilation status (observable entity)'
        categoryCoding = Coding.Coding(system=categorySystem, version=None, code=categoryCode, display=categoryDisplay)
        categoryCoding = categoryCoding.to_fhir()
        category = CodeableConcept.CodeableConcept(coding=[categoryCoding], text=None, extension=None)
        category = category.to_fhir()

        # code
        conditionCode = '444932008'
        conditionSystem = 'http://snomed.info/sct'
        conditionDisplay = 'Dependence on ventilator (finding)'
        conditionCoding = Coding.Coding(system=conditionSystem, version=None, code=conditionCode, display=conditionDisplay)
        conditionCoding = conditionCoding.to_fhir()
        code = CodeableConcept.CodeableConcept(coding=[conditionCoding], text=None, extension=None)
        code = code.to_fhir()

        # subject
        subject = patId

        # recordedDate
        recordedDate = recordedDate

        if present == True:

            # Verification status
            verificationSystemHL7 = 'http://terminology.hl7.org/CodeSystem/condition-ver-status'
            verificationCodeHL7 = 'confirmed'
            verificationDisplayHL7 = 'Confirmed'
            verificationCodingHL7 = Coding.Coding(system=verificationSystemHL7, version=None, code=verificationCodeHL7, display=verificationDisplayHL7)
            verificationCodingHL7 = verificationCodingHL7.to_fhir()
            verificationSystem = 'http://snomed.info/sct'
            verificationCode = '410605003'
            verificationDisplay = 'Confirmed present (qualifier value)'
            verificationCoding = Coding.Coding(system=verificationSystem, version=None, code=verificationCode, display=verificationDisplay)
            verificationCoding = verificationCoding.to_fhir()
            verificationStatus = CodeableConcept.CodeableConcept(coding=[verificationCodingHL7, verificationCoding], text=None, extension=None)
            verificationStatus = verificationStatus.to_fhir()

            # Clinical status
            statusCode = 'active'
            statusSystem = 'http://terminology.hl7.org/CodeSystem/condition-clinical'
            statusDisplay = 'Active'
            clinicalStatusCoding = Coding.Coding(system=statusSystem, version=None, code=statusCode, display=statusDisplay)
            clinicalStatusCoding = clinicalStatusCoding.to_fhir()
            clinicalStatus = CodeableConcept.CodeableConcept(coding=[clinicalStatusCoding], text=None, extension=None)
            clinicalStatus = clinicalStatus.to_fhir()

            condition = Condition(
                resourceId=resourceId,
                profile=profile,
                presenceExtension=None,
                clinicalStatus=clinicalStatus,
                verificationStatus=verificationStatus,
                category=category,
                severity=None,
                code=code,
                bodySite=None,
                subject=subject,
                onsetDateTime=None,
                recordedDate=recordedDate,
                stage=None,
                note=None
            )

            condition = condition.to_fhir()

            return condition

        elif present == False:
        
            # Verification status
            verificationSystemHL7 = 'http://terminology.hl7.org/CodeSystem/condition-ver-status'
            verificationCodeHL7 = 'refuted'
            verificationDisplayHL7 = 'Refuted'
            verificationCodingHL7 = Coding.Coding(system=verificationSystemHL7, version=None, code=verificationCodeHL7, display=verificationDisplayHL7)
            verificationCodingHL7 = verificationCodingHL7.to_fhir()
            verificationSystem = 'http://snomed.info/sct'
            verificationCode = '410594000'
            verificationDisplay = 'Definitely NOT present (qualifier value)'
            verificationCoding = Coding.Coding(system=verificationSystem, version=None, code=verificationCode, display=verificationDisplay)
            verificationCoding = verificationCoding.to_fhir()
            verificationStatus = CodeableConcept.CodeableConcept(coding=[verificationCodingHL7, verificationCoding], text=None, extension=None)
            verificationStatus = verificationStatus.to_fhir()

            condition = Condition(
                resourceId=resourceId,
                profile=profile,
                presenceExtension=None,
                clinicalStatus=None,
                verificationStatus=verificationStatus,
                category=category,
                severity=None,
                code=code,
                bodySite=None,
                subject=subject,
                onsetDateTime=None,
                recordedDate=recordedDate,
                stage=None,
                note=None
            )

            condition = condition.to_fhir()

            return condition
from sys import version
import uuid

from fhirclient.models import (
    medicationstatement as ms,
    meta as ma,
    fhirreference as fr,
    fhirdate as fd
)
from fhirclient.models.dosage import Dosage
from fhirclient.models.quantity import Quantity

from app import (
    Coding,
    CodeableConcept,
    Quantity,
    Ratio,
    Dosage
)

class MedicationStatement:
    def __init__(self, resourceId, profile, partOf, status, category, medication, subject, effectiveDateTime, dosage, reasonCode):
        self.resourceId = resourceId
        self.profile = profile
        self.partOf = partOf
        self.status = status 
        self.category = category
        self.medication = medication 
        self.subject = subject 
        self.effectiveDateTime = effectiveDateTime
        self.dosage = dosage
        self.reasonCode = reasonCode

    def to_fhir(self):
        medicationStatement = ms.MedicationStatement()

        resourceId = self.resourceId
        medicationStatement.id = str(resourceId)

        meta = ma.Meta()
        meta.profile = self.profile
        medicationStatement.meta = meta

        if self.partOf == None:
            pass
        else:
            partOf = fr.FHIRReference()
            partOf.reference = 'Procedure/' + str(self.partOf)
            medicationStatement.partOf = [partOf]

        status = self.status 
        medicationStatement.status = status 

        category = self.category 
        medicationStatement.category = category 

        medication = self.medication
        medicationStatement.medicationCodeableConcept = medication 

        subject = fr.FHIRReference()
        subject.reference = 'Patient/' + str(self.subject)
        medicationStatement.subject = subject

        effectiveDateTime = fd.FHIRDate(self.effectiveDateTime)
        medicationStatement.effectiveDateTime = effectiveDateTime

        dosage = self.dosage
        medicationStatement.dosage = dosage

        reasonCode = self.reasonCode
        medicationStatement.reasonCode = reasonCode

        return medicationStatement

def create_dopamine(patId, partOf, effectiveDateTime, rateRatioNumeratorValue):
    
    resourceId = uuid.uuid4()

    profile = ['https://www.medizininformatik-initiative.de/fhir/core/modul-medikation/StructureDefinition/MedicationStatement']

    partOf = partOf
    
    status = 'active'

    medCodeSystem = 'http://snomed.info/sct'
    medCodeCode = '59187003'
    medCodeDisplay = 'Product containing dopamine (medicinal product)'
    medCodeCoding = Coding.Coding(system=medCodeSystem, version=None, code=medCodeCode, display=medCodeDisplay)
    medCodeCoding = medCodeCoding.to_fhir()
    medCodeSystem2 = 'http://snomed.info/sct'
    medCodeCode2 = '412383006'
    medCodeDisplay2 = 'Dopamine (substance)'
    medCodeCoding2 = Coding.Coding(system=medCodeSystem2, version=None, code=medCodeCode2, display=medCodeDisplay2)
    medCodeCoding2 = medCodeCoding2.to_fhir()
    medCodeSystemATC = 'http://fhir.de/CodeSystem/dimdi/atc'
    medCodeCodeATC = 'C01CA04'
    medCodeDisplayATC = 'Dopamin'
    medCodeCodingATC = Coding.Coding(system=medCodeSystemATC, version=None, code=medCodeCodeATC, display=medCodeDisplayATC)
    medCodeCodingATC = medCodeCodingATC.to_fhir()
    medCodeText = 'Dopamin'
    medCode = CodeableConcept.CodeableConcept(coding=[medCodeCoding, medCodeCoding2, medCodeCodingATC], text=medCodeText, extension=None)
    medCode = medCode.to_fhir()

    subject = patId

    effectiveDateTime = effectiveDateTime

    routeSystem = 'http://standardterms.edqm.eu'
    routeCode = '20045000'
    routeDisplay = 'Intravenous use'
    routeCoding = Coding.Coding(system=routeSystem, version=None, code=routeCode, display=routeDisplay)
    routeCoding = routeCoding.to_fhir()
    route = CodeableConcept.CodeableConcept(coding=[routeCoding], text=None, extension=None)
    route = route.to_fhir()

    rateRatioNumeratorValue = rateRatioNumeratorValue
    rateRatioNumeratorUnit = 'microgram'
    rateRatioNumeratorSystem = 'http://unitsofmeasure.org'
    rateRatioNumeratorCode = 'ug'
    rateRatioNumerator = Quantity.Quantity(value=rateRatioNumeratorValue, comparator=None, unit=rateRatioNumeratorUnit, system=rateRatioNumeratorSystem, code=rateRatioNumeratorCode)
    rateRatioNumerator = rateRatioNumerator.to_fhir()

    rateRatioDenominatorValue = 1
    rateRatioDenominatorUnit = 'hour'
    rateRatioDenominatorSystem = 'http://unitsofmeasure.org'
    rateRatioDenominatorCode = 'h'
    rateRatioDenominator = Quantity.Quantity(value=rateRatioDenominatorValue, comparator=None, unit=rateRatioDenominatorUnit, system=rateRatioDenominatorSystem, code=rateRatioDenominatorCode)
    rateRatioDenominator = rateRatioDenominator.to_fhir()

    rateRatio = Ratio.Ratio(numerator=rateRatioNumerator, denominator=rateRatioDenominator)
    rateRatio = rateRatio.to_fhir()

    dosage = Dosage.Dosage(route=route, rateRatio=rateRatio)
    dosage = dosage.to_fhir()

    medicationStatement = MedicationStatement(
        resourceId=resourceId,
        profile=profile,
        partOf=partOf if not None else None,
        status=status,
        category=None,
        medication=medCode,
        subject=subject,
        effectiveDateTime=effectiveDateTime,
        dosage=[dosage],
        reasonCode=None
    )

    medicationStatement = medicationStatement.to_fhir()

    return medicationStatement

def create_adrenaline(patId, partOf, effectiveDateTime, rateRatioNumeratorValue):
    
    resourceId = uuid.uuid4()

    profile = ['https://www.medizininformatik-initiative.de/fhir/core/modul-medikation/StructureDefinition/MedicationStatement']

    partOf = partOf
    
    status = 'active'

    medCodeSystem = 'http://snomed.info/sct'
    medCodeCode = '65502005'
    medCodeDisplay = 'Product containing epinephrine (medicinal product)'
    medCodeCoding = Coding.Coding(system=medCodeSystem, version=None, code=medCodeCode, display=medCodeDisplay)
    medCodeCoding = medCodeCoding.to_fhir()
    medCodeSystem2 = 'http://snomed.info/sct'
    medCodeCode2 = '387362001'
    medCodeDisplay2 = 'Epinephrine (substance)'
    medCodeCoding2 = Coding.Coding(system=medCodeSystem2, version=None, code=medCodeCode2, display=medCodeDisplay2)
    medCodeCoding2 = medCodeCoding2.to_fhir()
    medCodeSystemATC = 'http://fhir.de/CodeSystem/dimdi/atc'
    medCodeCodeATC = 'C01CA24'
    medCodeDisplayATC = 'Epinephrin'
    medCodeCodingATC = Coding.Coding(system=medCodeSystemATC, version=None, code=medCodeCodeATC, display=medCodeDisplayATC)
    medCodeCodingATC = medCodeCodingATC.to_fhir()
    medCodeText = 'Adrenalin'
    medCode = CodeableConcept.CodeableConcept(coding=[medCodeCoding, medCodeCoding2, medCodeCodingATC], text=medCodeText, extension=None)
    medCode = medCode.to_fhir()

    subject = patId

    effectiveDateTime = effectiveDateTime

    routeSystem = 'http://standardterms.edqm.eu'
    routeCode = '20045000'
    routeDisplay = 'Intravenous use'
    routeCoding = Coding.Coding(system=routeSystem, version=None, code=routeCode, display=routeDisplay)
    routeCoding = routeCoding.to_fhir()
    route = CodeableConcept.CodeableConcept(coding=[routeCoding], text=None, extension=None)
    route = route.to_fhir()

    rateRatioNumeratorValue = rateRatioNumeratorValue
    rateRatioNumeratorUnit = 'microgram'
    rateRatioNumeratorSystem = 'http://unitsofmeasure.org'
    rateRatioNumeratorCode = 'ug'
    rateRatioNumerator = Quantity.Quantity(value=rateRatioNumeratorValue, comparator=None, unit=rateRatioNumeratorUnit, system=rateRatioNumeratorSystem, code=rateRatioNumeratorCode)
    rateRatioNumerator = rateRatioNumerator.to_fhir()

    rateRatioDenominatorValue = 1
    rateRatioDenominatorUnit = 'hour'
    rateRatioDenominatorSystem = 'http://unitsofmeasure.org'
    rateRatioDenominatorCode = 'h'
    rateRatioDenominator = Quantity.Quantity(value=rateRatioDenominatorValue, comparator=None, unit=rateRatioDenominatorUnit, system=rateRatioDenominatorSystem, code=rateRatioDenominatorCode)
    rateRatioDenominator = rateRatioDenominator.to_fhir()

    rateRatio = Ratio.Ratio(numerator=rateRatioNumerator, denominator=rateRatioDenominator)
    rateRatio = rateRatio.to_fhir()

    dosage = Dosage.Dosage(route=route, rateRatio=rateRatio)
    dosage = dosage.to_fhir()

    medicationStatement = MedicationStatement(
        resourceId=resourceId,
        profile=profile,
        partOf=partOf if not None else None,
        status=status,
        category=None,
        medication=medCode,
        subject=subject,
        effectiveDateTime=effectiveDateTime,
        dosage=[dosage],
        reasonCode=None
    )

    medicationStatement = medicationStatement.to_fhir()

    return medicationStatement

def create_noradrenaline(patId, partOf, effectiveDateTime, rateRatioNumeratorValue):
    
    resourceId = uuid.uuid4()

    profile = ['https://www.medizininformatik-initiative.de/fhir/core/modul-medikation/StructureDefinition/MedicationStatement']

    partOf = partOf
    
    status = 'active'

    medCodeSystem = 'http://snomed.info/sct'
    medCodeCode = '111130009'
    medCodeDisplay = 'Product containing norepinephrine (medicinal product)'
    medCodeCoding = Coding.Coding(system=medCodeSystem, version=None, code=medCodeCode, display=medCodeDisplay)
    medCodeCoding = medCodeCoding.to_fhir()
    medCodeSystem2 = 'http://snomed.info/sct'
    medCodeCode2 = '45555007'
    medCodeDisplay2 = 'Norepinephrine (substance)'
    medCodeCoding2 = Coding.Coding(system=medCodeSystem2, version=None, code=medCodeCode2, display=medCodeDisplay2)
    medCodeCoding2 = medCodeCoding2.to_fhir()
    medCodeSystemATC = 'http://fhir.de/CodeSystem/dimdi/atc'
    medCodeCodeATC = 'C01CA03'
    medCodeDisplayATC = 'Norepinephrin'
    medCodeCodingATC = Coding.Coding(system=medCodeSystemATC, version=None, code=medCodeCodeATC, display=medCodeDisplayATC)
    medCodeCodingATC = medCodeCodingATC.to_fhir()
    medCodeText = 'Norepinephrin'
    medCode = CodeableConcept.CodeableConcept(coding=[medCodeCoding, medCodeCoding2, medCodeCodingATC], text=medCodeText, extension=None)
    medCode = medCode.to_fhir()

    subject = patId

    effectiveDateTime = effectiveDateTime

    routeSystem = 'http://standardterms.edqm.eu'
    routeCode = '20045000'
    routeDisplay = 'Intravenous use'
    routeCoding = Coding.Coding(system=routeSystem, version=None, code=routeCode, display=routeDisplay)
    routeCoding = routeCoding.to_fhir()
    route = CodeableConcept.CodeableConcept(coding=[routeCoding], text=None, extension=None)
    route = route.to_fhir()

    rateRatioNumeratorValue = rateRatioNumeratorValue
    rateRatioNumeratorUnit = 'microgram'
    rateRatioNumeratorSystem = 'http://unitsofmeasure.org'
    rateRatioNumeratorCode = 'ug'
    rateRatioNumerator = Quantity.Quantity(value=rateRatioNumeratorValue, comparator=None, unit=rateRatioNumeratorUnit, system=rateRatioNumeratorSystem, code=rateRatioNumeratorCode)
    rateRatioNumerator = rateRatioNumerator.to_fhir()

    rateRatioDenominatorValue = 1
    rateRatioDenominatorUnit = 'hour'
    rateRatioDenominatorSystem = 'http://unitsofmeasure.org'
    rateRatioDenominatorCode = 'h'
    rateRatioDenominator = Quantity.Quantity(value=rateRatioDenominatorValue, comparator=None, unit=rateRatioDenominatorUnit, system=rateRatioDenominatorSystem, code=rateRatioDenominatorCode)
    rateRatioDenominator = rateRatioDenominator.to_fhir()

    rateRatio = Ratio.Ratio(numerator=rateRatioNumerator, denominator=rateRatioDenominator)
    rateRatio = rateRatio.to_fhir()

    dosage = Dosage.Dosage(route=route, rateRatio=rateRatio)
    dosage = dosage.to_fhir()

    medicationStatement = MedicationStatement(
        resourceId=resourceId,
        profile=profile,
        partOf=partOf if not None else None,
        status=status,
        category=None,
        medication=medCode,
        subject=subject,
        effectiveDateTime=effectiveDateTime,
        dosage=[dosage],
        reasonCode=None
    )

    medicationStatement = medicationStatement.to_fhir()

    return medicationStatement
import uuid

from fhirclient.models import (
    observation as obx,
    meta as ma,
    fhirreference as fr,
    fhirdate as fd,
)

from app import (
    Coding,
    CodeableConcept,
    Identifier,
    Quantity,
    Component
)

# generic FHIR Observation class
class Observation:

    def __init__(self, resourceId, profile, identifier, status, category, code, subject, effectiveDate, valueQuantity, valueCodeableConcept, valueInteger, dataAbsentReason, interpretation, note, bodySite, method, referenceRange, member, component):
        self.resourceId = resourceId
        self.profile = profile
        self.identifier = identifier
        self.status = status
        self.category = category
        self.code = code
        self.subject = subject
        self.effectiveDate = effectiveDate
        self.valueQuantity = valueQuantity
        self.valueCodeableConcept = valueCodeableConcept
        self.valueInteger = valueInteger
        self.dataAbsentReason = dataAbsentReason
        self.interpretation = interpretation 
        self.note = note 
        self.bodySite = bodySite
        self.method = method 
        self.referenceRange = referenceRange
        self.member = member
        self.component = component

    def to_fhir(self):
        observation = obx.Observation()

        resourceId = self.resourceId
        observation.id = str(resourceId)

        if self.profile == None:
            pass
        else:
            meta = ma.Meta()
            meta.profile = self.profile
            observation.meta = meta

        identifier = self.identifier
        observation.identifier = identifier

        status = self.status
        observation.status = status

        category = self.category
        observation.category = [category]

        code = self.code
        observation.code = code

        subject = fr.FHIRReference()
        subject.reference = 'Patient/' + str(self.subject)
        observation.subject = subject

        effectiveDate = fd.FHIRDate(self.effectiveDate)
        observation.effectiveDateTime = effectiveDate

        valueQuantity = self.valueQuantity
        observation.valueQuantity = valueQuantity

        valueCodeableConcept = self.valueCodeableConcept
        observation.valueCodeableConcept = valueCodeableConcept

        valueInteger = self.valueInteger
        observation.valueInteger = valueInteger

        dataAbsentReason = self.dataAbsentReason
        observation.dataAbsentReason = dataAbsentReason
        
        interpretation = self.interpretation
        observation.interpretation = interpretation
        
        note = self.note
        observation.note = note
        
        bodySite = self.bodySite
        observation.bodySite = bodySite
        
        method = self.method
        observation.method = method
        
        referenceRange = self.referenceRange
        observation.referenceRange = referenceRange
        
        if self.member == None:
            pass
        else:
            members = []
            for member in self.member:
                members.append(member)
                observation.hasMember = members
        
        if self.component == None:
            pass
        else:
            components = []
            for component in self.component:
                components.append(component)
                observation.component = components

        return observation

# paO2        
def create_oxygen_partial_pressure(patId, effectiveDateTime, valuePaCO2):
    resourceId = uuid.uuid4()

    profile = ['https://www.netzwerk-universitaetsmedizin.de/fhir/StructureDefinition/carbon-dioxide-partial-pressure']

    idfTypeSystem = 'http://terminology.hl7.org/CodeSystem/v2-0203'
    idfTypeCode = 'OBI'
    idfTypeCoding = Coding.Coding(system=idfTypeSystem, version=None, code=idfTypeCode, display=None)
    idfTypeCoding = [idfTypeCoding.to_fhir()]
    idfType = CodeableConcept.CodeableConcept(coding=idfTypeCoding, text=None, extension=None)
    idfType = idfType.to_fhir()
    idfSystem = 'https://www.charite.de/fhir/CodeSystem/lab-identifiers'
    idfCode = '2019-8_paCO2'
    idfAssigner = 'Charité'
    obsIdentifier = Identifier.Identifier(use=None, idfType=idfType, system=idfSystem, value=idfCode, period=None, assigner=idfAssigner)
    obsIdentifier = [obsIdentifier.to_fhir()]

    obsStatus = 'final'

    categoryLoincSystem = 'http://loinc.org'
    categoryLoincCode = '26436-6'
    categoryLoincCoding = Coding.Coding(system=categoryLoincSystem, version=None, code=categoryLoincCode, display=None)
    categoryLoincCoding = categoryLoincCoding.to_fhir()
    categoryObsSystem = 'http://terminology.hl7.org/CodeSystem/observation-category'
    categoryObsCode = 'laboratory'
    categoryObsCoding = Coding.Coding(system=categoryObsSystem, version=None, code=categoryObsCode, display=None)
    categoryObsCoding = categoryObsCoding.to_fhir()
    categoryLoincSystemstudies = 'http://loinc.org'
    categoryLoincCodestudies = '18767-4'
    categoryLoincCodingstudies = Coding.Coding(system=categoryLoincSystemstudies, version=None, code=categoryLoincCodestudies, display=None)
    categoryLoincCodingstudies = categoryLoincCodingstudies.to_fhir()
    obsCategory = CodeableConcept.CodeableConcept(coding=[categoryLoincCoding, categoryObsCoding, categoryLoincCodingstudies], text=None, extension=None)
    obsCategory = obsCategory.to_fhir()

    obsCodeSystem = 'http://loinc.org'
    obsCodeCode = '2019-8'
    obsCodeDisplay = 'Carbon dioxide [Partial pressure] in Arterial blood'
    obsCodeCoding = Coding.Coding(system=obsCodeSystem, version=None, code=obsCodeCode, display=obsCodeDisplay)
    obsCodeCoding = [obsCodeCoding.to_fhir()]
    obsCodeText = 'paCO2'
    obsCode = CodeableConcept.CodeableConcept(coding=obsCodeCoding, text=obsCodeText, extension=None)
    obsCode = obsCode.to_fhir()

    subject = patId

    effectiveDate = effectiveDateTime

    obsValueQuantityValue = valuePaCO2
    obsValueQuantityUnit = 'mmHg'
    obsValueQuantitySystem = 'http://unitsofmeasure.org'
    obsValueQuantityCode = 'mm[Hg]'
    obsValueQuantity = Quantity.Quantity(value=obsValueQuantityValue, comparator=None, unit=obsValueQuantityUnit, system=obsValueQuantitySystem, code=obsValueQuantityCode)
    obsValueQuantity = obsValueQuantity.to_fhir()

    obs = Observation(
        resourceId=resourceId,
        profile=profile,
        identifier=obsIdentifier,
        status=obsStatus,
        category=obsCategory,
        code=obsCode,
        subject=subject,
        effectiveDate=effectiveDate,
        valueQuantity=obsValueQuantity,
        valueCodeableConcept=None,
        valueInteger=None,
        dataAbsentReason=None,
        interpretation=None,
        note=None,
        bodySite=None,
        method=None,
        referenceRange=None,
        member=None,
        component=None)

    obs = obs.to_fhir()

    return obs

# FiO2
def create_inhaled_oxygen_concentration(patId, effectiveDateTime, valueFiO2):

    resourceId = uuid.uuid4()

    profile = ['https://www.netzwerk-universitaetsmedizin.de/fhir/StructureDefinition/inhaled-oxygen-concentration']

    idfTypeSystem = 'http://terminology.hl7.org/CodeSystem/v2-0203'
    idfTypeCode = 'OBI'
    idfTypeCoding = Coding.Coding(system=idfTypeSystem, version=None, code=idfTypeCode, display=None)
    idfTypeCoding = [idfTypeCoding.to_fhir()]
    idfType = CodeableConcept.CodeableConcept(coding=idfTypeCoding, text=None, extension=None)
    idfType = idfType.to_fhir()
    idfSystem = 'https://www.charite.de/fhir/CodeSystem/lab-identifiers'
    idfCode = '3150-0_FiO2'
    idfAssigner = 'Charité'
    obsIdentifier = Identifier.Identifier(use=None, idfType=idfType, system=idfSystem, value=idfCode, period=None, assigner=idfAssigner)
    obsIdentifier = [obsIdentifier.to_fhir()]

    obsStatus = 'final'

    categoryLoincSystem = 'http://loinc.org'
    categoryLoincCode = '26436-6'
    categoryLoincCoding = Coding.Coding(system=categoryLoincSystem, version=None, code=categoryLoincCode, display=None)
    categoryLoincCoding = categoryLoincCoding.to_fhir()
    categoryObsSystem = 'http://terminology.hl7.org/CodeSystem/observation-category'
    categoryObsCode = 'laboratory'
    categoryObsCoding = Coding.Coding(system=categoryObsSystem, version=None, code=categoryObsCode, display=None)
    categoryObsCoding = categoryObsCoding.to_fhir()
    categoryLoincSystemstudies = 'http://loinc.org'
    categoryLoincCodestudies = '18767-4'
    categoryLoincCodingstudies = Coding.Coding(system=categoryLoincSystemstudies, version=None, code=categoryLoincCodestudies, display=None)
    categoryLoincCodingstudies = categoryLoincCodingstudies.to_fhir()
    obsCategory = CodeableConcept.CodeableConcept(coding=[categoryLoincCoding, categoryObsCoding, categoryLoincCodingstudies], text=None, extension=None)
    obsCategory = obsCategory.to_fhir()

    obsCodeSystem = 'http://loinc.org'
    obsCodeCode = '3150-0'
    obsCodeDisplay = 'Inhaled oxygen concentration'
    obsCodeCoding = Coding.Coding(system=obsCodeSystem, version=None, code=obsCodeCode, display=obsCodeDisplay)
    obsCodeCoding = [obsCodeCoding.to_fhir()]
    obsCodeText = 'FiO2'
    obsCode = CodeableConcept.CodeableConcept(coding=obsCodeCoding, text=obsCodeText, extension=None)
    obsCode = obsCode.to_fhir()

    subject = patId

    effectiveDate = effectiveDateTime

    obsValueQuantityValue = valueFiO2
    obsValueQuantityUnit = '%'
    obsValueQuantitySystem = 'http://unitsofmeasure.org'
    obsValueQuantityCode = '%'
    obsValueQuantity = Quantity.Quantity(value=obsValueQuantityValue, comparator=None, unit=obsValueQuantityUnit, system=obsValueQuantitySystem, code=obsValueQuantityCode)
    obsValueQuantity = obsValueQuantity.to_fhir()

    obs = Observation(
        resourceId=resourceId,
        profile=profile,
        identifier=obsIdentifier,
        status=obsStatus,
        category=obsCategory,
        code=obsCode,
        subject=subject,
        effectiveDate=effectiveDate,
        valueQuantity=obsValueQuantity,
        valueCodeableConcept=None,
        valueInteger=None,
        dataAbsentReason=None,
        interpretation=None,
        note=None,
        bodySite=None,
        method=None,
        referenceRange=None,
        member=None,
        component=None)

    obs = obs.to_fhir()

    return obs

# BodyWeight
def create_body_weight(patId, effectiveDateTime, valueKilogram, valueGram):
    
    resourceId = uuid.uuid4()

    profile = ['https://www.netzwerk-universitaetsmedizin.de/fhir/StructureDefinition/body-weight']

    idfTypeSystem = 'http://terminology.hl7.org/CodeSystem/v2-0203'
    idfTypeCode = 'OBI'
    idfTypeCoding = Coding.Coding(system=idfTypeSystem, version=None, code=idfTypeCode, display=None)
    idfTypeCoding = [idfTypeCoding.to_fhir()]
    idfType = CodeableConcept.CodeableConcept(coding=idfTypeCoding, text=None, extension=None)
    idfType = idfType.to_fhir()
    idfSystem = 'https://www.charite.de/fhir/CodeSystem/observation-identifiers'
    idfCode = '29463-7' + '_' + 'BodyWeight'
    idfAssigner = 'Charité'
    obsIdentifier = Identifier.Identifier(use=None, idfType=idfType, system=idfSystem, value=idfCode, period=None, assigner=idfAssigner)
    obsIdentifier = [obsIdentifier.to_fhir()]

    obsStatus = 'final'

    categoryObsSystem = 'http://terminology.hl7.org/CodeSystem/observation-category'
    categoryObsCode = 'vital-signs'
    categoryObsCoding = Coding.Coding(system=categoryObsSystem, version=None, code=categoryObsCode, display=None)
    categoryObsCoding = categoryObsCoding.to_fhir()
    obsCategory = CodeableConcept.CodeableConcept(coding=[categoryObsCoding], text=None, extension=None)
    obsCategory = obsCategory.to_fhir()

    obsCodeSystemLn = 'http://loinc.org'
    obsCodeCodeLn = '29463-7'
    obsCodeDisplayLn = 'Body weight'
    obsCodeCodingLn = Coding.Coding(system=obsCodeSystemLn, version=None, code=obsCodeCodeLn, display=obsCodeDisplayLn)
    obsCodeCodingLn = obsCodeCodingLn.to_fhir()
    obsCodeSystemSCT = 'http://snomed.info/sct'
    obsCodeCodeSCT = '27113001'
    obsCodeDisplaySCT = 'Body weight (observable entity)'
    obsCodeCodingSCT = Coding.Coding(system=obsCodeSystemSCT, version=None, code=obsCodeCodeSCT, display=obsCodeDisplaySCT)
    obsCodeCodingSCT = obsCodeCodingSCT.to_fhir()
    obsCodeText = 'Body weight'
    obsCode = CodeableConcept.CodeableConcept(coding=[obsCodeCodingLn, obsCodeCodingSCT], text=obsCodeText, extension=None)
    obsCode = obsCode.to_fhir()

    subject = patId

    effectiveDate = effectiveDateTime

    if valueKilogram == None:
        pass
    else:
        obsQuantityValue = valueKilogram
        obsQuantityUnit = 'kilogram'
        obsQuantitySystem = 'http://unitsofmeasure.org'
        obsQuantityCode = 'kg' 
        obsQuantity = Quantity.Quantity(value=obsQuantityValue, comparator=None, unit=obsQuantityUnit, system=obsQuantitySystem, code=obsQuantityCode)
        obsQuantity = obsQuantity.to_fhir()

    if valueGram == None:
        pass
    else:
        obsQuantityValue = valueKilogram
        obsQuantityUnit = 'gram'
        obsQuantitySystem = 'http://unitsofmeasure.org'
        obsQuantityCode = 'g' 
        obsQuantity = Quantity.Quantity(value=obsQuantityValue, comparator=None, unit=obsQuantityUnit, system=obsQuantitySystem, code=obsQuantityCode)
        obsQuantity = obsQuantity.to_fhir()

    obsBodyWeight = Observation(
        resourceId=resourceId,
        profile=profile,
        identifier=obsIdentifier,
        status=obsStatus,
        category=obsCategory,
        code=obsCode,
        subject=subject,
        effectiveDate=effectiveDate,
        valueQuantity=obsQuantity,
        valueCodeableConcept=None,
        valueInteger=None,
        dataAbsentReason=None,
        interpretation=None,
        note=None,
        bodySite=None,
        method=None,
        referenceRange=None,
        member=None,
        component=None
    )

    obsBodyWeight = obsBodyWeight.to_fhir()
    
    return obsBodyWeight

# Glasgow Coma Scale
def create_glasgow_coma_scale(patId, effectiveDateTime, valueTotalScore, valueEye, valueVerbal, valueMotor):

    resourceId = uuid.uuid4()

    profile = None

    idfTypeSystem = 'http://terminology.hl7.org/CodeSystem/v2-0203'
    idfTypeCode = 'OBI'
    idfTypeCoding = Coding.Coding(system=idfTypeSystem, version=None, code=idfTypeCode, display=None)
    idfTypeCoding = [idfTypeCoding.to_fhir()]
    idfType = CodeableConcept.CodeableConcept(coding=idfTypeCoding, text=None, extension=None)
    idfType = idfType.to_fhir()
    idfSystem = 'https://www.charite.de/fhir/CodeSystem/observation-identifiers'
    idfCode = '9269-2' + '_' + 'GlasgowComaScale'
    idfAssigner = 'Charité'
    obsIdentifier = Identifier.Identifier(use=None, idfType=idfType, system=idfSystem, value=idfCode, period=None, assigner=idfAssigner)
    obsIdentifier = [obsIdentifier.to_fhir()]

    obsStatus = 'final'

    categoryObsSystem = 'http://terminology.hl7.org/CodeSystem/observation-category'
    categoryObsCode = 'survey'
    categoryObsCoding = Coding.Coding(system=categoryObsSystem, version=None, code=categoryObsCode, display=None)
    categoryObsCoding = categoryObsCoding.to_fhir()
    obsCategory = CodeableConcept.CodeableConcept(coding=[categoryObsCoding], text=None, extension=None)
    obsCategory = obsCategory.to_fhir()

    obsCodeSystem = 'http://loinc.org'
    obsCodeCode = '9269-2'
    obsCodeDisplay = 'Glasgow coma score total'
    obsCodeCoding = Coding.Coding(system=obsCodeSystem, version=None, code=obsCodeCode, display=obsCodeDisplay)
    obsCodeCoding = obsCodeCoding.to_fhir()
    obsCodeSystemSCT = 'http://snomed.info/sct'
    obsCodeCodeSCT = '248241002'
    obsCodeDisplaySCT = 'Glasgow coma score (observable entity)'
    obsCodeCodingSCT = Coding.Coding(system=obsCodeSystemSCT, version=None, code=obsCodeCodeSCT, display=obsCodeDisplaySCT)
    obsCodeCodingSCT = obsCodeCodingSCT.to_fhir()
    obsCodeText = 'Glasgow Coma Scale (GCS) score'
    obsCode = CodeableConcept.CodeableConcept(coding=[obsCodeCoding, obsCodeCodingSCT], text=obsCodeText, extension=None)
    obsCode = obsCode.to_fhir()

    subject = patId

    effectiveDate = effectiveDateTime

    obsMethodSystem = 'http://snomed.info/sct'
    obsMethodCode = '386554004'
    obsMethodDisplay = 'Glasgow coma scale (assessment scale)' 
    obsMethodCoding = Coding.Coding(system=obsMethodSystem, version=None, code=obsMethodCode, display=obsMethodDisplay)
    obsMethodCoding = obsMethodCoding.to_fhir()
    obsMethod = CodeableConcept.CodeableConcept(coding=[obsMethodCoding], text=None, extension=None)
    obsMethod = obsMethod.to_fhir()

    obsQuantityValue = valueTotalScore
    obsQuantityUnit = 'score'
    obsQuantitySystem = 'http://unitsofmeasure.org'
    obsQuantityCode = '{score}' 
    obsQuantity = Quantity.Quantity(value=obsQuantityValue, comparator=None, unit=obsQuantityUnit, system=obsQuantitySystem, code=obsQuantityCode)
    obsQuantity = obsQuantity.to_fhir()

    #Eye opening
    verbalCompCodeSystemLn = 'http://loinc.org'
    verbalCompCodeLn = '9267-6'
    verbalCompCodeDisplayLn = 'Glasgow coma score eye opening'
    verbalCompCodingLn = Coding.Coding(system=verbalCompCodeSystemLn, version=None, code=verbalCompCodeLn, display=verbalCompCodeDisplayLn)
    verbalCompCodingLn = verbalCompCodingLn.to_fhir()
    verbalCompCodeText = 'Eye opening response'
    verbalCompCode = CodeableConcept.CodeableConcept(coding=[verbalCompCodingLn], text=verbalCompCodeText, extension=None)
    verbalCompCode = verbalCompCode.to_fhir()
    
    verbalCompValueInt = valueEye

    verbalComp = Component.Component(code=verbalCompCode, valueQuantity=None, valueCodeableConcept=None, valueString=None, valueDateTime=None, valueInteger=verbalCompValueInt)
    verbalComp = verbalComp.to_fhir()

    # Verbal
    verbalCompCodeSystemLn = 'http://loinc.org'
    verbalCompCodeLn = '9270-0'
    verbalCompCodeDisplayLn = 'Glasgow coma score verbal'
    verbalCompCodingLn = Coding.Coding(system=verbalCompCodeSystemLn, version=None, code=verbalCompCodeLn, display=verbalCompCodeDisplayLn)
    verbalCompCodingLn = verbalCompCodingLn.to_fhir()
    verbalCompCodeText = 'Verbal response'
    verbalCompCode = CodeableConcept.CodeableConcept(coding=[verbalCompCodingLn], text=verbalCompCodeText, extension=None)
    verbalCompCode = verbalCompCode.to_fhir()
    
    verbalCompValueInt = valueVerbal

    verbalComp = Component.Component(code=verbalCompCode, valueQuantity=None, valueCodeableConcept=None, valueString=None, valueDateTime=None, valueInteger=verbalCompValueInt)
    verbalComp = verbalComp.to_fhir()

    # Motor
    motorCompCodeSystemLn = 'http://loinc.org'
    motorCompCodeLn = '9268-4'
    motorCompCodeDisplayLn = 'Glasgow coma score motor'
    motorCompCodingLn = Coding.Coding(system=motorCompCodeSystemLn, version=None, code=motorCompCodeLn, display=motorCompCodeDisplayLn)
    motorCompCodingLn = motorCompCodingLn.to_fhir()
    motorCompCodeText = 'Motor response'
    motorCompCode = CodeableConcept.CodeableConcept(coding=[motorCompCodingLn], text=motorCompCodeText, extension=None)
    motorCompCode = motorCompCode.to_fhir()
    
    motorCompValueInt = valueMotor

    motorComp = Component.Component(code=motorCompCode, valueQuantity=None, valueCodeableConcept=None, valueString=None, valueDateTime=None, valueInteger=motorCompValueInt)
    motorComp = motorComp.to_fhir()

    obs = Observation(
        resourceId=resourceId,
        profile=profile if not None else None,
        identifier=obsIdentifier,
        status=obsStatus,
        category=obsCategory,
        code=obsCode,
        subject=subject,
        effectiveDate=effectiveDate,
        valueQuantity=obsQuantity,
        valueCodeableConcept=None,
        valueInteger=None,
        dataAbsentReason=None,
        interpretation=None,
        note=None,
        bodySite=None,
        method=obsMethod,
        referenceRange=None,
        member=None,
        component=[verbalComp, verbalComp, motorComp])

    obs = obs.to_fhir()

    return obs

# Bilirubin
def create_bilirubin(patId, effectiveDateTime, value):
    
    resourceId = uuid.uuid4()

    profile = ['https://www.medizininformatik-initiative.de/fhir/core/modul-labor/StructureDefinition/ObservationLab']

    idfTypeSystem = 'http://terminology.hl7.org/CodeSystem/v2-0203'
    idfTypeCode = 'OBI'
    idfTypeCoding = Coding.Coding(system=idfTypeSystem, version=None, code=idfTypeCode, display=None)
    idfTypeCoding = [idfTypeCoding.to_fhir()]
    idfType = CodeableConcept.CodeableConcept(coding=idfTypeCoding, text=None, extension=None)
    idfType = idfType.to_fhir()
    idfSystem = 'https://www.charite.de/fhir/CodeSystem/lab-identifiers'
    idfCode = '1971-1_Bilirubin'
    idfAssigner = 'Charité'
    obsIdentifier = Identifier.Identifier(use=None, idfType=idfType, system=idfSystem, value=idfCode, period=None, assigner=idfAssigner)
    obsIdentifier = [obsIdentifier.to_fhir()]

    obsStatus = 'final'

    categoryLoincSystem = 'http://loinc.org'
    categoryLoincCode = '26436-6'
    categoryLoincCoding = Coding.Coding(system=categoryLoincSystem, version=None, code=categoryLoincCode, display=None)
    categoryLoincCoding = categoryLoincCoding.to_fhir()
    categoryObsSystem = 'http://terminology.hl7.org/CodeSystem/observation-category'
    categoryObsCode = 'laboratory'
    categoryObsCoding = Coding.Coding(system=categoryObsSystem, version=None, code=categoryObsCode, display=None)
    categoryObsCoding = categoryObsCoding.to_fhir()
    obsCategory = CodeableConcept.CodeableConcept(coding=[categoryLoincCoding, categoryObsCoding], text=None, extension=None)
    obsCategory = obsCategory.to_fhir()

    obsCodeSystem = 'http://loinc.org'
    obsCodeCode = '1974-5'
    obsCodeDisplay = 'Bilirubin.total [Mass/volume] in Body fluid'
    obsCodeCoding = Coding.Coding(system=obsCodeSystem, version=None, code=obsCodeCode, display=obsCodeDisplay)
    obsCodeCoding = [obsCodeCoding.to_fhir()]
    obsCodeText = 'Bilirubin gesamt'
    obsCode = CodeableConcept.CodeableConcept(coding=obsCodeCoding, text=obsCodeText, extension=None)
    obsCode = obsCode.to_fhir()

    subject = patId

    effectiveDate = effectiveDateTime

    obsValueQuantityValue = value
    obsValueQuantityUnit = 'mg/dL'
    obsValueQuantitySystem = 'http://unitsofmeasure.org'
    obsValueQuantityCode = 'mg/dL'
    obsValueQuantity = Quantity.Quantity(value=obsValueQuantityValue, comparator=None, unit=obsValueQuantityUnit, system=obsValueQuantitySystem, code=obsValueQuantityCode)
    obsValueQuantity = obsValueQuantity.to_fhir()

    observation = Observation(
        resourceId=resourceId,
        profile=profile,
        identifier=obsIdentifier,
        status=obsStatus,
        category=obsCategory,
        code=obsCode,
        subject=subject,
        effectiveDate=effectiveDate,
        valueQuantity=obsValueQuantity,
        valueCodeableConcept=None,
        valueInteger=None,
        dataAbsentReason=None,
        interpretation=None,
        note=None,
        bodySite=None,
        method=None,
        referenceRange=None,
        member=None,
        component=None)

    observation = observation.to_fhir()

    return observation

# Platelets
def create_platelets(patId, effectiveDateTime, value):
    
    resourceId = uuid.uuid4()

    profile = ['https://www.medizininformatik-initiative.de/fhir/core/modul-labor/StructureDefinition/ObservationLab']

    idfTypeSystem = 'http://terminology.hl7.org/CodeSystem/v2-0203'
    idfTypeCode = 'OBI'
    idfTypeCoding = Coding.Coding(system=idfTypeSystem, version=None, code=idfTypeCode, display=None)
    idfTypeCoding = [idfTypeCoding.to_fhir()]
    idfType = CodeableConcept.CodeableConcept(coding=idfTypeCoding, text=None, extension=None)
    idfType = idfType.to_fhir()
    idfSystem = 'https://www.charite.de/fhir/CodeSystem/lab-identifiers'
    idfCode = '777-3_Platelets'
    idfAssigner = 'Charité'
    obsIdentifier = Identifier.Identifier(use=None, idfType=idfType, system=idfSystem, value=idfCode, period=None, assigner=idfAssigner)
    obsIdentifier = [obsIdentifier.to_fhir()]

    obsStatus = 'final'

    categoryLoincSystem = 'http://loinc.org'
    categoryLoincCode = '26436-6'
    categoryLoincCoding = Coding.Coding(system=categoryLoincSystem, version=None, code=categoryLoincCode, display=None)
    categoryLoincCoding = categoryLoincCoding.to_fhir()
    categoryObsSystem = 'http://terminology.hl7.org/CodeSystem/observation-category'
    categoryObsCode = 'laboratory'
    categoryObsCoding = Coding.Coding(system=categoryObsSystem, version=None, code=categoryObsCode, display=None)
    categoryObsCoding = categoryObsCoding.to_fhir()
    obsCategory = CodeableConcept.CodeableConcept(coding=[categoryLoincCoding, categoryObsCoding], text=None, extension=None)
    obsCategory = obsCategory.to_fhir()

    obsCodeSystem = 'http://loinc.org'
    obsCodeCode = '777-3'
    obsCodeDisplay = 'Platelets [#/volume] in Blood by Automated count'
    obsCodeCoding = Coding.Coding(system=obsCodeSystem, version=None, code=obsCodeCode, display=obsCodeDisplay)
    obsCodeCoding = [obsCodeCoding.to_fhir()]
    obsCodeText = 'Platelets'
    obsCode = CodeableConcept.CodeableConcept(coding=obsCodeCoding, text=obsCodeText, extension=None)
    obsCode = obsCode.to_fhir()

    subject = patId

    effectiveDate = effectiveDateTime

    obsValueQuantityValue = value
    obsValueQuantityUnit = 'per nanoliter'
    obsValueQuantitySystem = 'http://unitsofmeasure.org'
    obsValueQuantityCode = '/nL'
    obsValueQuantity = Quantity.Quantity(value=obsValueQuantityValue, comparator=None, unit=obsValueQuantityUnit, system=obsValueQuantitySystem, code=obsValueQuantityCode)
    obsValueQuantity = obsValueQuantity.to_fhir()

    observation = Observation(
        resourceId=resourceId,
        profile=profile,
        identifier=obsIdentifier,
        status=obsStatus,
        category=obsCategory,
        code=obsCode,
        subject=subject,
        effectiveDate=effectiveDate,
        valueQuantity=obsValueQuantity,
        valueCodeableConcept=None,
        valueInteger=None,
        dataAbsentReason=None,
        interpretation=None,
        note=None,
        bodySite=None,
        method=None,
        referenceRange=None,
        member=None,
        component=None)

    observation = observation.to_fhir()

    return observation

# Creatinine
def create_creatinine(patId, effectiveDateTime, value):
    
    resourceId = uuid.uuid4()

    profile = ['https://www.medizininformatik-initiative.de/fhir/core/modul-labor/StructureDefinition/ObservationLab']

    idfTypeSystem = 'http://terminology.hl7.org/CodeSystem/v2-0203'
    idfTypeCode = 'OBI'
    idfTypeCoding = Coding.Coding(system=idfTypeSystem, version=None, code=idfTypeCode, display=None)
    idfTypeCoding = [idfTypeCoding.to_fhir()]
    idfType = CodeableConcept.CodeableConcept(coding=idfTypeCoding, text=None, extension=None)
    idfType = idfType.to_fhir()
    idfSystem = 'https://www.charite.de/fhir/CodeSystem/lab-identifiers'
    idfCode = '2160-0_Creatinine'
    idfAssigner = 'Charité'
    obsIdentifier = Identifier.Identifier(use=None, idfType=idfType, system=idfSystem, value=idfCode, period=None, assigner=idfAssigner)
    obsIdentifier = [obsIdentifier.to_fhir()]

    obsStatus = 'final'

    categoryLoincSystem = 'http://loinc.org'
    categoryLoincCode = '26436-6'
    categoryLoincCoding = Coding.Coding(system=categoryLoincSystem, version=None, code=categoryLoincCode, display=None)
    categoryLoincCoding = categoryLoincCoding.to_fhir()
    categoryObsSystem = 'http://terminology.hl7.org/CodeSystem/observation-category'
    categoryObsCode = 'laboratory'
    categoryObsCoding = Coding.Coding(system=categoryObsSystem, version=None, code=categoryObsCode, display=None)
    categoryObsCoding = categoryObsCoding.to_fhir()
    obsCategory = CodeableConcept.CodeableConcept(coding=[categoryLoincCoding, categoryObsCoding], text=None, extension=None)
    obsCategory = obsCategory.to_fhir()

    obsCodeSystem = 'http://loinc.org'
    obsCodeCode = '2160-0'
    obsCodeDisplay = 'Creatinine [Mass/volume] in Serum or Plasma'
    obsCodeCoding = Coding.Coding(system=obsCodeSystem, version=None, code=obsCodeCode, display=obsCodeDisplay)
    obsCodeCoding = [obsCodeCoding.to_fhir()]
    obsCodeText = 'Creatinine'
    obsCode = CodeableConcept.CodeableConcept(coding=obsCodeCoding, text=obsCodeText, extension=None)
    obsCode = obsCode.to_fhir()

    subject = patId

    effectiveDate = effectiveDateTime

    obsValueQuantityValue = value
    obsValueQuantityUnit = 'mg/dL'
    obsValueQuantitySystem = 'http://unitsofmeasure.org'
    obsValueQuantityCode = 'mg/dL'
    obsValueQuantity = Quantity.Quantity(value=obsValueQuantityValue, comparator=None, unit=obsValueQuantityUnit, system=obsValueQuantitySystem, code=obsValueQuantityCode)
    obsValueQuantity = obsValueQuantity.to_fhir()

    observation = Observation(
        resourceId=resourceId,
        profile=profile,
        identifier=obsIdentifier,
        status=obsStatus,
        category=obsCategory,
        code=obsCode,
        subject=subject,
        effectiveDate=effectiveDate,
        valueQuantity=obsValueQuantity,
        valueCodeableConcept=None,
        valueInteger=None,
        dataAbsentReason=None,
        interpretation=None,
        note=None,
        bodySite=None,
        method=None,
        referenceRange=None,
        member=None,
        component=None)

    observation = observation.to_fhir()

    return observation

# Mean blood pressure
def create_mean_blood_pressure(patId, effectiveDateTime, value):
    
    resourceId = uuid.uuid4()

    profile = None

    idfTypeSystem = 'http://terminology.hl7.org/CodeSystem/v2-0203'
    idfTypeCode = 'OBI'
    idfTypeCoding = Coding.Coding(system=idfTypeSystem, version=None, code=idfTypeCode, display=None)
    idfTypeCoding = [idfTypeCoding.to_fhir()]
    idfType = CodeableConcept.CodeableConcept(coding=idfTypeCoding, text=None, extension=None)
    idfType = idfType.to_fhir()
    idfSystem = 'https://www.charite.de/fhir/CodeSystem/observation-identifiers'
    idfCode = '8478-0' + '_' + 'MeanBloodPressure'
    idfAssigner = 'Charité'
    obsIdentifier = Identifier.Identifier(use=None, idfType=idfType, system=idfSystem, value=idfCode, period=None, assigner=idfAssigner)
    obsIdentifier = [obsIdentifier.to_fhir()]

    obsStatus = 'final'

    categoryObsSystem = 'http://terminology.hl7.org/CodeSystem/observation-category'
    categoryObsCode = 'vital-signs'
    categoryObsCoding = Coding.Coding(system=categoryObsSystem, version=None, code=categoryObsCode, display=None)
    categoryObsCoding = categoryObsCoding.to_fhir()
    obsCategory = CodeableConcept.CodeableConcept(coding=[categoryObsCoding], text=None, extension=None)
    obsCategory = obsCategory.to_fhir()

    obsCodeSystemLn = 'http://loinc.org'
    obsCodeCodeLn = '8478-0'
    obsCodeDisplayLn = 'Mean blood pressure'
    obsCodeCodingLn = Coding.Coding(system=obsCodeSystemLn, version=None, code=obsCodeCodeLn, display=obsCodeDisplayLn)
    obsCodeCodingLn = obsCodeCodingLn.to_fhir()
    obsCodeSystemSCT = 'http://snomed.info/sct'
    obsCodeCodeSCT = '6797001'
    obsCodeDisplaySCT = 'Mean blood pressure (observable entity)'
    obsCodeCodingSCT = Coding.Coding(system=obsCodeSystemSCT, version=None, code=obsCodeCodeSCT, display=obsCodeDisplaySCT)
    obsCodeCodingSCT = obsCodeCodingSCT.to_fhir()
    obsCodeText = 'Mean arterial pressure (MAP)'
    obsCode = CodeableConcept.CodeableConcept(coding=[obsCodeCodingLn, obsCodeCodingSCT], text=obsCodeText, extension=None)
    obsCode = obsCode.to_fhir()

    subject = patId

    effectiveDate = effectiveDateTime

    obsQuantityValue = value
    obsQuantityUnit = 'mmHg'
    obsQuantitySystem = 'http://unitsofmeasure.org'
    obsQuantityCode = 'mm[Hg]' 
    obsQuantity = Quantity.Quantity(value=obsQuantityValue, comparator=None, unit=obsQuantityUnit, system=obsQuantitySystem, code=obsQuantityCode)
    obsQuantity = obsQuantity.to_fhir()

    observation = Observation(
        resourceId=resourceId,
        profile=profile,
        identifier=obsIdentifier,
        status=obsStatus,
        category=obsCategory,
        code=obsCode,
        subject=subject,
        effectiveDate=effectiveDate,
        valueQuantity=obsQuantity,
        valueCodeableConcept=None,
        valueInteger=None,
        dataAbsentReason=None,
        interpretation=None,
        note=None,
        bodySite=None,
        method=None,
        referenceRange=None,
        member=None,
        component=None
    )

    observation = observation.to_fhir()
    
    return observation
import uuid
import datetime
import random

from fhirclient.models import (
    patient as p,
    meta as ma,
    fhirdate as fd,
)

from app import (
    Coding,
    CodeableConcept,
    Identifier
)

class Patient:

    def __init__(self, patientId, profile, identifier, dateOfBirth):
        self.patientId = patientId
        self.profile = profile
        self.identifier = identifier
        self.dateOfBirth = dateOfBirth

    def to_fhir(self):
        patient = p.Patient()
        patientId = self.patientId
        patient.id = str(patientId)

        if self.profile == None:
            pass
        else:
            meta = ma.Meta()
            meta.profile = self.profile
            patient.meta = meta

        identifier = self.identifier
        patient.identifier = identifier

        if self.dateOfBirth == None:
            pass
        else:
            dateOfBirth = fd.FHIRDate(self.dateOfBirth)
            patient.birthDate = dateOfBirth

        return patient

def create_patient(mrn, dateOfBirth):
    
    patId = uuid.uuid4()
    
    profile = None

    idfTypeSystem = 'http://terminology.hl7.org/CodeSystem/v2-0203'
    idfTypeCode = 'MR'
    idfTypeCoding = Coding.Coding(system=idfTypeSystem, version=None, code=idfTypeCode, display=None)
    idfTypeCoding = [idfTypeCoding.to_fhir()]
    idfType = CodeableConcept.CodeableConcept(coding=idfTypeCoding, text=None, extension=None)
    idfType = idfType.to_fhir()
    idfSystem = 'https://www.charite.de/fhir/CodeSystem/medical-record-numbers'
    idfCode = mrn
    idfAssigner = 'Charité'
    identifier = Identifier.Identifier(use=None, idfType=idfType, system=idfSystem, value=idfCode, period=None, assigner=idfAssigner)
    identifier = [identifier.to_fhir()]

    birthDate = dateOfBirth

    patient = Patient(
        patientId=patId, 
        profile=profile if not None else None,
        identifier=identifier,
        dateOfBirth=birthDate
        )
    patient = patient.to_fhir()
    
    return patient

def random_birth_date():
    start_date = datetime.date(1920, 1, 1)
    end_date = datetime.date(1990, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_birth_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_birth_date

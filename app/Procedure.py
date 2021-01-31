from fhirclient.models import (
    procedure as pcr,
    meta as ma,
    fhirdate as fd,
    fhirreference as fr
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

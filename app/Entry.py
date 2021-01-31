from fhirclient.models import (
    bundle as bdl
)

class Entry:

    def __init__(self, full_url, resource, request):
        self.full_url = full_url
        self.resource = resource
        self.request = request

    def to_fhir(self):
        entry = bdl.BundleEntry()

        full_url = self.full_url
        entry.fullUrl = full_url

        resource = self.resource
        entry.resource = resource

        request = self.request
        entry.request = request

        return entry
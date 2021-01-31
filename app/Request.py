from fhirclient.models import (
    bundle as bdl
)

class Request:

    def __init__(self, method, url):
        self.method = method
        self.url = url

    def to_fhir(self):
        request = bdl.BundleEntryRequest()

        method = self.method
        request.method = method

        url = self.url
        request.url = url

        return request
from fhirclient.models import (
    bundle as bdl,
    meta as ma,
    fhirdate as fd
)

class Bundle:

    def __init__(self, profile, identifier, bundle_type, timestamp, entry):
        self.profile = profile
        self.identifier = identifier
        self.bundle_type = bundle_type
        self.timestamp = timestamp
        self.entry = entry

    def to_fhir(self):
        bundle = bdl.Bundle()

        if self.profile == None:
            pass
        else:
            meta = ma.Meta()
            meta.profile = self.profile
            bundle.meta = meta

        identifier = self.identifier
        bundle.identifier = identifier

        bundle_type = self.bundle_type
        bundle.type = bundle_type

        timestamp = fd.FHIRDate(self.timestamp)
        bundle.timestamp = timestamp

        if self.entry == None:
            pass
        else:
            entries = []
            for entry in self.entry:
                entries.append(entry)
                bundle.entry = entries

        return bundle 

def create_bundle(timestamp, bundle_entries):

    # profile = None
    
    bundle_type = 'transaction'

    timestamp = timestamp

    bundle = Bundle(
        profile=None,
        identifier=None,
        bundle_type=bundle_type,
        timestamp=timestamp,
        entry=bundle_entries
    )

    bundle = bundle.to_fhir()

    return bundle
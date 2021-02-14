from app.Procedure import create_vasopressor_therapy
from app.Condition import create_dependence_on_ventilator
from app.Bundle import create_bundle
from app.MedicationStatement import create_adrenaline, create_dopamine, create_noradrenaline
from app.Patient import create_patient, random_birth_date
from app.Observation import create_bilirubin, create_body_weight, create_creatinine, create_glasgow_coma_scale, create_inhaled_oxygen_concentration, create_mean_blood_pressure, create_oxygen_partial_pressure, create_platelets, create_urine_output
from app import Request, Entry
import datetime
import json
from json import dumps
import random
from random import choices, randint
import yaml
from requests import post

def yaml_loader(filepath):
    with open(filepath, 'r') as settings_file:
        settings = yaml.safe_load(settings_file)
    return settings

settings = yaml_loader('settings.yaml')

fhir_server_enabled = settings['fhir-server']['enabled']
fhir_server_url = settings['fhir-server']['url']
number_of_patients = settings['data-generation']['number-of-patients']
local_output = settings['data-generation']['dumb-locally']
dependence_on_ventilator = settings['data-generation']['dependence-on-ventilator']

fhir_server = str(fhir_server_url)
headers = {
    'Accept':'application/fhir+json; fhirVersion=4.0',
    'Content-Type':'application/fhir+json; fhirVersion=4.0'
    }


i = 0
while i < number_of_patients:

    dateTime = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
    dateTime = str(dateTime)

    resources = []

    # Patient
    patient = create_patient(
        mrn=str(randint(10000000, 99999999)),
        dateOfBirth=str(random_birth_date())
    )
    resources.append(patient)

    if local_output == False:
        pass
    else:
        fname = 'Patient-' + str(patient.id) + '.json'
        with open('data/' + fname, 'w') as outfile:
            json.dump(patient.as_json(), outfile, indent=4)
        print("json written to file {fn}".format(fn=fname))

    # Body weight
    valueWeight = random.randrange(50, 130)
    weight = create_body_weight(
        patId=str(patient.id),
        effectiveDateTime=dateTime,
        valueKilogram=valueWeight,
        valueGram=None
    )

    resources.append(weight)

    if local_output == False:
        pass
    else:
        fname = 'Observation-body-weight-' + str(weight.id) + '.json'
        with open('data/' + fname, 'w') as outfile:
            json.dump(weight.as_json(), outfile, indent=4)
        print("json written to file {fn}".format(fn=fname))

    # PaO2
    valuePaO2 = random.randrange(60, 100)
    paO2 = create_oxygen_partial_pressure(
            patId=str(patient.id),
            effectiveDateTime=dateTime,
            valuePaCO2=valuePaO2
        )

    resources.append(paO2)

    if local_output == False:
        pass
    else:
        fname = 'Observation-laboratory-paO2-' + str(paO2.id) + '.json'
        with open('data/' + fname, 'w') as outfile:
            json.dump(paO2.as_json(), outfile, indent=4)
        print("json written to file {fn}".format(fn=fname))

    # FiO2
    valuesFiO2 = [23, 24, 28, 31, 35, 40, 50, 60, 90]
    valueFiO2 = random.choice(valuesFiO2)
    fiO2 = create_inhaled_oxygen_concentration(
        patId=str(patient.id),
        effectiveDateTime=dateTime,
        valueFiO2=valueFiO2
    )
    
    resources.append(fiO2)

    if local_output == False:
        pass
    else:
        fname = 'Observation-laboratory-fiO2-' + str(fiO2.id) + '.json'
        with open('data/' + fname, 'w') as outfile:
            json.dump(fiO2.as_json(), outfile, indent=4)
        print("json written to file {fn}".format(fn=fname))

    # Glasgow Coma Scale
    valuesEye = [1, 2, 3, 4]
    valEye = random.choice(valuesEye)
    valuesVerbal = [1, 2, 3, 4, 5]
    valVerbal = random.choice(valuesVerbal)
    valuesMotor = [1, 2, 3, 4, 5, 6]
    valMotor = random.choice(valuesMotor)
    valTotal = (valEye + valVerbal + valMotor)

    gcs = create_glasgow_coma_scale(
        patId=str(patient.id),
        effectiveDateTime=dateTime,
        valueTotalScore=valTotal,
        valueEye=valEye,
        valueVerbal=valVerbal,
        valueMotor=valMotor
    )

    resources.append(gcs)

    if local_output == False:
        pass
    else:
        fname = 'Observation-glasgow-coma-scale-' + str(gcs.id) + '.json'
        with open('data/' + fname, 'w') as outfile:
            json.dump(gcs.as_json(), outfile, indent=4)
        print("json written to file {fn}".format(fn=fname))

    # Bilirubin
    valueBilirubin = random.uniform(0.5, 13.0)
    valueBilirubin = round(valueBilirubin,2)
    bilirubin = create_bilirubin(
        patId=str(patient.id),
        effectiveDateTime=dateTime,
        value=valueBilirubin
    )

    resources.append(bilirubin)

    if local_output == False:
        pass
    else:
        fname = 'Observation-laboratory-bilirubin-' + str(bilirubin.id) + '.json'
        with open('data/' + fname, 'w') as outfile:
            json.dump(bilirubin.as_json(), outfile, indent=4)
        print("json written to file {fn}".format(fn=fname))

    # Creatinine
    valueCreatinine = random.uniform(0.0, 6.0)
    valueCreatinine = round(valueCreatinine,2)
    creatinine = create_creatinine(
        patId=str(patient.id),
        effectiveDateTime=dateTime,
        value=valueCreatinine
    )

    resources.append(creatinine)

    if local_output == False:
        pass
    else:
        fname = 'Observation-laboratory-creatinine-' + str(creatinine.id) + '.json'
        with open('data/' + fname, 'w') as outfile:
            json.dump(creatinine.as_json(), outfile, indent=4)
        print("json written to file {fn}".format(fn=fname))

    # Platelets
    valuePlatelets = random.randrange(10, 160)
    platelets = create_platelets(
        patId=str(patient.id),
        effectiveDateTime=dateTime,
        value=valuePlatelets
    )

    resources.append(platelets)

    if local_output == False:
        pass
    else:
        fname = 'Observation-laboratory-platelets-' + str(platelets.id) + '.json'
        with open('data/' + fname, 'w') as outfile:
            json.dump(platelets.as_json(), outfile, indent=4)
        print("json written to file {fn}".format(fn=fname))

    # Mean blood pressure
    valueMAP = random.randrange(50, 110)
    map = create_mean_blood_pressure(
        patId=str(patient.id),
        effectiveDateTime=dateTime,
        value=valueMAP
    )

    resources.append(map)

    if local_output == False:
        pass
    else:
        fname = 'Observation-mean-arterial-pressure-' + str(map.id) + '.json'
        with open('data/' + fname, 'w') as outfile:
            json.dump(map.as_json(), outfile, indent=4)
        print("json written to file {fn}".format(fn=fname))

    # 24h Urine
    valueUrine = random.uniform(0.1, 2.0)
    valueUrine = round(valueUrine, 1)
    urine = create_urine_output(
        patId=str(patient.id),
        effectiveDateTime=dateTime,
        value=valueUrine
    )

    resources.append(urine)

    if local_output == False:
        pass
    else:
        fname = 'Observation-urine-output-24h-' + str(urine.id) + '.json'
        with open('data/' + fname, 'w') as outfile:
            json.dump(urine.as_json(), outfile, indent=4)
        print("json written to file {fn}".format(fn=fname))

    # Vasopressors
    presences = [True, False]
    presence = random.choice(presences)
    if presence == False:
        pass
    else:

        vasopressor_therapy = create_vasopressor_therapy(
            patId=str(patient.id),
            performedDateTime=dateTime
        )

        resources.append(vasopressor_therapy)

        if local_output == False:
            pass
        else:
            fname = 'Procedure-vasopressor-therapy-' + str(vasopressor_therapy.id) + '.json'
            with open('data/' + fname, 'w') as outfile:
                json.dump(vasopressor_therapy.as_json(), outfile, indent=4)
            print("json written to file {fn}".format(fn=fname))

        vasopressor_presences = ['dopamine', 'adrenaline', 'noradrenaline']
        vasopressor_presences = random.choice(vasopressor_presences)

        if vasopressor_presences == 'dopamine':
            rateRatioNumeratorValues = [5, 10, 20]
            rateRatioNumeratorValue = random.choice(rateRatioNumeratorValues)
            rateRatioNumeratorValue = (rateRatioNumeratorValue*valueWeight)
            dopa = create_dopamine(
                patId=str(patient.id),
                partOf=str(vasopressor_therapy.id),
                effectiveDateTime=dateTime,
                rateRatioNumeratorValue=rateRatioNumeratorValue
            )

            resources.append(dopa)

            if local_output == False:
                pass
            else:
                fname = 'MedicationStatement-dopamine-' + str(dopa.id) + '.json'
                with open('data/' + fname, 'w') as outfile:
                    json.dump(dopa.as_json(), outfile, indent=4)
                print("json written to file {fn}".format(fn=fname))
        
        elif vasopressor_presences == 'adrenaline':
            rateRatioNumeratorValues = [0.1, 0.2, 0.3]
            rateRatioNumeratorValue = random.choice(rateRatioNumeratorValues)
            rateRatioNumeratorValue = (rateRatioNumeratorValue*valueWeight)
            adre = create_adrenaline(
                patId=str(patient.id),
                partOf=str(vasopressor_therapy.id),
                effectiveDateTime=dateTime,
                rateRatioNumeratorValue=rateRatioNumeratorValue
            )

            resources.append(adre)

            if local_output == False:
                pass
            else:
                fname = 'MedicationStatement-adrenaline-' + str(adre.id) + '.json'
                with open('data/' + fname, 'w') as outfile:
                    json.dump(adre.as_json(), outfile, indent=4)
                print("json written to file {fn}".format(fn=fname))

        elif vasopressor_presences == 'noradrenaline':
            rateRatioNumeratorValues = [0.1, 0.2, 0.3]
            rateRatioNumeratorValue = random.choice(rateRatioNumeratorValues)
            rateRatioNumeratorValue = (rateRatioNumeratorValue*valueWeight)
            nora = create_noradrenaline(
                patId=str(patient.id),
                partOf=str(vasopressor_therapy.id),
                effectiveDateTime=dateTime,
                rateRatioNumeratorValue=rateRatioNumeratorValue
            )

            resources.append(nora)

            if local_output == False:
                pass
            else:
                fname = 'MedicationStatement-noradrenaline-' + str(nora.id) + '.json'
                with open('data/' + fname, 'w') as outfile:
                    json.dump(nora.as_json(), outfile, indent=4)
                print("json written to file {fn}".format(fn=fname))

    # Dependence on ventilator
    dependence = create_dependence_on_ventilator(
        patId=str(patient.id),
        present=dependence_on_ventilator,
        recordedDate=dateTime
    )

    if local_output == False:
        pass
    else:
        fname = 'Condition-dependence-on-ventilator-' + str(dependence.id) + '.json'
        with open('data/' + fname, 'w') as outfile:
            json.dump(dependence.as_json(), outfile, indent=4)
        print("json written to file {fn}".format(fn=fname))

    resources.append(dependence)

    bundle_entries = []
    for resource in resources:
        full_url = 'urn:uuid:' + str(resource.id)
        resource = resource
        if resource.resource_type == 'Patient':
            req_method = 'PUT'
            req_url = str(resource.resource_type) + '/' + str(resource.id)
        elif resource.resource_type == 'Procedure':
            req_method = 'PUT'
            req_url = str(resource.resource_type) + '/' + str(resource.id)
        else:
            req_method = 'POST'
            req_url = str(resource.resource_type)

        request = Request.Request(method=req_method, url=req_url)
        request = request.to_fhir()
        entry = Entry.Entry(full_url=full_url, resource=resource, request=request)
        entry = entry.to_fhir()

        bundle_entries.append(entry)

    bundle = create_bundle(timestamp=dateTime, bundle_entries=bundle_entries)

    if local_output == False:
        pass
    else:
        fname = 'Bundle_patient_' + str(patient.id) + '.json'
        with open('data/' + fname, 'w') as outfile:
            json.dump(bundle.as_json(), outfile, indent=4)
        print("json written to file {fn}".format(fn=fname))

    if fhir_server_enabled == False:
        pass
    else:
        req = post(f'{fhir_server}', headers = headers, data = dumps(bundle.as_json()))
        print(req.status_code)

    i+=1
# sofa-on-fhir

Python script that generates some of the data needed to compute the SOFA-score in FHIR format

## Info
* This is a minimal standalone script to generate data needed to compute the SOFA score based on FHIR. The script will generate FHIR Bundles containing a Patient resource and additional measurements. The measurements include Observation resources for:
    * PaO2
    * FiO2
    * Bilirubin
    * Platelets
    * Creatinine
    * 24h Urine
    * Glasgow Coma Scale (GCS)

Plus there is a MedicationStatement resource for adminisration of dopamine, adrenaline and noradrenaline. There is some randomization implemented in creating the measurement values.

The SOFA-Score is based on the publication *Vincent JL, Moreno R, Takala J, et al. The SOFA (Sepsis-related Organ Failure Assessment) score to describe organ dysfunction/failure. On behalf of the Working Group on Sepsis-Related Problems of the European Society of Intensive Care Medicine. Intensive Care Med. 1996;22(7):707-710. doi:10.1007/BF01709751*

## Prerequisites
* Python >3.6
* SMART on FHIR Python client

## Usage
* Adjust the settings.yaml for your needs
    * if you are using a FHIR-server, specify the url and set to enabled
    * number of patients is the amount of data to be generated
    * all resources can be dumbed to the local data folder if enabled
* Run sofa-on-fhir.py

## License
* [MIT](https://tldrlegal.com/license/mit-license)

## Links
* [FHIR profiles from the Medical Informatics Initiative (MII)](https://simplifier.net/organization/koordinationsstellemii)
* [SMART on FHIR Python Client](http://docs.smarthealthit.org/client-py/index.html)
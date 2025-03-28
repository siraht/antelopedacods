"""
Configuration settings and constants for the application.
"""

# Provider constants
PROVIDERID = "ABC123"
PROVIDERLOCATIONID = "LOC001"

# Service code mappings
SERVICE_CODE_MAPPING = {
    "OP": "asam-1",
    "IOP": "asam-2.1"
}

# Default service level
DEFAULT_SERVICE_LEVEL = ""

# Default payer account ID
DEFAULT_PAYER_ACCOUNT_ID = ""

# Default primary clinician
DEFAULT_PRIMARY_CLINICIAN = ""

# Gender options for dropdown
GENDER_OPTIONS = {
    "Male": 1,
    "Female": 2,
    "Other": 3,
    "Unknown": 9
}

# Required client fields
REQUIRED_CLIENT_FIELDS = ["ProviderClientId", "FirstName", "LastName", "DateofBirth", "Gender", "ZipCode"]

# Field mapping dictionary for standardization
FIELD_MAPPING = {
    "unique id": "ProviderClientId",
    "uniqueid": "ProviderClientId",
    "client id": "ProviderClientId",
    "clientid": "ProviderClientId",
    "id": "ProviderClientId",
    "first name": "FirstName",
    "firstname": "FirstName",
    "first": "FirstName",
    "last name": "LastName",
    "lastname": "LastName",
    "last": "LastName",
    "client": "ClientFullName",  # New mapping for the Client field
    "date of birth": "DateofBirth",
    "dateofbirth": "DateofBirth",
    "dob": "DateofBirth",
    "birth date": "DateofBirth",
    "birthdate": "DateofBirth",
    "biological sex": "Gender",
    "gender": "Gender",
    "sex": "Gender",
    "zip": "ZipCode",
    "zipcode": "ZipCode",
    "zip code": "ZipCode",
    "postal code": "ZipCode",
    "postalcode": "ZipCode",
    # Admission date mappings
    "admission date": "AdmissionDate",
    "admissiondate": "AdmissionDate",
    "admit date": "AdmissionDate",
    "admitdate": "AdmissionDate",
    "date admitted": "AdmissionDate",
    "dateadmitted": "AdmissionDate",
    "admission for state": "AdmissionDate",
    "admissionforstate": "AdmissionDate"
}

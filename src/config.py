"""
Configuration settings and constants for the application.
"""

# Provider constants
PROVIDERID = "ABC123"
PROVIDERLOCATIONID = "LOC001"

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
    "date of birth": "DateofBirth",
    "dateofbirth": "DateofBirth",
    "dob": "DateofBirth",
    "birth date": "DateofBirth",
    "birthdate": "DateofBirth",
    "gender": "Gender",
    "sex": "Gender",
    "zip": "ZipCode",
    "zipcode": "ZipCode",
    "zip code": "ZipCode",
    "postal code": "ZipCode",
    "postalcode": "ZipCode"
}

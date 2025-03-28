"""
Configuration file for admission survey questions.
"""

# This stores all admission survey questions and their properties
ADMISSION_SURVEY_QUESTIONS = {
  "questions": [
    {
      "sequence_number": "99",
      "question_text": "First Appointment Offered",
      "field_type": "date",
      "default_value": "",
      "valid_values": None,
      "value_descriptions": None,
      "rules": None
    },
    {
      "sequence_number": "19",
      "question_text": "Days Client Waited for Treatment Entry",
      "field_type": "numeric",
      "default_value": "000",
      "valid_values": {"min": 0, "max": 999},
      "value_descriptions": None,
      "rules": None
    },
    {
      "sequence_number": "20",
      "question_text": "Interim Services Offered",
      "field_type": "select",
      "default_value": "",
      "valid_values": [""],
      "value_descriptions": {"": "Blank"},
      "rules": None
    },
    {
      "sequence_number": "21",
      "question_text": "Number of Prior Substance Abuse Treatment Episodes",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 0, "max": 998},
      "value_descriptions": None,
      "rules": None
    },
    {
      "sequence_number": "22",
      "question_text": "Number of Detox Episodes",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 0, "max": 998},
      "value_descriptions": None,
      "rules": None
    },
    {
      "sequence_number": "100",
      "question_text": "Client's Sexual Orientation",
      "field_type": "select",
      "default_value": "5",
      "valid_values": ["1", "2", "3", "4", "5"],
      "value_descriptions": {
        "1": "Heterosexual",
        "2": "Gay/Lesbian",
        "3": "Bisexual",
        "4": "Other",
        "5": "Declined"
      },
      "rules": None
    },
    {
      "sequence_number": "24",
      "question_text": "Is Client Pregnant",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "Not Pregnant",
        "1": "Pregnant"
      },
      "rules": None
    },
    {
      "sequence_number": "37",
      "question_text": "Client's Marital Status",
      "field_type": "select",
      "default_value": "1",
      "valid_values": ["1", "2", "3", "4", "5"],
      "value_descriptions": {
        "1": "Never Married",
        "2": "Married",
        "3": "Widowed",
        "4": "Separated",
        "5": "Divorced"
      },
      "rules": None
    },
    {
      "sequence_number": "38",
      "question_text": "Client's Monthly Income",
      "field_type": "numeric",
      "default_value": "0",
      "valid_values": {"min": 0, "max": 9999},
      "value_descriptions": None,
      "rules": None
    },
    {
      "sequence_number": "39",
      "question_text": "Number of Persons Living on Client's Legal Income",
      "field_type": "numeric",
      "default_value": "1",
      "valid_values": {"min": 1, "max": 99},
      "value_descriptions": None,
      "rules": None
    },
    {
      "sequence_number": "40",
      "question_text": "Number of Children Dependent on Client",
      "field_type": "numeric",
      "default_value": "0",
      "valid_values": {"min": 0, "max": 98},
      "value_descriptions": None,
      "rules": None
    },
    {
      "sequence_number": "41",
      "question_text": "Client Active in Military or Service Veteran",
      "field_type": "boolean",
      "default_value": "0",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "Not Active in Military",
        "1": "Active in Military"
      },
      "rules": None
    },
    {
      "sequence_number": "42",
      "question_text": "Client's Living Situation",
      "field_type": "select",
      "default_value": "14",
      "valid_values": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"],
      "value_descriptions": {
        "1": "Correctional facility/Jail Inpatient",
        "2": "ATU Adults Only",
        "3": "Residential Treatment/Group (Youth)",
        "4": "Foster Home (Youth)",
        "5": "Boarding home (Adult)",
        "6": "Group Home (Adult)",
        "7": "Nursing Home",
        "8": "Residential Facility (MH Adult)",
        "9": "Residential Facility (Other)",
        "10": "Sober Living",
        "11": "Homeless (no fixed address; includes shelters)",
        "12": "Supported housing",
        "13": "Assisted Living",
        "14": "Independent Living",
        "15": "Halfway House",
        "16": "Unknown"
      },
      "rules": None
    },
    {
      "sequence_number": "43",
      "question_text": "Client Disability None",
      "field_type": "boolean",
      "default_value": "1",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "Client Disabled",
        "1": "Client Not Disabled"
      },
      "rules": [
        {
          "dependencies": ["44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58"],
          "condition": "any([answers.get(dep, '0') == '1' for dep in dependencies])",
          "action": "set_value '0'"
        }
      ]
    },
    {
      "sequence_number": "44",
      "question_text": "Client's Disability Mental Retardation",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "45",
      "question_text": "Client's Disability Cerebral Palsy",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "46",
      "question_text": "Client's Disability Seizure/Epilepsy",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "47",
      "question_text": "Client's Disability Autism",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "48",
      "question_text": "Client's Disability Neurological",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "49",
      "question_text": "Client's Disability Delayed Development",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "50",
      "question_text": "Client's Disability Deaf",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "51",
      "question_text": "Client's Disability Non-verbal",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "52",
      "question_text": "Client's Disability Blind",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "53",
      "question_text": "Client's Disability Non-Ambulatory",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "54",
      "question_text": "Client's Disability Brain Injury",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "55",
      "question_text": "Client's Disability Psychiatric",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "56",
      "question_text": "Client's Disability Downs Syndrome",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "57",
      "question_text": "Client's Disability ADD",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "58",
      "question_text": "Client's Disability Other",
      "field_type": "boolean",
      "default_value": "",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "59",
      "question_text": "Requires Reasonable Accommodations",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["0", "1", "9", ""],
      "value_descriptions": {
        "0": "No",
        "1": "Yes",
        "9": "Unknown",
        "": "N/A"
      },
      "rules": [
        {
          "dependencies": ["43"],
          "condition": "answers.get('43', '0') == '1'",
          "action": "set_to_blank"
        }
      ]
    },
    {
      "sequence_number": "60",
      "question_text": "Clinic Providing Reasonable Accommodations",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["0", "1", "9", ""],
      "value_descriptions": {
        "0": "Reasonable Accommodations not provided",
        "1": "Reasonable Accommodations provided",
        "9": "Unknown",
        "": "N/A"
      },
      "rules": [
        {
          "dependencies": ["59"],
          "condition": "answers.get('59', '') == '1'",
          "action": "enable"
        },
        {
          "dependencies": ["59"],
          "condition": "answers.get('59', '') != '1'",
          "action": "set_to_blank"
        }
      ]
    },
    {
      "sequence_number": "61",
      "question_text": "Highest School Grade Completed",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "18"],
      "value_descriptions": {
        "0": "No formal education",
        "1": "1st grade",
        "2": "2nd grade",
        "3": "3rd grade",
        "4": "4th grade",
        "5": "5th grade",
        "6": "6th grade",
        "7": "7th grade",
        "8": "8th grade",
        "9": "9th grade",
        "10": "10th grade",
        "11": "11th grade",
        "12": "High School Graduate (or GED)",
        "13": "College (1st year)",
        "14": "College (2nd year)",
        "15": "College (3rd year)",
        "16": "Bachelor's Degree",
        "18": "Master's Degree"
      },
      "rules": None
    },
    {
      "sequence_number": "62",
      "question_text": "Current Employment Status",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
      "value_descriptions": {
        "1": "Employed full time (35+ hours/week)",
        "2": "Employed part time (<35 hours/week)",
        "3": "Unemployed",
        "4": "Supported employment",
        "5": "Homemaker",
        "6": "Student",
        "7": "Retired",
        "8": "Disabled",
        "9": "Inmate",
        "10": "Military",
        "11": "Volunteer"
      },
      "rules": None
    },
    {
      "sequence_number": "101",
      "question_text": "Client Attended School Within Past 3 Months",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["0", "1", "9", ""],
      "value_descriptions": {
        "0": "No",
        "1": "Yes",
        "9": "Unknown",
        "": "N/A"
      },
      "rules": None
    },
    {
      "sequence_number": "63",
      "question_text": "Primary Source of Income/Support",
      "field_type": "select",
      "default_value": "1",
      "valid_values": ["1", "2", "3", "4", "5", "6"],
      "value_descriptions": {
        "1": "Wages",
        "2": "Public assistance",
        "3": "Retirement/Pension",
        "4": "Disability",
        "5": "Other",
        "6": "None"
      },
      "rules": None
    },
    {
      "sequence_number": "64",
      "question_text": "Primary Source of Payment for Treatment Episode",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
      "value_descriptions": {
        "1": "Self pay",
        "2": "MSO funds",
        "3": "Blue Cross/Blue Shield",
        "4": "Medicare",
        "5": "Medicaid",
        "6": "Active duty military/dependent government health plan",
        "7": "Other government payment (includes TANF and/or CORE services)",
        "8": "Worker's Compensation",
        "9": "Other health insurance companies",
        "10": "No charge (free, charity, special research, teaching)",
        "11": "Other",
        "12": "Colorado ATR"
      },
      "rules": None
    },
    {
      "sequence_number": "65",
      "question_text": "Health Insurance of Client",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2"],
      "value_descriptions": {
        "1": "Client is insured",
        "2": "Client is not insured"
      },
      "rules": None
    },
    {
      "sequence_number": "66",
      "question_text": "Health Insurance Covers Substance Abuse Treatment",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["0", "1", "9", ""],
      "value_descriptions": {
        "0": "No",
        "1": "Yes",
        "9": "Unknown",
        "": "N/A"
      },
      "rules": [
        {
          "dependencies": ["65"],
          "condition": "answers.get('65', '') == '1'",
          "action": "enable"
        },
        {
          "dependencies": ["65"],
          "condition": "answers.get('65', '') != '1'",
          "action": "set_to_blank"
        }
      ]
    },
    {
      "sequence_number": "67",
      "question_text": "Current Mental Health Problem",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["0", "1", "9"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes",
        "9": "Unknown"
      },
      "rules": None
    },
    {
      "sequence_number": "102",
      "question_text": "Experienced or Witnessed Trauma Event",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["0", "1", "2"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes",
        "2": "Unable to assess"
      },
      "rules": None
    },
    {
      "sequence_number": "68",
      "question_text": "Transfer or Referral Source",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"],
      "value_descriptions": {
        "1": "Individual (self, family, friend)",
        "2": "Alcohol/drug abuse care provider",
        "3": "Other health care provider (e.g., medical, mental)",
        "4": "School (education)",
        "5": "Employer",
        "6": "Social/Human services",
        "7": "Non DUI Criminal Justice (e.g., Probation, Parole/TASC, S8-94, Community Corrections)",
        "8": "DUI/DWI Criminal Justice Involuntary commitment",
        "9": "Other Community referral",
        "10": "Drug Court",
        "11": "STIRRT",
        "12": "Crisis System",
        "13": "I MATTER (Rapid Mental Health Response for CO Youth)",
        "14": "Unknown"
      },
      "rules": None
    },
    {
      "sequence_number": "69",
      "question_text": "Family Issues and Problems",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2", "3", "4"],
      "value_descriptions": {
        "1": "None (issues are temporary and relationships generally positive)",
        "2": "Slight (some issues present; occasional friction or discord)",
        "3": "Moderate (frequent disruptions or turbulence in family functioning)",
        "4": "Severe (extensive disruption of family functioning)"
      },
      "rules": None
    },
    {
      "sequence_number": "70",
      "question_text": "Socialization Problems",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2", "3", "4"],
      "value_descriptions": {
        "1": "None (able to form good relationships with others)",
        "2": "Slight (difficulty developing or maintaining relationships)",
        "3": "Moderate (inadequate social skills resulting in tenuous and strained relationships)",
        "4": "Severe (unable to form relationships)"
      },
      "rules": None
    },
    {
      "sequence_number": "71",
      "question_text": "Education, Employment Problems",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2", "3", "4"],
      "value_descriptions": {
        "1": "None (comfortable and competent in school or at work)",
        "2": "Slight (occasional or mild disruption of performance at school or work)",
        "3": "Moderate (occasional major or frequent minor disruptions; rarely meets expectations)",
        "4": "Severe (serious incapacity, absent motivation and ineffective functioning)"
      },
      "rules": None
    },
    {
      "sequence_number": "72",
      "question_text": "Medical, Physical Problems",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2", "3", "4"],
      "value_descriptions": {
        "1": "None (no physical problems or well-controlled chronic conditions)",
        "2": "Slight (occasional or mild problems that interfere with daily living)",
        "3": "Moderate (frequent or chronic health problems)",
        "4": "Severe (incapacitated due to medical/physical problems)"
      },
      "rules": None
    },
    {
      "sequence_number": "73",
      "question_text": "Primary Drug - Drug Type",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"],
      "value_descriptions": {
        "0": "None",
        "1": "Alcohol",
        "2": "Barbiturate",
        "3": "Benzodiazepine tranquilizer",
        "4": "Clonazepam",
        "5": "Other sedative/hypnotic",
        "6": "Other tranquilizer",
        "7": "Cocaine Hydrochloride/crack",
        "8": "Methamphetamine",
        "9": "Other amphetamine",
        "10": "Other Stimulant",
        "11": "Heroin",
        "12": "Non Rx Methadone",
        "13": "Other Opiate/synthetic opiate",
        "14": "Marijuana/hashish",
        "15": "LSD",
        "16": "PCP",
        "17": "Other hallucinogens",
        "18": "Inhalant",
        "19": "Over the counter drug",
        "20": "Flunitrazepam",
        "21": "Gamma-hydroxybutyrate",
        "22": "Ketamine",
        "23": "Methylenedioxymethamphetamine (MDMA, ecstasy)",
        "24": "Anabolic Steroid",
        "25": "Other",
        "26": "Buprenorphine"
      },
      "rules": None
    },
    {
      "sequence_number": "74",
      "question_text": "Secondary Drug - Drug Type",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27"],
      "value_descriptions": {
        "0": "None",
        "1": "Alcohol",
        "2": "Barbiturate",
        "3": "Benzodiazepine tranquilizer",
        "4": "Clonazepam",
        "5": "Other sedative/hypnotic",
        "6": "Other tranquilizer",
        "7": "Cocaine Hydrochloride/crack",
        "8": "Methamphetamine",
        "9": "Other amphetamine",
        "10": "Other Stimulant",
        "11": "Heroin",
        "12": "Non Rx Methadone",
        "13": "Other Opiate/synthetic opiate",
        "14": "Marijuana/hashish",
        "15": "LSD",
        "16": "PCP",
        "17": "Other hallucinogens",
        "18": "Inhalant",
        "19": "Over the counter drug",
        "20": "Flunitrazepam",
        "21": "Gamma-hydroxybutyrate",
        "22": "Ketamine",
        "23": "Methylenedioxymethamphetamine (MDMA, ecstasy)",
        "24": "Anabolic Steroid",
        "25": "Other",
        "26": "Buprenorphine",
        "27": "Nicotine"
      },
      "rules": [
        {
          "dependencies": ["73"],
          "condition": "answers.get('73', '') == value",
          "action": "invalid"
        }
      ]
    },
    {
      "sequence_number": "75",
      "question_text": "Tertiary Drug - Drug Type",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27"],
      "value_descriptions": {
        "0": "None",
        "1": "Alcohol",
        "2": "Barbiturate",
        "3": "Benzodiazepine tranquilizer",
        "4": "Clonazepam",
        "5": "Other sedative/hypnotic",
        "6": "Other tranquilizer",
        "7": "Cocaine Hydrochloride/crack",
        "8": "Methamphetamine",
        "9": "Other amphetamine",
        "10": "Other Stimulant",
        "11": "Heroin",
        "12": "Non Rx Methadone",
        "13": "Other Opiate/synthetic opiate",
        "14": "Marijuana/hashish",
        "15": "LSD",
        "16": "PCP",
        "17": "Other hallucinogens",
        "18": "Inhalant",
        "19": "Over the counter drug",
        "20": "Flunitrazepam",
        "21": "Gamma-hydroxybutyrate",
        "22": "Ketamine",
        "23": "Methylenedioxymethamphetamine (MDMA, ecstasy)",
        "24": "Anabolic Steroid",
        "25": "Other",
        "26": "Buprenorphine",
        "27": "Nicotine"
      },
      "rules": [
        {
          "dependencies": ["74"],
          "condition": "answers.get('74', '') == ''",
          "action": "set_to_blank"
        },
        {
          "dependencies": ["73", "74"],
          "condition": "value != '' and (value == answers.get('73', '') or (value == answers.get('74', '') and answers.get('74', '') != '0'))",
          "action": "invalid"
        }
      ]
    },
    {
      "sequence_number": "76",
      "question_text": "Primary Drug - Clinician's Diagnostic Impression",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2", "3"],
      "value_descriptions": {
        "1": "Use",
        "2": "Abuse",
        "3": "Dependence"
      },
      "rules": [
        {
          "dependencies": ["74"],
          "condition": "answers.get('74', '') == ''",
          "action": "set_to_blank"
        }
      ]
    },
    {
      "sequence_number": "77",
      "question_text": "Secondary Drug - Clinician's Diagnostic Impression",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2", "3", "0", "9", ""],
      "value_descriptions": {
        "1": "Use",
        "2": "Abuse",
        "3": "Dependence",
        "0": "None",
        "9": "Unknown",
        "": "N/A"
      },
      "rules": [
        {
          "dependencies": ["74"],
          "condition": "answers.get('74', '') == ''",
          "action": "set_to_blank"
        }
      ]
    },
    {
      "sequence_number": "78",
      "question_text": "Tertiary Drug - Clinician's Diagnostic Impression",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2", "3", "0", "9", ""],
      "value_descriptions": {
        "1": "Use",
        "2": "Abuse",
        "3": "Dependence",
        "0": "None",
        "9": "Unknown",
        "": "N/A"
      },
      "rules": [
        {
          "dependencies": ["75"],
          "condition": "answers.get('75', '') == ''",
          "action": "set_to_blank"
        }
      ]
    },
    {
      "sequence_number": "79",
      "question_text": "Primary Drug - Days Used in Last 30 Days",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 0, "max": 30},
      "value_descriptions": None,
      "rules": [
        {
          "dependencies": ["73"],
          "condition": "answers.get('73', '') == ''",
          "action": "set_to_blank"
        }
      ]
    },
    {
      "sequence_number": "80",
      "question_text": "Secondary Drug - Days Used in Last 30 Days",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 0, "max": 30},
      "value_descriptions": None,
      "rules": [
        {
          "dependencies": ["74"],
          "condition": "answers.get('74', '') == ''",
          "action": "set_to_blank"
        }
      ]
    },
    {
      "sequence_number": "81",
      "question_text": "Tertiary Drug - Days Used in Last 30 Days",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 0, "max": 30},
      "value_descriptions": None,
      "rules": [
        {
          "dependencies": ["75"],
          "condition": "answers.get('75', '') == ''",
          "action": "set_to_blank"
        }
      ]
    },
    {
      "sequence_number": "82",
      "question_text": "Primary Drug - Usual Route of Administration",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2", "3", "4", "5"],
      "value_descriptions": {
        "1": "Oral",
        "2": "Smoking (pipe/cigarette)",
        "3": "Inhalation (nose/mouth)",
        "4": "Injection (IV/IM)",
        "5": "Other"
      },
      "rules": [
        {
          "dependencies": ["73"],
          "condition": "answers.get('73', '') == ''",
          "action": "set_to_blank"
        }
      ]
    },
    {
      "sequence_number": "83",
      "question_text": "Secondary Drug - Usual Route of Administration",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2", "3", "4", "5", "9", ""],
      "value_descriptions": {
        "1": "Oral",
        "2": "Smoking (pipe/cigarette)",
        "3": "Inhalation (nose/mouth)",
        "4": "Injection (IV/IM)",
        "5": "Other",
        "9": "Unknown",
        "": "N/A"
      },
      "rules": [
        {
          "dependencies": ["74"],
          "condition": "answers.get('74', '') == ''",
          "action": "set_to_blank"
        }
      ]
    },
    {
      "sequence_number": "84",
      "question_text": "Tertiary Drug - Usual Route of Administration",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2", "3", "4", "5", "9", ""],
      "value_descriptions": {
        "1": "Oral",
        "2": "Smoking (pipe/cigarette)",
        "3": "Inhalation (nose/mouth)",
        "4": "Injection (IV/IM)",
        "5": "Other",
        "9": "Unknown",
        "": "N/A"
      },
      "rules": [
        {
          "dependencies": ["75"],
          "condition": "answers.get('75', '') == ''",
          "action": "set_to_blank"
        }
      ]
    },
    {
      "sequence_number": "85",
      "question_text": "Primary Drug - Age First Used",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 1, "max": 98},
      "value_descriptions": None,
      "rules": [
        {
          "dependencies": ["73"],
          "condition": "answers.get('73', '') == ''",
          "action": "set_to_blank"
        }
      ]
    },
    {
      "sequence_number": "86",
      "question_text": "Secondary Drug - Age First Used",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 1, "max": 98},
      "value_descriptions": None,
      "rules": [
        {
          "dependencies": ["74"],
          "condition": "answers.get('74', '') == ''",
          "action": "set_to_blank"
        }
      ]
    },
    {
      "sequence_number": "87",
      "question_text": "Tertiary Drug - Age First Used",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 1, "max": 98},
      "value_descriptions": None,
      "rules": [
        {
          "dependencies": ["75"],
          "condition": "answers.get('75', '') == ''",
          "action": "set_to_blank"
        }
      ]
    },
    {
      "sequence_number": "88",
      "question_text": "Source of Illicit Drugs",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
      "value_descriptions": {
        "1": "Family",
        "2": "School",
        "3": "Friends",
        "4": "Jail/prison",
        "5": "Internet",
        "6": "Entertainment event",
        "7": "Stranger/street vendor",
        "8": "Refused",
        "9": "Unknown",
        "10": "Prescription"
      },
      "rules": None
    },
    {
      "sequence_number": "89",
      "question_text": "Visits to Medical Emergency Room",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 0, "max": 99},
      "value_descriptions": {"99": "Unknown"},
      "rules": None
    },
    {
      "sequence_number": "90",
      "question_text": "Admissions to Medical Hospital",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 0, "max": 99},
      "value_descriptions": {"99": "Unknown"},
      "rules": None
    },
    {
      "sequence_number": "91",
      "question_text": "Visits to Psychiatric Emergency Room",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 0, "max": 99},
      "value_descriptions": {"99": "Unknown"},
      "rules": None
    },
    {
      "sequence_number": "92",
      "question_text": "Admissions to Psychiatric Hospital",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 0, "max": 99},
      "value_descriptions": {"99": "Unknown"},
      "rules": None
    },
    {
      "sequence_number": "93",
      "question_text": "Number of DUI/DWI Arrests in Last 30 Days",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 0, "max": 96},
      "value_descriptions": None,
      "rules": None
    },
    {
      "sequence_number": "94",
      "question_text": "Number of Other Arrests in Last 30 Days",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 0, "max": 96},
      "value_descriptions": None,
      "rules": None
    },
    {
      "sequence_number": "95",
      "question_text": "Frequency of Self-Help Program Attendance",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 0, "max": 30},
      "value_descriptions": None,
      "rules": None
    },
    {
      "sequence_number": "96",
      "question_text": "Covered by Interstate Compact",
      "field_type": "boolean",
      "default_value": "0",
      "valid_values": ["0", "1"],
      "value_descriptions": {
        "0": "No",
        "1": "Yes"
      },
      "rules": None
    },
    {
      "sequence_number": "97",
      "question_text": "Tobacco Use Status",
      "field_type": "select",
      "default_value": "",
      "valid_values": ["1", "2", "3", "4", "5", "6"],
      "value_descriptions": {
        "1": "Current smoker/tobacco user - every day",
        "2": "Current smoker/tobacco user - periodically",
        "3": "Former smoker/tobacco user",
        "4": "Never smoker/tobacco user",
        "5": "Smoker/tobacco user - current status unknown",
        "6": "Unknown if ever smoked/used"
      },
      "rules": None
    },
    {
      "sequence_number": "98",
      "question_text": "Statutory Commitment at Admission",
      "field_type": "select",
      "default_value": "0",
      "valid_values": ["0", "1", "2"],
      "value_descriptions": {
        "0": "None (no commitment or holding procedure)",
        "1": "Emergency Commitment (detox clinics ONLY, valid only for Service Code 'asam-3.2-wm')",
        "2": "Involuntary Commitment to non-detox treatment"
      },
      "rules": None
    }
  ]
}

# Function to get a specific question by sequence number
def get_question(sequence_number):
    """
    Get question details by sequence number.
    
    Args:
        sequence_number (str): The sequence number of the question
        
    Returns:
        dict: Question details or None if not found
    """
    for question in ADMISSION_SURVEY_QUESTIONS["questions"]:
        if question["sequence_number"] == sequence_number:
            return question
    return None

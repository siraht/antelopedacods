# Workflow
1. User uploads a csv or pastes in TSV text
2. The tool ingests the data and creates a data table for all clients contained in the data
3. User selects a client to create records for and whether they want to create a Client+Admission+Admissions Survey record, or a Discharge record.
4. Tool follows workflow for either type of record
    ## Client+Admission+Admissions Survey record workflow
    1. Present the user with a text input box to paste JSON that contains the client's survey answers
    2. Check that all required fields for Client, Admission, and Survey records are present and valid
    3. Highlight all Client, Admission, and Survey record fields that are missing required information or invalid
    4. If any fields are missing required information or invalid, display an error message and allow the user to fix the issue
    5. If all fields are valid, allow the user to create the Client, Admission, and Survey records

    ## Discharge record workflow
    1. Present the user with a date field to choose the discharge date
    2. Calculate the ProviderAdmissionId using the same formula that is used for the Admission records
    3. Check that all required fields for Discharge records are present and valid
    4. Highlight all Discharge record fields that are missing required information or invalid
    5. If any fields are missing required information or invalid, display an error message and allow the user to fix the issue
    6. If all fields are valid, allow the user to create the Discharge record
5. Allow as many records to be created as the user wants
6. Export the data into multiple csv files when the user is finished



# Client records
Client records contain the following fields. If there is a value in Static Value then that is the value that should always be output for the field. Variable Value and Rules are used to determine the value of the field.
"Field Name","Static Value","Variable Value","Rules"
"RecordType","Client","","always output Client"
"ProviderId","","","pull PROVIDERID from config"
"ProviderClientId","","Client's Unique ID","output client's Unique ID"
"SocialSecurityNumber","000000000","","always output 9 zeros"
"DateofBirth","","","output DOB as MM/DD/YYYY"
"Gender","","1=M,2=F","1 for Male, 2 for Female","",""
"LastName","","","Output last name"
"FirstName","","","Output first name"
"MiddleName","","","optional, output nothing unless value provided",""
"Address1","","","optional, output nothing unless value provided",""
"Address2","","","optional, output nothing unless value provided",""
"City","","","output the city the client lives in"
"CountyID","","xx","output 0 if homeless, 99 if unknown, otherwise use county code from County Codes list","",""
"StateID","CO","","always output CO"
"ZipCode","","xxxxx0000","output the 5 digit zip code with four 0s appended to the end, leave blank if homeless",""
"PhoneNumber","","","leave blank"
"MedicaidID","","","output the Medicaid ID if a client has Medicaid"
"OutofStateFlag","0","","always 0 for in state"
"ClientisHomelessFlag","","0=No,1=Yes","1 if homeless, 0 if not","",""
"RaceWhite","","0=No,1=Yes",""
"RaceBlack","","0=No,1=Yes",""
"RaceAmericanIndianAlaskanNative","","0=No,1=Yes",""
"RaceAsian","","0=No,1=Yes",""
"RaceNativeHawaiianPacificIslander","","0=No,1=Yes",""
"RaceDeclined","","0=No,1=Yes","output 1 if none of RaceWhite,RaceBlack,RaceAmericanIndianAlaskanNative,RaceAsian,RaceNativeHawaiianPacificIslander are 1, output 0 if any of them are 0"
"Ethnicity","","0=Not Hispanic,1=Hispanic/Mexican,2=Hispanic/Puerto Rican,3=Hispanic/Cuban,4=Other Hispanic,5=Declined"

# Admission records
Admission records need to contain the following fields. If there is a value in Static Value then that is the value that should always be output for the field. Variable Value and Rules are used to determine the value of the field.
"Field Name","Static Value","Variable Value","Rules"
"RecordType","Admission","","always output ""Admission"""
"ProviderId","","","pull PROVIDERID from config"
"ProviderClientId","","","output client's Unique ID"
"ProviderAdmissionId","","","generate a unique alphanumeric ID using client name and admission date that is no longer than 15 characters"
"ProviderLocationId","","","output PROVIDERLOCATIONID from config"
"ServiceCode","","asam-1=OP,asam-2.1=IOP","output asam-1 for OP level care and asam-2.1 for IOP level care"
"DefaultPayerAccountID","","","output the default payer using the payer account list"
"ReferralNumber","","","leave blank"
"AdmissionDate","","","Output admission date in MM/DD/YYYY format"
"PrimaryClinicianName","","","output name of Primary Clinician"
"FirstContactDate","","","Output date of first contact in MM/DD/YYYY format"

# Discharge records
Discharge records need to contain the following fields. If there is a value in Static Value then that is the value that should always be output for the field. Variable Value and Rules are used to determine the value of the field.
"Field Name","Static Value","Variable Value","Rules"
"RecordType","Discharge","","always output ""Discharge"""
"ProviderId","","","pull PROVIDERID from config"
"ProviderClientID","","","output client's Unique ID"
"ProviderAdmissionId","","output the ProviderAdmissionId for this client's Admission record"
"DischargeDate","","output date of discharge in MM/DD/YYYY format"

# Survey records
Survey records are different than any other record in that there are multiple rows per survey, one for each question. If there is a value in Static Value, that is the value that should always be output for the field. Rules are used to determine the value of the field.
"Field Name","Static Value","Rules"
"RecordType","SurAns",
"ProviderId","PROVIDERID","pull PROVIDERID from config"
"ProviderAdmissionId","","output the ProviderAdmissionId for this client's Admission record"
"QuestionGroupId","","Output 1 if for an Admission, 2 if for a Discharge"
"ExportSequenceNumber","","output the number of the question"
"AnswerValue","","output the answer value for the question"

# Sample client TSV that would be pasted into tool
Key,Client,Phone,Email,Parents,Parent Emails,Parent Involvement,Unique ID,Parent IDs,Status,Note,Unique BIlling,DOB,Demographics,Primary Clinician,Clinical Team Members,Lead Creation Date,Discharge Date,Grade in school,Biological Sex,Address,Address Line 2,denver,State,Zip,Race,Hispanic,Race for reporting,Related Lead,Related Lead - Text,CCAR Required,First Half CCAR Admission,Second Half CCAR Admission,Admissions CCAR Fixed Width,CCAR Discharge,DACODS Required,DACODS Admission,DACODS DIscharge,Expected Peer Mentor per week,Expected Individual Therapy per week,Expected Parent Coaching and Family Therapy per week,Expected Parent Group per week,Expected Teen Group per week,Total Expected per week,Parent of,Parent of - text,Referred By,Referred By - Text,Referred By Org,Referred By Org - Text,Referred By - Last Modified,Generate PDF
20250113184120-155,First Last,5055555555,test@protonmail.com,George,test@protonmail.com,Involved,4324322,,Active,,,03/27/2007,,Cathy Trejos,,,,,Female,111 Hello Ave,,Littleton,CO,80120-3410,Decline to answer,Decline to answer,Decline to answer,,,TRUE,02/06/2025,02/25/2025,,,,,,,1,,,,,,,,,children's,children's,,

# TSV/CSV field to output record field mapping
Output fields are the fields that will be output in the final csv files. Input fields are the fields that will be inputted using CSV or TSV.
Output Fields,Input Fields
RecordType,
ProviderId,
ProviderClientId,Unique ID
SocialSecurityNumber,
DateofBirth,DOB
Gender,Biological Sex
LastName,Client
FirstName,Client
MiddleName,
Address1,
Address2,
City,City
CountyID,
StateID,
ZipCode,Zip
PhoneNumber,
MedicaidID,
OutofStateFlag,
ClientisHomelessFlag,
RaceWhite,
RaceBlack,
RaceAmericanIndianAlaskanNative,
RaceAsian,
RaceNativeHawaiianPacificIslander,
RaceDeclined,Race for reporting
Ethnicity,
ProviderAdmissionId,
ProviderLocationId,
ServiceCode,
DefaultPayerAccountID,
ReferralNumber,
AdmissionDate,
PrimaryClinicianName,Primary Clinician
FirstContactDate,Lead Creation Date
DischargeDate,Discharge Date
QuestionGroupId,
ExportSequenceNumber,
AnswerValue,

# Admissions survey questions
The Sequence Number is the key of the question, with Question as the label. Rules defines what values are valid or invalid based on other survery question's answer. Default Value is what should be output if there is not a provided answer from the data. Answer / Valid Responses defines valid values for that field. Value descriptions are the descriptions for the valid values, to be used in the dropdowns.
"Sequence Number","Rules","Question","Default Value","Answer / Valid Responses","Value descriptions"
" 99 ","","First Appointment Offered","","MM/DD/YYYY",""
" 19 ","","Days Client Waited for Treatment Entry","000","000",""
" 20 ","","Interim Services Offered","","Blank",""
" 21 ","","Number of Prior Substance Abuse Treatment Episodes","","Value 000-998",""
" 22 ","","Number of Detox Episodes","","Value 000-998",""
" 100 ","","Client's Sexual Orientation","5","Value 1 2 3 4 5"," '1' for Heterosexual, '2' for Gay/Lesbian, '3' for Bisexual, '4' for Other, '5' for Declined. "
" 24 ","","Is Client Pregnant",""," Value 0 1 ","1 for Pregnant, 0 for Not Pregnant"
" 37 ","","Client's Marital Status","1","Value 1 2 3 4 5"," '1' for Never Married, '2' for Married, '3' for Widowed, '4' for Separated, '5' for Divorced."
" 38 ","","Client's Monthly Income","0","Value 0000-9999",""
" 39 ","","Number of Persons Living on Client's Legal Income","1"," Value 1 to 99 ",""
" 40 ","","Number of Children Dependent on Client","0"," Value 0 to 98 ",""
" 41 ","","Client Active in Military or Service Veteran","0"," Value 0 1 ","0 for not active in military, 1 for active in military"
" 42 ","","Client's Living Situation","14"," Value 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ","' 1' for Correctional facility/Jail Inpatient, '2' for ATU Adults Only, '3' for Residential Treatment/Group (Youth), '4' for Foster Home (Youth), '5' for Boarding home (Adult), '6' for Group Home (Adult), '7' for Nursing Home, '8' for Residential Facility (MH Adult), '9' for Residential Facility (Other), '10' for Sober Living, '11' for Homeless (no fixed address; includes shelters), '12' for Supported housing, '13' for Assisted Living, '14' for Independent Living, '15' for Halfway House. If the client’s address is homeless, output '11'"
" 43 ","Must be 0 if any of 44-58 are 1","Client Disability None","1"," Value 0 1 ","1 is Client Not Disabled, 0 is Client Disabled"
" 44 ","","Client's Disability Mental Retardation",""," Value 0 1 ","0 is No, 1 is Yes"
" 45 ","","Client's Disability Cerebral Palsy",""," Value 0 1 ","0 is No, 1 is Yes"
" 46 ","","Client's Disability Seizure/Epilepsy",""," Value 0 1 ","0 is No, 1 is Yes"
" 47 ","","Client's Disability Autism",""," Value 0 1 ","0 is No, 1 is Yes"
" 48 ","","Client's Disability Neurological",""," Value 0 1 ","0 is No, 1 is Yes"
" 49 ","","Client's Disability Delayed Development",""," Value 0 1 ","0 is No, 1 is Yes"
" 50 ","","Client's Disability Deaf",""," Value 0 1 ","0 is No, 1 is Yes"
" 51 ","","Client's Disability Non-verbal",""," Value 0 1 ","0 is No, 1 is Yes"
" 52 ","","Client's Disability Blind",""," Value 0 1 ","0 is No, 1 is Yes"
" 53 ","","Client's Disability Non-Ambulatory",""," Value 0 1 ","0 is No, 1 is Yes"
" 54 ","","Client's Disability Brain Injury",""," Value 0 1 ","0 is No, 1 is Yes"
" 55 ","","Client's Disability Psychiatric",""," Value 0 1 ","0 is No, 1 is Yes"
" 56 ","","Client's Disability Downs Syndrome",""," Value 0 1 ","0 is No, 1 is Yes"
" 57 ","","Client's Disability ADD",""," Value 0 1 ","0 is No, 1 is Yes"
" 58 ","","Client's Disability Other",""," Value 0 1 ","0 is No, 1 is Yes"
" 59 ","If 43=1 then leave blank, otherwise output 0 or 1","Requires Reasonable Accommodations",""," Value 0 1 9 Blank ","0 is No, 1 is Yes, Blank is N/A"
" 60 "," If 59=1 then must be 0 or 1, if 59 does not equal 1 then must be blank ","Clinic Providing Reasonable Accommodations",""," Value 0 1 9 Blank ","1=Reasonable Accomodations provided, 0=Reasonable Accomodations not provided, Blank = N/A"
" 61 ","","Highest School Grade Completed",""," Value 0 1-11 12 13 - 15 16 18 ","' 0' for No formal education, '1' to '11' for 1st through 11th grade, '12' for High School Graduate (or GED), '13' to '15' for College, '16' for Bachelor's Degree, '18' for Master's Degree."
" 62 ","","Current Employment Status",""," Value 1 2 3 4 5 6 7 8 9 10 11 ","' 1' for Employed full time (35+ hours/week), '2' for Employed part time (<35 hours/week), '3' for Unemployed, '4' for Supported employment, '5' for Homemaker, '6' for Student, '7' for Retired, '8' for Disabled, '9' for Inmate, '10' for Military, '11' for Volunteer."
" 101 ","","Client Attended School Within Past 3 Months",""," Value 0 1 9 Blank ","0 is No, 1 is Yes"
" 63 ","","Primary Source of Income/Support","1"," Value 1 2 3 4 5 6","'1' for Wages, '2' for Public assistance, '3' for Retirement/Pension, '4' for Disability, '5' for Other, '6' for None,"
" 64 "," If 5, Client must have a MedicaidID, Colorado ATR (12) is only valid if Admission ServiceCode = asam-1","Primary Source of Payment for Treatment Episode",""," Value 1 2 3 4 5 6 7 8 9 10 11 12 ","' 1' for Self pay, '2' for MSO funds, '3' for Blue Cross/Blue Shield, '4' for Medicare, '5' for Medicaid, '6' for Active duty military/dependent government health plan, '7' for Other government payment (includes TANF and/or CORE services), '8' for Worker's Compensation, '9' for Other health insurance companies, '10' for No charge (free, charity, special research, teaching), '11' for Other, '12' for Colorado ATR "
" 65 ","","Health Insurance of Client",""," Value 1 2","'1' for Client is insured, '2' for Client is not insured"
" 66 ","If 65=1 then must be 0, 1, if 65 is not 1 then must be blank","Health Insurance Covers Substance Abuse Treatment",""," Value 0 1 9 Blank ","0 is No, 1 is Yes, Blank is N/A"
" 67 ","","Current Mental Health Problem",""," Value 0 1 9 "," '0' for No, '1' for Yes, '9' for Unknown"
" 102 ","","Experienced or Witnessed Trauma Event",""," Value 0 1 2 ","'0' for No, '1' for Yes, '2' for Unable to assess"
" 68 ","","Transfer or Referral Source",""," Value 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ","' 1' for Individual (self, family, friend), '2' for Alcohol/drug abuse care provider, '3' for Other health care provider (e.g., medical, mental), '4' for School (education), '5' for Employer, '6' for Social/Human services, '7' for Non DUI Criminal Justice (e.g., Probation, Parole/TASC, S8-94, Community Corrections), '8' for DUI/DWI Criminal Justice Involuntary commitment, '9' for Other Community referral, '10' for Drug Court, '11' for STIRRT, '12' for Crisis System, '13' for I MATTER (Rapid Mental Health Response for CO Youth)"
" 69 ","","Family Issues and Problems",""," Value 1 2 3 4","'1' for None (issues are temporary and relationships generally positive), '2' for Slight (some issues present; occasional friction or discord), '3' for Moderate (frequent disruptions or turbulence in family functioning), '4' for Severe (extensive disruption of family functioning)"
" 70 ","","Socialization Problems",""," Value 1 2 3 4","'1' for None (able to form good relationships with others), '2' for Slight (difficulty developing or maintaining relationships), '3' for Moderate (inadequate social skills resulting in tenuous and strained relationships), '4' for Severe (unable to form relationships)"
" 71 ","","Education, Employment Problems",""," Value 1 2 3 4","'1' for None (comfortable and competent in school or at work), '2' for Slight (occasional or mild disruption of performance at school or work), '3' for Moderate (occasional major or frequent minor disruptions; rarely meets expectations), '4' for Severe (serious incapacity, absent motivation and ineffective functioning),"
" 72 ","","Medical, Physical Problems",""," Value 1 2 3 4"," '1' for None (no physical problems or well-controlled chronic conditions), '2' for Slight (occasional or mild problems that interfere with daily living), '3' for Moderate (frequent or chronic health problems), '4' for Severe (incapacitated due to medical/physical problems)"
" 73 ","","Primary Drug - Drug Type",""," Value 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ","' 0' for None, '1' for Alcohol, '2' for Barbiturate, '3' for Benzodiazepine tranquilizer, '4' for Clonazepam, '5' for Other sedative/hypnotic, '6' for Other tranquilizer, '7' for Cocaine Hydrochloride/crack, '8' for Methamphetamine, '9' for Other amphetamine, '10' for Other Stimulant, '11' for Heroin, '12' for Non Rx Methadone, '13' for Other Opiate/synthetic opiate, '14' for Marijuana/hashish, '15' for LSD, '16' for PCP, '17' for Other hallucinogens, '18' for Inhalant, '19' for Over the counter drug, '20' for Flunitrazepam, '21' for Gamma-hydroxybutyrate, '22' for Ketamine, '23' for Methylenedioxymethamphetamine (MDMA, ecstasy), '24' for Anabolic Steroid, '25' for Other, '26' for Buprenorphine"
" 74 ","Cannot equal value of 73","Secondary Drug - Drug Type",""," Value 0 1-27 ","' 0' for None, '1' for Alcohol, '2' for Barbiturate, '3' for Benzodiazepine tranquilizer, '4' for Clonazepam, '5' for Other sedative/hypnotic, '6' for Other tranquilizer, '7' for Cocaine Hydrochloride/crack, '8' for Methamphetamine, '9' for Other amphetamine, '10' for Other Stimulant, '11' for Heroin, '12' for Non Rx Methadone, '13' for Other Opiate/synthetic opiate, '14' for Marijuana/hashish, '15' for LSD, '16' for PCP, '17' for Other hallucinogens, '18' for Inhalant, '19' for Over the counter drug, '20' for Flunitrazepam, '21' for Gamma-hydroxybutyrate, '22' for Ketamine, '23' for Methylenedioxymethamphetamine (MDMA, ecstasy), '24' for Anabolic Steroid, '25' for Other, '26' for Buprenorphine., '27' for Nicotine"
" 75 ","When 74 is blank, must be blank. If 75 is not blank, must not equal 73 or 74","Tertiary Drug - Drug Type",""," Value 0 1-27 ","' 0' for None, '1' for Alcohol, '2' for Barbiturate, '3' for Benzodiazepine tranquilizer, '4' for Clonazepam, '5' for Other sedative/hypnotic, '6' for Other tranquilizer, '7' for Cocaine Hydrochloride/crack, '8' for Methamphetamine, '9' for Other amphetamine, '10' for Other Stimulant, '11' for Heroin, '12' for Non Rx Methadone, '13' for Other Opiate/synthetic opiate, '14' for Marijuana/hashish, '15' for LSD, '16' for PCP, '17' for Other hallucinogens, '18' for Inhalant, '19' for Over the counter drug, '20' for Flunitrazepam, '21' for Gamma-hydroxybutyrate, '22' for Ketamine, '23' for Methylenedioxymethamphetamine (MDMA, ecstasy), '24' for Anabolic Steroid, '25' for Other, '26' for Buprenorphine., '27' for Nicotine"
" 76 ","When 74 is blank, must be blank. If 74 is not blank, must be 1-3","Primary Drug - Clinician's Diagnostic Impression",""," Value 1 2 3","'1' for Use, '2' for Abuse, '3' for Dependence"
" 77 ","When 74 is blank, must be blank. If 74 is not blank, must be 1-3","Secondary Drug - Clinician's Diagnostic Impression",""," Value 1 2 3 0 9 Blank ","'1' for Use, '2' for Abuse, '3' for Dependence, Blank for N/A"
" 78 ","When 75 is blank, must be blank. If 75 is not blank, must be 1-3","Tertiary Drug - Clinician's Diagnostic Impression",""," Value 1 2 3 0 9 Blank ","'1' for Use, '2' for Abuse, '3' for Dependence, Blank for N/A"
" 79 ","If 73 is blank, must be blank. If 73 is not blank, must be 0-30","Primary Drug - Days Used in Last 30 Days",""," Value 0 to 30",""
" 80 ","If 74 is blank, must be blank. If 74 is not blank, must be 0-30","Secondary Drug - Days Used in Last 30 Days",""," Value 0 to 30 Blank ",""
" 81 ","If 75 is blank, must be blank. If 75 is not blank, must be 0-30","Tertiary Drug - Days Used in Last 30 Days",""," Value 0 to 30 Blank ",""
" 82 ","If 73 is blank, must be blank","Primary Drug - Usual Route of Administration",""," Value 1 2 3 4 5","'1' for Oral, '2' for Smoking (pipe/cigarette), '3' for Inhalation (nose/mouth), '4' for Injection (IV/IM), '5' for Other"
" 83 ","If 74 is blank, must be blank","Secondary Drug - Usual Route of Administration",""," Value 1 2 3 4 5 9 Blank ","'1' for Oral, '2' for Smoking (pipe/cigarette), '3' for Inhalation (nose/mouth), '4' for Injection (IV/IM), '5' for Other"
" 84 ","If 75 is blank, must be blank","Tertiary Drug - Usual Route of Administration",""," Value 1 2 3 4 5 9 Blank ","'1' for Oral, '2' for Smoking (pipe/cigarette), '3' for Inhalation (nose/mouth), '4' for Injection (IV/IM), '5' for Other"
" 85 ","Must not be greater than client's age, ","Primary Drug - Age First Used",""," Value 1 to 98",""
" 86 ","Must not be greater than client's age, blank when 74 is blank","Secondary Drug - Age First Used",""," Value 1 to 98 Blank ","Blank for N/A"
" 87 ","Must not be greater than client's age, blank when 75 is blank","Tertiary Drug - Age First Used",""," Value 1 to 98 Blank ","Blank for N/A"
" 88 ","","Source of Illicit Drugs",""," Value 1 2 3 4 5 6 7 8 9 10","' 1' for Family, '2' for School, '3' for Friends, '4' for Jail/prison, '5' for Internet, '6' for Entertainment event, '7' for Stranger/street vendor, '8' for Refused, '9' for Unknown, '10' for Prescription."
" 89 ","","Visits to Medical Emergency Room",""," Value 0 to 98 99 ","'99' for Unknown"
" 90 ","","Admissions to Medical Hospital",""," Value 0 to 98 99 ","'99' for Unknown"
" 91 ","","Visits to Psychiatric Emergency Room",""," Value 0 to 98 99 ","'99' for Unknown"
" 92 ","","Admissions to Psychiatric Hospital",""," Value 0 to 98 99 ","'99' for Unknown"
" 93 ","","Number of DUI/DWI Arrests in Last 30 Days",""," Value 0 to 96 ",""
" 94 ","","Number of Other Arrests in Last 30 Days",""," Value 0 to 96 ",""
" 95 ","","Frequency of Self-Help Program Attendance",""," Value 0 to 30 ",""
" 96 ","","Covered by Interstate Compact","0"," Value 0 1","0 is No, 1 is Yes"
" 97 ","","Tobacco Use Status",""," Value 1 2 3 4 5 6 ","'1' for Current smoker/tobacco user - every day, '2' for Current smoker/tobacco user - periodically, '3' for Former smoker/tobacco user, '4' for Never smoker/tobacco user, '5' for Smoker/tobacco user - current status unknown, '6' for Unknown if ever smoked/used"
" 98 ","","Statutory Commitment at Admission","0"," Value 0 2 ","'0' for None (no commitment or holding procedure), '1' for Emergency Commitment (detox clinics ONLY, valid only for Service Code 'asam-3.2-wm'), '2' for Involuntary Commitment to non-detox treatment "

# County Codes list
County Code,County Name
0,Homeless
1,Adams
2,Alamosa
3,Arapahoe
4,Archuleta
5,Baca
6,Bent
7,Boulder
8,Broomfield
9,Chaffee
10,Cheyenne
11,Clear Creek
12,Conejos
13,Costilla
14,Crowley
15,Custer
16,Delta
17,Denver
18,Dolores
19,Douglas
20,Eagle
21,El Paso
22,Elbert
23,Fremont
24,Garfiel
25,Gilpin
26,Grand
27,Gunnison
28,Hinsdale
29,Huerfano
30,Jackson
31,Jefferson
32,Kiowa
33,Kit Carson
34,La Plata
35,Lake
36,Larimer
37,Las Animas
38,Lincoln
39,Logan
40,Mesa
41,Mineral
42,Moffat
43,Montezuma
44,Montrose
45,Morgan
46,Otero
47,Ouray
48,Park
49,Phillips
50,Pitkin
51,Prowers
52,Pueblo
53,Rio Blanco
54,Rio Grande
55,Routt
56,Saguache
57,San Juan
58,San Miguel
59,Sedgwick
60,Summit
61,Teller
62,Washington
63,Weld
64,Yuma
77,Out of State
88,Refused
99,Unknown


# Zip codes and counties list
8,Colorado,CO,80002,Jefferson,Arvada
8,Colorado,CO,80003,Jefferson,Arvada
8,Colorado,CO,80004,Jefferson,Arvada
8,Colorado,CO,80005,Jefferson,Arvada
8,Colorado,CO,80007,Jefferson,Zcta 80007
8,Colorado,CO,80010,Adams,Aurora
8,Colorado,CO,80011,Arapahoe,Aurora
8,Colorado,CO,80012,Arapahoe,Aurora
8,Colorado,CO,80013,Arapahoe,Aurora
8,Colorado,CO,80014,Arapahoe,Aurora
8,Colorado,CO,80015,Arapahoe,Aurora
8,Colorado,CO,80016,Arapahoe,Aurora
8,Colorado,CO,80017,Arapahoe,Aurora
8,Colorado,CO,80018,Arapahoe,Aurora
8,Colorado,CO,80019,Adams,Aurora
8,Colorado,CO,80020,Boulder,Broomfield
8,Colorado,CO,80021,Jefferson,Westminster
8,Colorado,CO,80022,Adams,Commerce city
8,Colorado,CO,80024,Adams,Dupont
8,Colorado,CO,80025,Boulder,Eldorado springs
8,Colorado,CO,80026,Boulder,Lafayette
8,Colorado,CO,80027,Boulder,Louisville
8,Colorado,CO,80030,Adams,Westminster
8,Colorado,CO,80031,Adams,Westminster
8,Colorado,CO,80033,Jefferson,Wheat ridge
8,Colorado,CO,800HH,Arapahoe,Zcta 800hh
8,Colorado,CO,800XX,Adams,Zcta 800xx
8,Colorado,CO,80101,Elbert,Agate
8,Colorado,CO,80102,Adams,Bennett
8,Colorado,CO,80103,Arapahoe,Byers
8,Colorado,CO,80104,Douglas,Castle rock
8,Colorado,CO,80105,Arapahoe,Deer trail
8,Colorado,CO,80106,El Paso,Elbert
8,Colorado,CO,80107,Elbert,Elizabeth
8,Colorado,CO,80110,Arapahoe,Cherry hills vil
8,Colorado,CO,80111,Arapahoe,Cherry hills vil
8,Colorado,CO,80112,Arapahoe,Englewood
8,Colorado,CO,80116,Douglas,Franktown
8,Colorado,CO,80117,Elbert,Kiowa
8,Colorado,CO,80118,Douglas,Larkspur
8,Colorado,CO,80120,Arapahoe,Littleton
8,Colorado,CO,80121,Arapahoe,Greenwood villag
8,Colorado,CO,80122,Arapahoe,Littleton
8,Colorado,CO,80123,Jefferson,Bow mar
8,Colorado,CO,80124,Douglas,Littleton
8,Colorado,CO,80125,Douglas,Littleton
8,Colorado,CO,80126,Douglas,Highlands ranch
8,Colorado,CO,80127,Jefferson,Littleton
8,Colorado,CO,80128,Jefferson,Zcta 80128
8,Colorado,CO,80132,El Paso,Monument
8,Colorado,CO,80133,El Paso,Palmer lake
8,Colorado,CO,80134,Douglas,Parker
8,Colorado,CO,80135,Douglas,Deckers
8,Colorado,CO,80136,Adams,Strasburg
8,Colorado,CO,80137,Adams,Watkins
8,Colorado,CO,80138,Douglas,Zcta 80138
8,Colorado,CO,801XX,Arapahoe,Zcta 801xx
8,Colorado,CO,80202,Denver,Denver
8,Colorado,CO,80203,Denver,Denver
8,Colorado,CO,80204,Denver,Denver
8,Colorado,CO,80205,Denver,Denver
8,Colorado,CO,80206,Denver,Denver
8,Colorado,CO,80207,Denver,Denver
8,Colorado,CO,80209,Denver,Denver
8,Colorado,CO,80210,Denver,Denver
8,Colorado,CO,80211,Denver,Denver
8,Colorado,CO,80212,Denver,Mountain view
8,Colorado,CO,80214,Jefferson,Edgewater
8,Colorado,CO,80215,Jefferson,Lakewood
8,Colorado,CO,80216,Denver,Denver
8,Colorado,CO,80218,Denver,Denver
8,Colorado,CO,80219,Denver,Denver
8,Colorado,CO,80220,Denver,Denver
8,Colorado,CO,80221,Adams,Federal heights
8,Colorado,CO,80222,Denver,Glendale
8,Colorado,CO,80223,Denver,Denver
8,Colorado,CO,80224,Denver,Denver
8,Colorado,CO,80226,Jefferson,Lakewood
8,Colorado,CO,80227,Jefferson,Denver
8,Colorado,CO,80228,Jefferson,Lakewood
8,Colorado,CO,80229,Adams,Thornton
8,Colorado,CO,80230,Denver,Lowry afb
8,Colorado,CO,80231,Denver,Denver
8,Colorado,CO,80232,Jefferson,Lakewood
8,Colorado,CO,80233,Adams,Northglenn
8,Colorado,CO,80234,Adams,Northglenn
8,Colorado,CO,80235,Jefferson,Denver
8,Colorado,CO,80236,Denver,Denver
8,Colorado,CO,80237,Denver,Denver
8,Colorado,CO,80239,Denver,Denver
8,Colorado,CO,80241,Adams,Northglenn
8,Colorado,CO,80246,Denver,Zcta 80246
8,Colorado,CO,80249,Denver,Denver
8,Colorado,CO,80260,Adams,Zcta 80260
8,Colorado,CO,80264,Denver,Lincoln center b
8,Colorado,CO,80290,Denver,Two united bank
8,Colorado,CO,80293,Denver,First interstate
8,Colorado,CO,80294,Denver,Denver
8,Colorado,CO,80301,Boulder,Boulder
8,Colorado,CO,80302,Boulder,Boulder
8,Colorado,CO,80303,Boulder,Boulder
8,Colorado,CO,80304,Boulder,Boulder
8,Colorado,CO,80401,Jefferson,Golden
8,Colorado,CO,80403,Jefferson,Golden
8,Colorado,CO,80420,Park,Alma
8,Colorado,CO,80421,Park,Bailey
8,Colorado,CO,80422,Gilpin,Black hawk
8,Colorado,CO,80423,Eagle,Bond
8,Colorado,CO,80424,Summit,Breckenridge
8,Colorado,CO,80425,Jefferson,Buffalo creek
8,Colorado,CO,80426,Eagle,Burns
8,Colorado,CO,80427,Gilpin,Central city
8,Colorado,CO,80428,Routt,Clark
8,Colorado,CO,80430,Jackson,Coalmont
8,Colorado,CO,80432,Park,Como
8,Colorado,CO,80433,Jefferson,Conifer
8,Colorado,CO,80434,Jackson,Cowdrey
8,Colorado,CO,80435,Summit,Keystone
8,Colorado,CO,80436,Clear Creek,Dumont
8,Colorado,CO,80438,Clear Creek,Empire
8,Colorado,CO,80439,Jefferson,Evergreen
8,Colorado,CO,80440,Park,Fairplay
8,Colorado,CO,80442,Grand,Fraser
8,Colorado,CO,80443,Summit,Copper mountain
8,Colorado,CO,80444,Clear Creek,Georgetown
8,Colorado,CO,80446,Grand,Granby
8,Colorado,CO,80447,Grand,Grand lake
8,Colorado,CO,80448,Park,Grant
8,Colorado,CO,80449,Park,Hartsel
8,Colorado,CO,80451,Grand,Hot sulphur spri
8,Colorado,CO,80452,Clear Creek,Idaho springs
8,Colorado,CO,80454,Jefferson,Indian hills
8,Colorado,CO,80455,Boulder,Jamestown
8,Colorado,CO,80456,Park,Jefferson
8,Colorado,CO,80457,Jefferson,Kittredge
8,Colorado,CO,80459,Grand,Kremmling
8,Colorado,CO,80461,Lake,Leadville
8,Colorado,CO,80463,Eagle,Mc coy
8,Colorado,CO,80465,Jefferson,Morrison
8,Colorado,CO,80466,Boulder,Nederland
8,Colorado,CO,80467,Routt,Oak creek
8,Colorado,CO,80468,Grand,Parshall
8,Colorado,CO,80469,Routt,Phippsburg
8,Colorado,CO,80470,Jefferson,Pine
8,Colorado,CO,80473,Jackson,Rand
8,Colorado,CO,80474,Gilpin,Rollinsville
8,Colorado,CO,80476,Clear Creek,Silver plume
8,Colorado,CO,80478,Grand,Tabernash
8,Colorado,CO,80479,Routt,Toponas
8,Colorado,CO,80480,Jackson,Walden
8,Colorado,CO,80481,Boulder,Ward
8,Colorado,CO,80482,Grand,Winter park
8,Colorado,CO,80483,Routt,Yampa
8,Colorado,CO,80487,Routt,Steamboat spring
8,Colorado,CO,80498,Summit,Silverthorne
8,Colorado,CO,804HH,Grand,Zcta 804hh
8,Colorado,CO,804XX,Grand,Zcta 804xx
8,Colorado,CO,80501,Boulder,Longmont
8,Colorado,CO,80503,Boulder,Longmont
8,Colorado,CO,80504,Weld,Longmont
8,Colorado,CO,80510,Boulder,Allenspark
8,Colorado,CO,80512,Larimer,Bellvue
8,Colorado,CO,80513,Larimer,Berthoud
8,Colorado,CO,80514,Weld,Dacono
8,Colorado,CO,80515,Larimer,Drake
8,Colorado,CO,80516,Boulder,Erie
8,Colorado,CO,80517,Larimer,Estes park
8,Colorado,CO,80520,Weld,Firestone
8,Colorado,CO,80521,Larimer,Fort collins
8,Colorado,CO,80524,Larimer,Fort collins
8,Colorado,CO,80525,Larimer,Fort collins
8,Colorado,CO,80526,Larimer,Fort collins
8,Colorado,CO,80528,Larimer,Zcta 80528
8,Colorado,CO,80530,Weld,Frederick
8,Colorado,CO,80532,Larimer,Glen haven
8,Colorado,CO,80534,Weld,Johnstown
8,Colorado,CO,80535,Larimer,Laporte
8,Colorado,CO,80536,Larimer,Virginia dale
8,Colorado,CO,80537,Larimer,Loveland
8,Colorado,CO,80538,Larimer,Loveland
8,Colorado,CO,80540,Boulder,Lyons
8,Colorado,CO,80542,Weld,Mead
8,Colorado,CO,80543,Weld,Milliken
8,Colorado,CO,80545,Larimer,Red feather lake
8,Colorado,CO,80547,Larimer,Timnath
8,Colorado,CO,80549,Larimer,Wellington
8,Colorado,CO,80550,Weld,Windsor
8,Colorado,CO,80601,Adams,Lochbui
8,Colorado,CO,80610,Weld,Ault
8,Colorado,CO,80611,Weld,Briggsdale
8,Colorado,CO,80612,Weld,Carr
8,Colorado,CO,80615,Weld,Eaton
8,Colorado,CO,80620,Weld,Evans
8,Colorado,CO,80621,Weld,Wattenburg
8,Colorado,CO,80623,Weld,Gilcrest
8,Colorado,CO,80624,Weld,Gill
8,Colorado,CO,80631,Weld,Garden city
8,Colorado,CO,80634,Weld,Greeley
8,Colorado,CO,80640,Adams,Henderson
8,Colorado,CO,80642,Weld,Hudson
8,Colorado,CO,80643,Weld,Keenesburg
8,Colorado,CO,80644,Weld,Kersey
8,Colorado,CO,80645,Weld,La salle
8,Colorado,CO,80648,Weld,Nunn
8,Colorado,CO,80649,Morgan,Orchard
8,Colorado,CO,80650,Weld,Pierce
8,Colorado,CO,80651,Weld,Platteville
8,Colorado,CO,80652,Weld,Roggen
8,Colorado,CO,80653,Morgan,Weldona
8,Colorado,CO,80654,Morgan,Hoyt
8,Colorado,CO,806HH,Adams,Zcta 806hh
8,Colorado,CO,80701,Morgan,Fort morgan
8,Colorado,CO,80705,Morgan,Log lane village
8,Colorado,CO,80720,Washington,Akron
8,Colorado,CO,80721,Phillips,Amherst
8,Colorado,CO,80722,Logan,Atwood
8,Colorado,CO,80723,Morgan,Brush
8,Colorado,CO,80726,Logan,Crook
8,Colorado,CO,80727,Yuma,Eckley
8,Colorado,CO,80728,Logan,Fleming
8,Colorado,CO,80729,Weld,Grover
8,Colorado,CO,80731,Phillips,Haxtun
8,Colorado,CO,80733,Morgan,Hillrose
8,Colorado,CO,80734,Phillips,Holyoke
8,Colorado,CO,80735,Yuma,Hale
8,Colorado,CO,80736,Logan,Iliff
8,Colorado,CO,80737,Sedgwick,Julesburg
8,Colorado,CO,80740,Washington,Lindon
8,Colorado,CO,80741,Logan,Willard
8,Colorado,CO,80742,Weld,New raymer
8,Colorado,CO,80743,Washington,Otis
8,Colorado,CO,80744,Sedgwick,Ovid
8,Colorado,CO,80745,Logan,Padroni
8,Colorado,CO,80747,Logan,Peetz
8,Colorado,CO,80749,Sedgwick,Sedgwick
8,Colorado,CO,80750,Morgan,Snyder
8,Colorado,CO,80751,Logan,Sterling
8,Colorado,CO,80754,Weld,Stoneham
8,Colorado,CO,80755,Yuma,Vernon
8,Colorado,CO,80757,Washington,Last chance
8,Colorado,CO,80758,Yuma,Laird
8,Colorado,CO,80759,Yuma,Yuma
8,Colorado,CO,807HH,Logan,Zcta 807hh
8,Colorado,CO,80801,Washington,Anton
8,Colorado,CO,80802,Cheyenne,Arapahoe
8,Colorado,CO,80804,Lincoln,Arriba
8,Colorado,CO,80805,Kit Carson,Bethune
8,Colorado,CO,80807,Kit Carson,Burlington
8,Colorado,CO,80808,El Paso,Calhan
8,Colorado,CO,80809,El Paso,North pole
8,Colorado,CO,80810,Cheyenne,Cheyenne wells
8,Colorado,CO,80812,Washington,Cope
8,Colorado,CO,80813,Teller,Cripple creek
8,Colorado,CO,80814,Teller,Divide
8,Colorado,CO,80815,Kit Carson,Flagler
8,Colorado,CO,80816,Teller,Florissant
8,Colorado,CO,80817,El Paso,Fountain
8,Colorado,CO,80818,Lincoln,Genoa
8,Colorado,CO,80819,El Paso,Green mountain f
8,Colorado,CO,80820,Park,Guffey
8,Colorado,CO,80821,Lincoln,Hugo
8,Colorado,CO,80822,Yuma,Joes
8,Colorado,CO,80823,Lincoln,Karval
8,Colorado,CO,80824,Yuma,Kirk
8,Colorado,CO,80825,Cheyenne,Kit carson
8,Colorado,CO,80827,Park,Lake george
8,Colorado,CO,80828,Lincoln,Limon
8,Colorado,CO,80829,El Paso,Manitou springs
8,Colorado,CO,80830,Elbert,Matheson
8,Colorado,CO,80831,El Paso,Peyton
8,Colorado,CO,80832,El Paso,Ramah
8,Colorado,CO,80833,El Paso,Rush
8,Colorado,CO,80834,Kit Carson,Seibert
8,Colorado,CO,80835,Elbert,Simla
8,Colorado,CO,80836,Kit Carson,Stratton
8,Colorado,CO,80840,El Paso,United states ai
8,Colorado,CO,80860,Teller,Victor
8,Colorado,CO,80861,Kit Carson,Vona
8,Colorado,CO,80862,Cheyenne,Wild horse
8,Colorado,CO,80863,Teller,Woodland park
8,Colorado,CO,80864,El Paso,Yoder
8,Colorado,CO,80866,Teller,Woodland park
8,Colorado,CO,80903,El Paso,Colorado springs
8,Colorado,CO,80904,El Paso,Colorado springs
8,Colorado,CO,80905,El Paso,Colorado springs
8,Colorado,CO,80906,El Paso,Colorado springs
8,Colorado,CO,80907,El Paso,Colorado springs
8,Colorado,CO,80908,El Paso,Colorado springs
8,Colorado,CO,80909,El Paso,Colorado springs
8,Colorado,CO,80910,El Paso,Colorado springs
8,Colorado,CO,80911,El Paso,Colorado springs
8,Colorado,CO,80913,El Paso,Fort carson
8,Colorado,CO,80915,El Paso,Colorado springs
8,Colorado,CO,80916,El Paso,Colorado springs
8,Colorado,CO,80917,El Paso,Colorado springs
8,Colorado,CO,80918,El Paso,Colorado springs
8,Colorado,CO,80919,El Paso,Colorado springs
8,Colorado,CO,80920,El Paso,Colorado springs
8,Colorado,CO,80921,El Paso,Colorado springs
8,Colorado,CO,80922,El Paso,Colorado springs
8,Colorado,CO,80925,El Paso,Colorado springs
8,Colorado,CO,80926,El Paso,Colorado springs
8,Colorado,CO,80928,El Paso,Colorado springs
8,Colorado,CO,80929,El Paso,Colorado springs
8,Colorado,CO,80930,El Paso,Colorado springs
8,Colorado,CO,81001,Pueblo,Pueblo
8,Colorado,CO,81003,Pueblo,Pueblo
8,Colorado,CO,81004,Pueblo,Pueblo
8,Colorado,CO,81005,Pueblo,Pueblo
8,Colorado,CO,81006,Pueblo,Pueblo
8,Colorado,CO,81007,Pueblo,Pueblo west
8,Colorado,CO,81008,Pueblo,Pueblo
8,Colorado,CO,81020,Las Animas,Aguilar
8,Colorado,CO,81021,Kiowa,Arlington
8,Colorado,CO,81022,Pueblo,North avondale
8,Colorado,CO,81023,Pueblo,Beulah
8,Colorado,CO,81024,Las Animas,Boncarbo
8,Colorado,CO,81025,Pueblo,Boone
8,Colorado,CO,81027,Las Animas,Branson
8,Colorado,CO,81029,Baca,Campo
8,Colorado,CO,81030,Otero,Cheraw
8,Colorado,CO,81033,Crowley,Crowley
8,Colorado,CO,81036,Kiowa,Chivington
8,Colorado,CO,81039,Otero,Fowler
8,Colorado,CO,81040,Huerfano,Farisita
8,Colorado,CO,81041,Prowers,Granada
8,Colorado,CO,81043,Prowers,Hartman
8,Colorado,CO,81044,Bent,Caddoa
8,Colorado,CO,81045,Kiowa,Haswell
8,Colorado,CO,81047,Prowers,Holly
8,Colorado,CO,81049,Las Animas,Villegreen
8,Colorado,CO,81050,Otero,Timpas
8,Colorado,CO,81052,Prowers,Lamar
8,Colorado,CO,81054,Bent,Deora
8,Colorado,CO,81055,Huerfano,Cuchara
8,Colorado,CO,81057,Bent,Mc clave
8,Colorado,CO,81058,Otero,Manzanola
8,Colorado,CO,81059,Las Animas,Delhi
8,Colorado,CO,81062,Crowley,Olney springs
8,Colorado,CO,81063,Crowley,Ordway
8,Colorado,CO,81064,Baca,Utleyville
8,Colorado,CO,81066,Huerfano,Red wing
8,Colorado,CO,81067,Otero,Rocky ford
8,Colorado,CO,81069,Pueblo,Rye
8,Colorado,CO,81071,Kiowa,Towner
8,Colorado,CO,81073,Baca,Springfield
8,Colorado,CO,81076,Crowley,Sugar city
8,Colorado,CO,81077,Otero,Swink
8,Colorado,CO,81081,Las Animas,Trinchera
8,Colorado,CO,81082,Las Animas,Jansen
8,Colorado,CO,81084,Baca,Lycan
8,Colorado,CO,81087,Baca,Vilas
8,Colorado,CO,81089,Huerfano,Farista
8,Colorado,CO,81090,Baca,Walsh
8,Colorado,CO,81091,Las Animas,Weston
8,Colorado,CO,81092,Prowers,Wiley
8,Colorado,CO,810HH,Bent,Zcta 810hh
8,Colorado,CO,810XX,Huerfano,Zcta 810xx
8,Colorado,CO,81101,Alamosa,Alamosa
8,Colorado,CO,81120,Conejos,Antonito
8,Colorado,CO,81121,Archuleta,Arboles
8,Colorado,CO,81122,La Plata,Bayfield
8,Colorado,CO,81123,Costilla,Blanca
8,Colorado,CO,81124,Conejos,Capulin
8,Colorado,CO,81125,Saguache,Center
8,Colorado,CO,81126,Costilla,Chama
8,Colorado,CO,81127,Archuleta,Chimney rock
8,Colorado,CO,81128,Archuleta,Chromo
8,Colorado,CO,81130,Mineral,Creede
8,Colorado,CO,81131,Saguache,Crestone
8,Colorado,CO,81132,Rio Grande,La garita
8,Colorado,CO,81133,Costilla,Fort garland
8,Colorado,CO,81136,Alamosa,Hooper
8,Colorado,CO,81137,La Plata,Ignacio
8,Colorado,CO,81140,Conejos,La jara
8,Colorado,CO,81141,Conejos,Manassa
8,Colorado,CO,81143,Saguache,Moffat
8,Colorado,CO,81144,Rio Grande,Monte vista
8,Colorado,CO,81146,Alamosa,Mosca
8,Colorado,CO,81147,Archuleta,Pagosa springs
8,Colorado,CO,81148,Conejos,Romeo
8,Colorado,CO,81149,Saguache,Saguache
8,Colorado,CO,81151,Conejos,Sanford
8,Colorado,CO,81152,Costilla,Mesita
8,Colorado,CO,81153,Costilla,San pablo
8,Colorado,CO,81154,Rio Grande,South fork
8,Colorado,CO,81155,Saguache,Villa grove
8,Colorado,CO,811XX,Costilla,Zcta 811xx
8,Colorado,CO,81201,Chaffee,Salida
8,Colorado,CO,81210,Gunnison,Almont
8,Colorado,CO,81211,Chaffee,Buena vista
8,Colorado,CO,81212,Fremont,Canon city
8,Colorado,CO,81220,Gunnison,Cimarron
8,Colorado,CO,81221,Fremont,Coal creek
8,Colorado,CO,81222,Fremont,Coaldale
8,Colorado,CO,81223,Fremont,Cotopaxi
8,Colorado,CO,81224,Gunnison,Crested butte
8,Colorado,CO,81225,Gunnison,Crested butte
8,Colorado,CO,81226,Fremont,Florence
8,Colorado,CO,81230,Gunnison,Gunnison
8,Colorado,CO,81233,Fremont,Howard
8,Colorado,CO,81235,Hinsdale,Lake city
8,Colorado,CO,81236,Chaffee,Nathrop
8,Colorado,CO,81239,Gunnison,Parlin
8,Colorado,CO,81240,Fremont,Penrose
8,Colorado,CO,81241,Gunnison,Pitkin
8,Colorado,CO,81243,Gunnison,Powderhorn
8,Colorado,CO,81244,Fremont,Rockvale
8,Colorado,CO,81248,Saguache,Sargents
8,Colorado,CO,81251,Lake,Twin lakes
8,Colorado,CO,81252,Custer,Westcliffe
8,Colorado,CO,81253,Custer,Wetmore
8,Colorado,CO,812HH,Fremont,Zcta 812hh
8,Colorado,CO,812XX,Hinsdale,Zcta 812xx
8,Colorado,CO,81301,La Plata,Durango
8,Colorado,CO,81320,Dolores,Cahone
8,Colorado,CO,81321,Montezuma,Cortez
8,Colorado,CO,81323,Montezuma,Dolores
8,Colorado,CO,81324,Dolores,Dove creek
8,Colorado,CO,81325,San Miguel,Egnar
8,Colorado,CO,81326,La Plata,Hesperus
8,Colorado,CO,81327,Montezuma,Lewis
8,Colorado,CO,81328,Montezuma,Mancos
8,Colorado,CO,81330,Montezuma,Mesa verde natio
8,Colorado,CO,81331,Montezuma,Pleasant view
8,Colorado,CO,81332,Dolores,Rico
8,Colorado,CO,81334,Montezuma,Towaoc
8,Colorado,CO,81335,Montezuma,Yellow jacket
8,Colorado,CO,813XX,Dolores,Zcta 813xx
8,Colorado,CO,81401,Montrose,Montrose
8,Colorado,CO,81410,Delta,Austin
8,Colorado,CO,81411,Montrose,Bedrock
8,Colorado,CO,81413,Delta,Cedaredge
8,Colorado,CO,81415,Delta,Crawford
8,Colorado,CO,81416,Delta,Delta
8,Colorado,CO,81418,Delta,Eckert
8,Colorado,CO,81419,Delta,Hotchkiss
8,Colorado,CO,81422,Montrose,Naturita
8,Colorado,CO,81423,San Miguel,Norwood
8,Colorado,CO,81424,Montrose,Nucla
8,Colorado,CO,81425,Montrose,Olathe
8,Colorado,CO,81426,San Miguel,Ophir
8,Colorado,CO,81427,Ouray,Ouray
8,Colorado,CO,81428,Delta,Paonia
8,Colorado,CO,81430,San Miguel,Placerville
8,Colorado,CO,81431,Montrose,Redvale
8,Colorado,CO,81432,Ouray,Ridgway
8,Colorado,CO,81433,San Juan,Silverton
8,Colorado,CO,81434,Gunnison,Somerset
8,Colorado,CO,81435,San Miguel,Telluride
8,Colorado,CO,814XX,San Juan,Zcta 814xx
8,Colorado,CO,81501,Mesa,Grand junction
8,Colorado,CO,81503,Mesa,Grand junction
8,Colorado,CO,81504,Mesa,Fruitvale
8,Colorado,CO,81505,Mesa,Grand junction
8,Colorado,CO,81506,Mesa,Grand junction
8,Colorado,CO,81520,Mesa,Clifton
8,Colorado,CO,81521,Mesa,Fruita
8,Colorado,CO,81522,Mesa,Gateway
8,Colorado,CO,81523,Mesa,Glade park
8,Colorado,CO,81524,Mesa,Loma
8,Colorado,CO,81525,Mesa,Mack
8,Colorado,CO,81526,Mesa,Palisade
8,Colorado,CO,81527,Mesa,Whitewater
8,Colorado,CO,815HH,Mesa,Zcta 815hh
8,Colorado,CO,815XX,Mesa,Zcta 815xx
8,Colorado,CO,81601,Garfield,Glenwood springs
8,Colorado,CO,81610,Moffat,Dinosaur
8,Colorado,CO,81611,Pitkin,Aspen
8,Colorado,CO,81615,Pitkin,Snowmass village
8,Colorado,CO,81620,Eagle,Avon
8,Colorado,CO,81621,Eagle,Basalt
8,Colorado,CO,81623,Garfield,Marble
8,Colorado,CO,81624,Mesa,Collbran
8,Colorado,CO,81625,Moffat,Craig
8,Colorado,CO,81630,Mesa,De beque
8,Colorado,CO,81631,Eagle,Eagle
8,Colorado,CO,81632,Eagle,Edwards
8,Colorado,CO,81635,Garfield,Battlement mesa
8,Colorado,CO,81637,Eagle,Gypsum
8,Colorado,CO,81638,Moffat,Hamilton
8,Colorado,CO,81639,Routt,Hayden
8,Colorado,CO,81640,Moffat,Maybell
8,Colorado,CO,81641,Rio Blanco,Meeker
8,Colorado,CO,81642,Pitkin,Meredith
8,Colorado,CO,81643,Mesa,Mesa
8,Colorado,CO,81645,Eagle,Gilman
8,Colorado,CO,81646,Mesa,Molina
8,Colorado,CO,81647,Garfield,New castle
8,Colorado,CO,81648,Rio Blanco,Rangely
8,Colorado,CO,81649,Eagle,Red cliff
8,Colorado,CO,81650,Garfield,Rifle
8,Colorado,CO,81652,Garfield,Silt
8,Colorado,CO,81653,Routt,Slater
8,Colorado,CO,81654,Pitkin,Snowmass
8,Colorado,CO,81655,Eagle,Wolcott
8,Colorado,CO,81656,Pitkin,Woody creek
8,Colorado,CO,81657,Eagle,Vail
8,Colorado,CO,816HH,Garfield,Zcta 816hh
8,Colorado,CO,816XX,Moffat,Zcta 816xx
8,Colorado,CO,82063,Larimer,
8,Colorado,CO,80002,Jefferson,Arvada
8,Colorado,CO,80003,Jefferson,Arvada
8,Colorado,CO,80004,Jefferson,Arvada
8,Colorado,CO,80005,Jefferson,Arvada
8,Colorado,CO,80007,Jefferson,Zcta 80007
8,Colorado,CO,80010,Adams,Aurora
8,Colorado,CO,80011,Arapahoe,Aurora
8,Colorado,CO,80012,Arapahoe,Aurora
8,Colorado,CO,80013,Arapahoe,Aurora
8,Colorado,CO,80014,Arapahoe,Aurora
8,Colorado,CO,80015,Arapahoe,Aurora
8,Colorado,CO,80016,Arapahoe,Aurora
8,Colorado,CO,80017,Arapahoe,Aurora
8,Colorado,CO,80018,Arapahoe,Aurora
8,Colorado,CO,80019,Adams,Aurora
8,Colorado,CO,80020,Boulder,Broomfield
8,Colorado,CO,80021,Jefferson,Westminster
8,Colorado,CO,80022,Adams,Commerce city
8,Colorado,CO,80024,Adams,Dupont
8,Colorado,CO,80025,Boulder,Eldorado springs
8,Colorado,CO,80026,Boulder,Lafayette
8,Colorado,CO,80027,Boulder,Louisville
8,Colorado,CO,80030,Adams,Westminster
8,Colorado,CO,80031,Adams,Westminster
8,Colorado,CO,80033,Jefferson,Wheat ridge
8,Colorado,CO,800HH,Arapahoe,Zcta 800hh
8,Colorado,CO,800XX,Adams,Zcta 800xx
8,Colorado,CO,80101,Elbert,Agate
8,Colorado,CO,80102,Adams,Bennett
8,Colorado,CO,80103,Arapahoe,Byers
8,Colorado,CO,80104,Douglas,Castle rock
8,Colorado,CO,80105,Arapahoe,Deer trail
8,Colorado,CO,80106,El Paso,Elbert
8,Colorado,CO,80107,Elbert,Elizabeth
8,Colorado,CO,80110,Arapahoe,Cherry hills vil
8,Colorado,CO,80111,Arapahoe,Cherry hills vil
8,Colorado,CO,80112,Arapahoe,Englewood
8,Colorado,CO,80116,Douglas,Franktown
8,Colorado,CO,80117,Elbert,Kiowa
8,Colorado,CO,80118,Douglas,Larkspur
8,Colorado,CO,80120,Arapahoe,Littleton
8,Colorado,CO,80121,Arapahoe,Greenwood villag
8,Colorado,CO,80122,Arapahoe,Littleton
8,Colorado,CO,80123,Jefferson,Bow mar
8,Colorado,CO,80124,Douglas,Littleton
8,Colorado,CO,80125,Douglas,Littleton
8,Colorado,CO,80126,Douglas,Highlands ranch
8,Colorado,CO,80127,Jefferson,Littleton
8,Colorado,CO,80128,Jefferson,Zcta 80128
8,Colorado,CO,80132,El Paso,Monument
8,Colorado,CO,80133,El Paso,Palmer lake
8,Colorado,CO,80134,Douglas,Parker
8,Colorado,CO,80135,Douglas,Deckers
8,Colorado,CO,80136,Adams,Strasburg
8,Colorado,CO,80137,Adams,Watkins
8,Colorado,CO,80138,Douglas,Zcta 80138
8,Colorado,CO,801XX,Arapahoe,Zcta 801xx
8,Colorado,CO,80202,Denver,Denver
8,Colorado,CO,80203,Denver,Denver
8,Colorado,CO,80204,Denver,Denver
8,Colorado,CO,80205,Denver,Denver
8,Colorado,CO,80206,Denver,Denver
8,Colorado,CO,80207,Denver,Denver
8,Colorado,CO,80209,Denver,Denver
8,Colorado,CO,80210,Denver,Denver
8,Colorado,CO,80211,Denver,Denver
8,Colorado,CO,80212,Denver,Mountain view
8,Colorado,CO,80214,Jefferson,Edgewater
8,Colorado,CO,80215,Jefferson,Lakewood
8,Colorado,CO,80216,Denver,Denver
8,Colorado,CO,80218,Denver,Denver
8,Colorado,CO,80219,Denver,Denver
8,Colorado,CO,80220,Denver,Denver
8,Colorado,CO,80221,Adams,Federal heights
8,Colorado,CO,80222,Denver,Glendale
8,Colorado,CO,80223,Denver,Denver
8,Colorado,CO,80224,Denver,Denver
8,Colorado,CO,80226,Jefferson,Lakewood
8,Colorado,CO,80227,Jefferson,Denver
8,Colorado,CO,80228,Jefferson,Lakewood
8,Colorado,CO,80229,Adams,Thornton
8,Colorado,CO,80230,Denver,Lowry afb
8,Colorado,CO,80231,Denver,Denver
8,Colorado,CO,80232,Jefferson,Lakewood
8,Colorado,CO,80233,Adams,Northglenn
8,Colorado,CO,80234,Adams,Northglenn
8,Colorado,CO,80235,Jefferson,Denver
8,Colorado,CO,80236,Denver,Denver
8,Colorado,CO,80237,Denver,Denver
8,Colorado,CO,80239,Denver,Denver
8,Colorado,CO,80241,Adams,Northglenn
8,Colorado,CO,80246,Denver,Zcta 80246
8,Colorado,CO,80249,Denver,Denver
8,Colorado,CO,80260,Adams,Zcta 80260
8,Colorado,CO,80264,Denver,Lincoln center b
8,Colorado,CO,80290,Denver,Two united bank
8,Colorado,CO,80293,Denver,First interstate
8,Colorado,CO,80294,Denver,Denver
8,Colorado,CO,80301,Boulder,Boulder
8,Colorado,CO,80302,Boulder,Boulder
8,Colorado,CO,80303,Boulder,Boulder
8,Colorado,CO,80304,Boulder,Boulder
8,Colorado,CO,80401,Jefferson,Golden
8,Colorado,CO,80403,Jefferson,Golden
8,Colorado,CO,80420,Park,Alma
8,Colorado,CO,80421,Park,Bailey
8,Colorado,CO,80422,Gilpin,Black hawk
8,Colorado,CO,80423,Eagle,Bond
8,Colorado,CO,80424,Summit,Breckenridge
8,Colorado,CO,80425,Jefferson,Buffalo creek
8,Colorado,CO,80426,Eagle,Burns
8,Colorado,CO,80427,Gilpin,Central city
8,Colorado,CO,80428,Routt,Clark
8,Colorado,CO,80430,Jackson,Coalmont
8,Colorado,CO,80432,Park,Como
8,Colorado,CO,80433,Jefferson,Conifer
8,Colorado,CO,80434,Jackson,Cowdrey
8,Colorado,CO,80435,Summit,Keystone
8,Colorado,CO,80436,Clear Creek,Dumont
8,Colorado,CO,80438,Clear Creek,Empire
8,Colorado,CO,80439,Jefferson,Evergreen
8,Colorado,CO,80440,Park,Fairplay
8,Colorado,CO,80442,Grand,Fraser
8,Colorado,CO,80443,Summit,Copper mountain
8,Colorado,CO,80444,Clear Creek,Georgetown
8,Colorado,CO,80446,Grand,Granby
8,Colorado,CO,80447,Grand,Grand lake
8,Colorado,CO,80448,Park,Grant
8,Colorado,CO,80449,Park,Hartsel
8,Colorado,CO,80451,Grand,Hot sulphur spri
8,Colorado,CO,80452,Clear Creek,Idaho springs
8,Colorado,CO,80454,Jefferson,Indian hills
8,Colorado,CO,80455,Boulder,Jamestown
8,Colorado,CO,80456,Park,Jefferson
8,Colorado,CO,80457,Jefferson,Kittredge
8,Colorado,CO,80459,Grand,Kremmling
8,Colorado,CO,80461,Lake,Leadville
8,Colorado,CO,80463,Eagle,Mc coy
8,Colorado,CO,80465,Jefferson,Morrison
8,Colorado,CO,80466,Boulder,Nederland
8,Colorado,CO,80467,Routt,Oak creek
8,Colorado,CO,80468,Grand,Parshall
8,Colorado,CO,80469,Routt,Phippsburg
8,Colorado,CO,80470,Jefferson,Pine
8,Colorado,CO,80473,Jackson,Rand
8,Colorado,CO,80474,Gilpin,Rollinsville
8,Colorado,CO,80476,Clear Creek,Silver plume
8,Colorado,CO,80478,Grand,Tabernash
8,Colorado,CO,80479,Routt,Toponas
8,Colorado,CO,80480,Jackson,Walden
8,Colorado,CO,80481,Boulder,Ward
8,Colorado,CO,80482,Grand,Winter park
8,Colorado,CO,80483,Routt,Yampa
8,Colorado,CO,80487,Routt,Steamboat spring
8,Colorado,CO,80498,Summit,Silverthorne
8,Colorado,CO,804HH,Grand,Zcta 804hh
8,Colorado,CO,804XX,Grand,Zcta 804xx
8,Colorado,CO,80501,Boulder,Longmont
8,Colorado,CO,80503,Boulder,Longmont
8,Colorado,CO,80504,Weld,Longmont
8,Colorado,CO,80510,Boulder,Allenspark
8,Colorado,CO,80512,Larimer,Bellvue
8,Colorado,CO,80513,Larimer,Berthoud
8,Colorado,CO,80514,Weld,Dacono
8,Colorado,CO,80515,Larimer,Drake
8,Colorado,CO,80516,Boulder,Erie
8,Colorado,CO,80517,Larimer,Estes park
8,Colorado,CO,80520,Weld,Firestone
8,Colorado,CO,80521,Larimer,Fort collins
8,Colorado,CO,80524,Larimer,Fort collins
8,Colorado,CO,80525,Larimer,Fort collins
8,Colorado,CO,80526,Larimer,Fort collins
8,Colorado,CO,80528,Larimer,Zcta 80528
8,Colorado,CO,80530,Weld,Frederick
8,Colorado,CO,80532,Larimer,Glen haven
8,Colorado,CO,80534,Weld,Johnstown
8,Colorado,CO,80535,Larimer,Laporte
8,Colorado,CO,80536,Larimer,Virginia dale
8,Colorado,CO,80537,Larimer,Loveland
8,Colorado,CO,80538,Larimer,Loveland
8,Colorado,CO,80540,Boulder,Lyons
8,Colorado,CO,80542,Weld,Mead
8,Colorado,CO,80543,Weld,Milliken
8,Colorado,CO,80545,Larimer,Red feather lake
8,Colorado,CO,80547,Larimer,Timnath
8,Colorado,CO,80549,Larimer,Wellington
8,Colorado,CO,80550,Weld,Windsor
8,Colorado,CO,80601,Adams,Lochbui
8,Colorado,CO,80610,Weld,Ault
8,Colorado,CO,80611,Weld,Briggsdale
8,Colorado,CO,80612,Weld,Carr
8,Colorado,CO,80615,Weld,Eaton
8,Colorado,CO,80620,Weld,Evans
8,Colorado,CO,80621,Weld,Wattenburg
8,Colorado,CO,80623,Weld,Gilcrest
8,Colorado,CO,80624,Weld,Gill
8,Colorado,CO,80631,Weld,Garden city
8,Colorado,CO,80634,Weld,Greeley
8,Colorado,CO,80640,Adams,Henderson
8,Colorado,CO,80642,Weld,Hudson
8,Colorado,CO,80643,Weld,Keenesburg
8,Colorado,CO,80644,Weld,Kersey
8,Colorado,CO,80645,Weld,La salle
8,Colorado,CO,80648,Weld,Nunn
8,Colorado,CO,80649,Morgan,Orchard
8,Colorado,CO,80650,Weld,Pierce
8,Colorado,CO,80651,Weld,Platteville
8,Colorado,CO,80652,Weld,Roggen
8,Colorado,CO,80653,Morgan,Weldona
8,Colorado,CO,80654,Morgan,Hoyt
8,Colorado,CO,806HH,Adams,Zcta 806hh
8,Colorado,CO,80701,Morgan,Fort morgan
8,Colorado,CO,80705,Morgan,Log lane village
8,Colorado,CO,80720,Washington,Akron
8,Colorado,CO,80721,Phillips,Amherst
8,Colorado,CO,80722,Logan,Atwood
8,Colorado,CO,80723,Morgan,Brush
8,Colorado,CO,80726,Logan,Crook
8,Colorado,CO,80727,Yuma,Eckley
8,Colorado,CO,80728,Logan,Fleming
8,Colorado,CO,80729,Weld,Grover
8,Colorado,CO,80731,Phillips,Haxtun
8,Colorado,CO,80733,Morgan,Hillrose
8,Colorado,CO,80734,Phillips,Holyoke
8,Colorado,CO,80735,Yuma,Hale
8,Colorado,CO,80736,Logan,Iliff
8,Colorado,CO,80737,Sedgwick,Julesburg
8,Colorado,CO,80740,Washington,Lindon
8,Colorado,CO,80741,Logan,Willard
8,Colorado,CO,80742,Weld,New raymer
8,Colorado,CO,80743,Washington,Otis
8,Colorado,CO,80744,Sedgwick,Ovid
8,Colorado,CO,80745,Logan,Padroni
8,Colorado,CO,80747,Logan,Peetz
8,Colorado,CO,80749,Sedgwick,Sedgwick
8,Colorado,CO,80750,Morgan,Snyder
8,Colorado,CO,80751,Logan,Sterling
8,Colorado,CO,80754,Weld,Stoneham
8,Colorado,CO,80755,Yuma,Vernon
8,Colorado,CO,80757,Washington,Last chance
8,Colorado,CO,80758,Yuma,Laird
8,Colorado,CO,80759,Yuma,Yuma
8,Colorado,CO,807HH,Logan,Zcta 807hh
8,Colorado,CO,80801,Washington,Anton
8,Colorado,CO,80802,Cheyenne,Arapahoe
8,Colorado,CO,80804,Lincoln,Arriba
8,Colorado,CO,80805,Kit Carson,Bethune
8,Colorado,CO,80807,Kit Carson,Burlington
8,Colorado,CO,80808,El Paso,Calhan
8,Colorado,CO,80809,El Paso,North pole
8,Colorado,CO,80810,Cheyenne,Cheyenne wells
8,Colorado,CO,80812,Washington,Cope
8,Colorado,CO,80813,Teller,Cripple creek
8,Colorado,CO,80814,Teller,Divide
8,Colorado,CO,80815,Kit Carson,Flagler
8,Colorado,CO,80816,Teller,Florissant
8,Colorado,CO,80817,El Paso,Fountain
8,Colorado,CO,80818,Lincoln,Genoa
8,Colorado,CO,80819,El Paso,Green mountain f
8,Colorado,CO,80820,Park,Guffey
8,Colorado,CO,80821,Lincoln,Hugo
8,Colorado,CO,80822,Yuma,Joes
8,Colorado,CO,80823,Lincoln,Karval
8,Colorado,CO,80824,Yuma,Kirk
8,Colorado,CO,80825,Cheyenne,Kit carson
8,Colorado,CO,80827,Park,Lake george
8,Colorado,CO,80828,Lincoln,Limon
8,Colorado,CO,80829,El Paso,Manitou springs
8,Colorado,CO,80830,Elbert,Matheson
8,Colorado,CO,80831,El Paso,Peyton
8,Colorado,CO,80832,El Paso,Ramah
8,Colorado,CO,80833,El Paso,Rush
8,Colorado,CO,80834,Kit Carson,Seibert
8,Colorado,CO,80835,Elbert,Simla
8,Colorado,CO,80836,Kit Carson,Stratton
8,Colorado,CO,80840,El Paso,United states ai
8,Colorado,CO,80860,Teller,Victor
8,Colorado,CO,80861,Kit Carson,Vona
8,Colorado,CO,80862,Cheyenne,Wild horse
8,Colorado,CO,80863,Teller,Woodland park
8,Colorado,CO,80864,El Paso,Yoder
8,Colorado,CO,80866,Teller,Woodland park
8,Colorado,CO,80903,El Paso,Colorado springs
8,Colorado,CO,80904,El Paso,Colorado springs
8,Colorado,CO,80905,El Paso,Colorado springs
8,Colorado,CO,80906,El Paso,Colorado springs
8,Colorado,CO,80907,El Paso,Colorado springs
8,Colorado,CO,80908,El Paso,Colorado springs
8,Colorado,CO,80909,El Paso,Colorado springs
8,Colorado,CO,80910,El Paso,Colorado springs
8,Colorado,CO,80911,El Paso,Colorado springs
8,Colorado,CO,80913,El Paso,Fort carson
8,Colorado,CO,80915,El Paso,Colorado springs
8,Colorado,CO,80916,El Paso,Colorado springs
8,Colorado,CO,80917,El Paso,Colorado springs
8,Colorado,CO,80918,El Paso,Colorado springs
8,Colorado,CO,80919,El Paso,Colorado springs
8,Colorado,CO,80920,El Paso,Colorado springs
8,Colorado,CO,80921,El Paso,Colorado springs
8,Colorado,CO,80922,El Paso,Colorado springs
8,Colorado,CO,80925,El Paso,Colorado springs
8,Colorado,CO,80926,El Paso,Colorado springs
8,Colorado,CO,80928,El Paso,Colorado springs
8,Colorado,CO,80929,El Paso,Colorado springs
8,Colorado,CO,80930,El Paso,Colorado springs
8,Colorado,CO,81001,Pueblo,Pueblo
8,Colorado,CO,81003,Pueblo,Pueblo
8,Colorado,CO,81004,Pueblo,Pueblo
8,Colorado,CO,81005,Pueblo,Pueblo
8,Colorado,CO,81006,Pueblo,Pueblo
8,Colorado,CO,81007,Pueblo,Pueblo west
8,Colorado,CO,81008,Pueblo,Pueblo
8,Colorado,CO,81020,Las Animas,Aguilar
8,Colorado,CO,81021,Kiowa,Arlington
8,Colorado,CO,81022,Pueblo,North avondale
8,Colorado,CO,81023,Pueblo,Beulah
8,Colorado,CO,81024,Las Animas,Boncarbo
8,Colorado,CO,81025,Pueblo,Boone
8,Colorado,CO,81027,Las Animas,Branson
8,Colorado,CO,81029,Baca,Campo
8,Colorado,CO,81030,Otero,Cheraw
8,Colorado,CO,81033,Crowley,Crowley
8,Colorado,CO,81036,Kiowa,Chivington
8,Colorado,CO,81039,Otero,Fowler
8,Colorado,CO,81040,Huerfano,Farisita
8,Colorado,CO,81041,Prowers,Granada
8,Colorado,CO,81043,Prowers,Hartman
8,Colorado,CO,81044,Bent,Caddoa
8,Colorado,CO,81045,Kiowa,Haswell
8,Colorado,CO,81047,Prowers,Holly
8,Colorado,CO,81049,Las Animas,Villegreen
8,Colorado,CO,81050,Otero,Timpas
8,Colorado,CO,81052,Prowers,Lamar
8,Colorado,CO,81054,Bent,Deora
8,Colorado,CO,81055,Huerfano,Cuchara
8,Colorado,CO,81057,Bent,Mc clave
8,Colorado,CO,81058,Otero,Manzanola
8,Colorado,CO,81059,Las Animas,Delhi
8,Colorado,CO,81062,Crowley,Olney springs
8,Colorado,CO,81063,Crowley,Ordway
8,Colorado,CO,81064,Baca,Utleyville
8,Colorado,CO,81066,Huerfano,Red wing
8,Colorado,CO,81067,Otero,Rocky ford
8,Colorado,CO,81069,Pueblo,Rye
8,Colorado,CO,81071,Kiowa,Towner
8,Colorado,CO,81073,Baca,Springfield
8,Colorado,CO,81076,Crowley,Sugar city
8,Colorado,CO,81077,Otero,Swink
8,Colorado,CO,81081,Las Animas,Trinchera
8,Colorado,CO,81082,Las Animas,Jansen
8,Colorado,CO,81084,Baca,Lycan
8,Colorado,CO,81087,Baca,Vilas
8,Colorado,CO,81089,Huerfano,Farista
8,Colorado,CO,81090,Baca,Walsh
8,Colorado,CO,81091,Las Animas,Weston
8,Colorado,CO,81092,Prowers,Wiley
8,Colorado,CO,810HH,Bent,Zcta 810hh
8,Colorado,CO,810XX,Huerfano,Zcta 810xx
8,Colorado,CO,81101,Alamosa,Alamosa
8,Colorado,CO,81120,Conejos,Antonito
8,Colorado,CO,81121,Archuleta,Arboles
8,Colorado,CO,81122,La Plata,Bayfield
8,Colorado,CO,81123,Costilla,Blanca
8,Colorado,CO,81124,Conejos,Capulin
8,Colorado,CO,81125,Saguache,Center
8,Colorado,CO,81126,Costilla,Chama
8,Colorado,CO,81127,Archuleta,Chimney rock
8,Colorado,CO,81128,Archuleta,Chromo
8,Colorado,CO,81130,Mineral,Creede
8,Colorado,CO,81131,Saguache,Crestone
8,Colorado,CO,81132,Rio Grande,La garita
8,Colorado,CO,81133,Costilla,Fort garland
8,Colorado,CO,81136,Alamosa,Hooper
8,Colorado,CO,81137,La Plata,Ignacio
8,Colorado,CO,81140,Conejos,La jara
8,Colorado,CO,81141,Conejos,Manassa
8,Colorado,CO,81143,Saguache,Moffat
8,Colorado,CO,81144,Rio Grande,Monte vista
8,Colorado,CO,81146,Alamosa,Mosca
8,Colorado,CO,81147,Archuleta,Pagosa springs
8,Colorado,CO,81148,Conejos,Romeo
8,Colorado,CO,81149,Saguache,Saguache
8,Colorado,CO,81151,Conejos,Sanford
8,Colorado,CO,81152,Costilla,Mesita
8,Colorado,CO,81153,Costilla,San pablo
8,Colorado,CO,81154,Rio Grande,South fork
8,Colorado,CO,81155,Saguache,Villa grove
8,Colorado,CO,811XX,Costilla,Zcta 811xx
8,Colorado,CO,81201,Chaffee,Salida
8,Colorado,CO,81210,Gunnison,Almont
8,Colorado,CO,81211,Chaffee,Buena vista
8,Colorado,CO,81212,Fremont,Canon city
8,Colorado,CO,81220,Gunnison,Cimarron
8,Colorado,CO,81221,Fremont,Coal creek
8,Colorado,CO,81222,Fremont,Coaldale
8,Colorado,CO,81223,Fremont,Cotopaxi
8,Colorado,CO,81224,Gunnison,Crested butte
8,Colorado,CO,81225,Gunnison,Crested butte
8,Colorado,CO,81226,Fremont,Florence
8,Colorado,CO,81230,Gunnison,Gunnison
8,Colorado,CO,81233,Fremont,Howard
8,Colorado,CO,81235,Hinsdale,Lake city
8,Colorado,CO,81236,Chaffee,Nathrop
8,Colorado,CO,81239,Gunnison,Parlin
8,Colorado,CO,81240,Fremont,Penrose
8,Colorado,CO,81241,Gunnison,Pitkin
8,Colorado,CO,81243,Gunnison,Powderhorn
8,Colorado,CO,81244,Fremont,Rockvale
8,Colorado,CO,81248,Saguache,Sargents
8,Colorado,CO,81251,Lake,Twin lakes
8,Colorado,CO,81252,Custer,Westcliffe
8,Colorado,CO,81253,Custer,Wetmore
8,Colorado,CO,812HH,Fremont,Zcta 812hh
8,Colorado,CO,812XX,Hinsdale,Zcta 812xx
8,Colorado,CO,81301,La Plata,Durango
8,Colorado,CO,81320,Dolores,Cahone
8,Colorado,CO,81321,Montezuma,Cortez
8,Colorado,CO,81323,Montezuma,Dolores
8,Colorado,CO,81324,Dolores,Dove creek
8,Colorado,CO,81325,San Miguel,Egnar
8,Colorado,CO,81326,La Plata,Hesperus
8,Colorado,CO,81327,Montezuma,Lewis
8,Colorado,CO,81328,Montezuma,Mancos
8,Colorado,CO,81330,Montezuma,Mesa verde natio
8,Colorado,CO,81331,Montezuma,Pleasant view
8,Colorado,CO,81332,Dolores,Rico
8,Colorado,CO,81334,Montezuma,Towaoc
8,Colorado,CO,81335,Montezuma,Yellow jacket
8,Colorado,CO,813XX,Dolores,Zcta 813xx
8,Colorado,CO,81401,Montrose,Montrose
8,Colorado,CO,81410,Delta,Austin
8,Colorado,CO,81411,Montrose,Bedrock
8,Colorado,CO,81413,Delta,Cedaredge
8,Colorado,CO,81415,Delta,Crawford
8,Colorado,CO,81416,Delta,Delta
8,Colorado,CO,81418,Delta,Eckert
8,Colorado,CO,81419,Delta,Hotchkiss
8,Colorado,CO,81422,Montrose,Naturita
8,Colorado,CO,81423,San Miguel,Norwood
8,Colorado,CO,81424,Montrose,Nucla
8,Colorado,CO,81425,Montrose,Olathe
8,Colorado,CO,81426,San Miguel,Ophir
8,Colorado,CO,81427,Ouray,Ouray
8,Colorado,CO,81428,Delta,Paonia
8,Colorado,CO,81430,San Miguel,Placerville
8,Colorado,CO,81431,Montrose,Redvale
8,Colorado,CO,81432,Ouray,Ridgway
8,Colorado,CO,81433,San Juan,Silverton
8,Colorado,CO,81434,Gunnison,Somerset
8,Colorado,CO,81435,San Miguel,Telluride
8,Colorado,CO,814XX,San Juan,Zcta 814xx
8,Colorado,CO,81501,Mesa,Grand junction
8,Colorado,CO,81503,Mesa,Grand junction
8,Colorado,CO,81504,Mesa,Fruitvale
8,Colorado,CO,81505,Mesa,Grand junction
8,Colorado,CO,81506,Mesa,Grand junction
8,Colorado,CO,81520,Mesa,Clifton
8,Colorado,CO,81521,Mesa,Fruita
8,Colorado,CO,81522,Mesa,Gateway
8,Colorado,CO,81523,Mesa,Glade park
8,Colorado,CO,81524,Mesa,Loma
8,Colorado,CO,81525,Mesa,Mack
8,Colorado,CO,81526,Mesa,Palisade
8,Colorado,CO,81527,Mesa,Whitewater
8,Colorado,CO,815HH,Mesa,Zcta 815hh
8,Colorado,CO,815XX,Mesa,Zcta 815xx
8,Colorado,CO,81601,Garfield,Glenwood springs
8,Colorado,CO,81610,Moffat,Dinosaur
8,Colorado,CO,81611,Pitkin,Aspen
8,Colorado,CO,81615,Pitkin,Snowmass village
8,Colorado,CO,81620,Eagle,Avon
8,Colorado,CO,81621,Eagle,Basalt
8,Colorado,CO,81623,Garfield,Marble
8,Colorado,CO,81624,Mesa,Collbran
8,Colorado,CO,81625,Moffat,Craig
8,Colorado,CO,81630,Mesa,De beque
8,Colorado,CO,81631,Eagle,Eagle
8,Colorado,CO,81632,Eagle,Edwards
8,Colorado,CO,81635,Garfield,Battlement mesa
8,Colorado,CO,81637,Eagle,Gypsum
8,Colorado,CO,81638,Moffat,Hamilton
8,Colorado,CO,81639,Routt,Hayden
8,Colorado,CO,81640,Moffat,Maybell
8,Colorado,CO,81641,Rio Blanco,Meeker
8,Colorado,CO,81642,Pitkin,Meredith
8,Colorado,CO,81643,Mesa,Mesa
8,Colorado,CO,81645,Eagle,Gilman
8,Colorado,CO,81646,Mesa,Molina
8,Colorado,CO,81647,Garfield,New castle
8,Colorado,CO,81648,Rio Blanco,Rangely
8,Colorado,CO,81649,Eagle,Red cliff
8,Colorado,CO,81650,Garfield,Rifle
8,Colorado,CO,81652,Garfield,Silt
8,Colorado,CO,81653,Routt,Slater
8,Colorado,CO,81654,Pitkin,Snowmass
8,Colorado,CO,81655,Eagle,Wolcott
8,Colorado,CO,81656,Pitkin,Woody creek
8,Colorado,CO,81657,Eagle,Vail
8,Colorado,CO,816HH,Garfield,Zcta 816hh
8,Colorado,CO,816XX,Moffat,Zcta 816xx
8,Colorado,CO,82063,Larimer,
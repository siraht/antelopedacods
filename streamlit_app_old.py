import streamlit as st
import pandas as pd
import json
import re
from datetime import datetime
from io import StringIO

# Constants and static data
PROVIDERID = "ABC123"
PROVIDERLOCATIONID = "LOC001"

# Gender options for dropdown
gender_options = {
    "Male": 1,
    "Female": 2,
    "Other": 3,
    "Unknown": 9
}

# Date validation regex pattern (MM/DD/YYYY)
date_pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$'

# Function to validate date format
def validate_date(date_str):
    if not date_str or not isinstance(date_str, str):
        return False
    return bool(re.match(date_pattern, date_str))

# Function to validate and format zip code
def validate_zip(zip_str):
    if not zip_str or not isinstance(zip_str, str):
        return ""
    # Remove any non-digit characters
    zip_clean = re.sub(r'\D', '', zip_str)
    if len(zip_clean) == 5:
        return zip_clean + "0000"  # Append 0000 to make it 9 digits
    elif len(zip_clean) == 9:
        return zip_clean
    else:
        return ""  # Invalid zip format

# Initialize session state for storing dataframes and navigation
if 'clients_df' not in st.session_state:
    st.session_state.clients_df = pd.DataFrame()
if 'admissions_df' not in st.session_state:
    st.session_state.admissions_df = pd.DataFrame()
if 'survey_df' not in st.session_state:
    st.session_state.survey_df = pd.DataFrame()
if 'discharges_df' not in st.session_state:
    st.session_state.discharges_df = pd.DataFrame()
if 'page' not in st.session_state:
    st.session_state.page = "Data Ingestion"

# Sidebar for navigation
st.sidebar.title("Client Data Management")
st.sidebar.markdown("Navigate through the application using the options below.")

# Navigation options
page = st.sidebar.radio(
    "Go to",
    ["Data Ingestion", "Data Table", "Record Creation", "Data Export"],
    key="sidebar_navigation"
)
st.session_state.page = page

# Display data stats in sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("Data Statistics")
st.sidebar.markdown(f"**Clients:** {len(st.session_state.clients_df)} records")
st.sidebar.markdown(f"**Admissions:** {len(st.session_state.admissions_df)} records")
st.sidebar.markdown(f"**Surveys:** {len(st.session_state.survey_df)} records")
st.sidebar.markdown(f"**Discharges:** {len(st.session_state.discharges_df)} records")

# Main content area
st.title("Client Data Management App")
st.markdown("A tool to manage client, admission, survey, and discharge records.")

# Conditional display based on navigation
if st.session_state.page == "Data Ingestion":
    # Data Ingestion Section
    st.header("Data Ingestion")
    st.markdown("Upload a CSV file or paste TSV data below to get started.")
    
    # File uploader for CSV
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
    # Text area for TSV input
    tsv_text = st.text_area("Or paste TSV text here")

# Define field mapping dictionary for standardization outside of any conditional blocks
field_mapping = {
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

# Data Ingestion processing logic
if st.session_state.page == "Data Ingestion":
    # Process the uploaded data
    if uploaded_file is not None:
        try:
            clients_df = pd.read_csv(uploaded_file, delimiter=',')
            # Normalize column names
            clients_df.columns = [col.strip().lower() for col in clients_df.columns]
            # Apply field mapping
            clients_df = clients_df.rename(columns=field_mapping)
            # Handle missing fields
            for required_field in ["ProviderClientId", "FirstName", "LastName", "DateofBirth", "Gender", "ZipCode"]:
                if required_field not in clients_df.columns:
                    clients_df[required_field] = ""
            
            st.success(f"CSV file successfully loaded with {len(clients_df)} records.")
            st.session_state.clients_df = clients_df
        except Exception as e:
            st.error(f"Error loading CSV file: {e}")

    # Process the TSV text input
    if tsv_text:
        try:
            clients_df = pd.read_csv(StringIO(tsv_text), delimiter='\t')
            # Normalize column names
            clients_df.columns = [col.strip().lower() for col in clients_df.columns]
            # Apply field mapping
            clients_df = clients_df.rename(columns=field_mapping)
            # Handle missing fields
            for required_field in ["ProviderClientId", "FirstName", "LastName", "DateofBirth", "Gender", "ZipCode"]:
                if required_field not in clients_df.columns:
                    clients_df[required_field] = ""
            
            st.success(f"TSV data successfully loaded with {len(clients_df)} records.")
            st.session_state.clients_df = clients_df
        except Exception as e:
            st.error(f"Error parsing TSV data: {e}")

# Data Table Section
if st.session_state.page == "Data Table":
    st.header("Client Data Table")
    st.markdown("Edit client data below. Changes will be automatically saved.")
    
    if not st.session_state.clients_df.empty:
        # Configure column options for the data editor
        column_config = {
            "ProviderClientId": st.column_config.TextColumn(
                "Provider Client ID",
                help="Unique identifier for the client",
                required=True
            ),
            "FirstName": st.column_config.TextColumn(
                "First Name",
                help="Client's first name",
                required=True
            ),
            "LastName": st.column_config.TextColumn(
                "Last Name",
                help="Client's last name",
                required=True
            ),
            "DateofBirth": st.column_config.TextColumn(
                "Date of Birth",
                help="Format: MM/DD/YYYY",
                required=True
            ),
            "Gender": st.column_config.SelectboxColumn(
                "Gender",
                help="Select client's gender",
                options=list(gender_options.keys()),
                required=True
            ),
            "ZipCode": st.column_config.TextColumn(
                "Zip Code",
                help="5-digit zip code (will be formatted to 9 digits)",
                required=False
            )
        }
        
        # Create the data editor
        edited_df = st.data_editor(
            st.session_state.clients_df,
            column_config=column_config,
            num_rows="dynamic",
            use_container_width=True,
            hide_index=True
        )
        
        # Validate and update the edited dataframe
        if edited_df is not None and not edited_df.empty:
            # Validate DateofBirth format
            invalid_dates = []
            for idx, row in edited_df.iterrows():
                if not validate_date(row.get('DateofBirth', '')):
                    invalid_dates.append(idx)
            
            if invalid_dates:
                st.error(f"Invalid date format detected in {len(invalid_dates)} rows. Please use MM/DD/YYYY format.")
            
            # Format ZipCode
            edited_df['ZipCode'] = edited_df['ZipCode'].apply(validate_zip)
            
            # Update session state with validated data
            st.session_state.clients_df = edited_df
    else:
        st.info("No client data loaded. Please go to the Data Ingestion page to upload data.")

# Record Creation Section
if st.session_state.page == "Record Creation":
    st.header("Record Creation")
    
    # Only show record creation if clients data is available
    if not st.session_state.clients_df.empty:
        # Select client for record creation
        client_ids = st.session_state.clients_df["ProviderClientId"].tolist()
        selected_client_id = st.selectbox("Select a Client", client_ids)
    
    # Get the selected client data
    selected_client = st.session_state.clients_df[st.session_state.clients_df["ProviderClientId"] == selected_client_id].iloc[0]
    
    # Display selected client info
    st.markdown(f"**Selected Client:** {selected_client['FirstName']} {selected_client['LastName']}")
    
    # Record type selection
    record_type = st.radio("Create Record Type", ["Client+Admission+Survey", "Discharge"])
    
    if record_type == "Client+Admission+Survey":
        # Form for admission data
        with st.form("admission_form"):
            st.subheader("Admission Information")
            
            # Date fields
            admission_date = st.date_input("Admission Date", datetime.now())
            formatted_admission_date = admission_date.strftime("%m/%d/%Y")
            
            # Generate ProviderAdmissionId (e.g., LastF20230101 from client last name and admission date)
            last_initial = selected_client['LastName'][0] if selected_client['LastName'] else 'X'
            first_initial = selected_client['FirstName'][0] if selected_client['FirstName'] else 'X'
            admission_date_str = admission_date.strftime("%Y%m%d")
            provider_admission_id = f"{selected_client['LastName'][:4]}{first_initial}{admission_date_str}"
            
            st.text_input("Provider Admission ID", provider_admission_id, disabled=True)
            
            # Survey JSON input
            survey_json = st.text_area("Paste Survey JSON")
            
            # Submit button
            submitted = st.form_submit_button("Create Admission and Survey Records")
            
            if submitted:
                try:
                    # Validate JSON
                    if survey_json:
                        survey_data = json.loads(survey_json)
                        
                        # Check for required fields in survey
                        required_fields = ["Q1", "Q2", "Q3"]
                        missing_fields = [field for field in required_fields if field not in survey_data]
                        
                        if missing_fields:
                            st.error(f"Missing required fields in survey JSON: {', '.join(missing_fields)}")
                        else:
                            # Create admission record
                            admission_record = pd.DataFrame({
                                "ProviderClientId": [selected_client_id],
                                "ProviderAdmissionId": [provider_admission_id],
                                "AdmissionDate": [formatted_admission_date],
                                "ProviderId": [PROVIDERID],
                                "ProviderLocationId": [PROVIDERLOCATIONID]
                            })
                            
                            # Create survey record
                            survey_record = pd.DataFrame({
                                "ProviderClientId": [selected_client_id],
                                "ProviderAdmissionId": [provider_admission_id],
                                **{k: [v] for k, v in survey_data.items()}
                            })
                            
                            # Add to session state
                            if st.session_state.admissions_df.empty:
                                st.session_state.admissions_df = admission_record
                            else:
                                st.session_state.admissions_df = pd.concat([st.session_state.admissions_df, admission_record], ignore_index=True)
                            
                            if st.session_state.survey_df.empty:
                                st.session_state.survey_df = survey_record
                            else:
                                st.session_state.survey_df = pd.concat([st.session_state.survey_df, survey_record], ignore_index=True)
                            
                            st.success("Admission and Survey records created successfully!")
                    else:
                        st.error("Survey JSON is required")
                except json.JSONDecodeError:
                    st.error("Invalid JSON format. Please check your input.")
                except Exception as e:
                    st.error(f"Error creating records: {e}")
    
    else:  # Discharge record
        with st.form("discharge_form"):
            st.subheader("Discharge Information")
            
            # Get admission IDs for this client
            if not st.session_state.admissions_df.empty:
                client_admissions = st.session_state.admissions_df[
                    st.session_state.admissions_df["ProviderClientId"] == selected_client_id
                ]
                
                if not client_admissions.empty:
                    admission_ids = client_admissions["ProviderAdmissionId"].tolist()
                    selected_admission_id = st.selectbox("Select Admission", admission_ids)
                    
                    # Date fields
                    discharge_date = st.date_input("Discharge Date", datetime.now())
                    formatted_discharge_date = discharge_date.strftime("%m/%d/%Y")
                    
                    # Submit button
                    submitted = st.form_submit_button("Create Discharge Record")
                    
                    if submitted:
                        try:
                            # Create discharge record
                            discharge_record = pd.DataFrame({
                                "ProviderClientId": [selected_client_id],
                                "ProviderAdmissionId": [selected_admission_id],
                                "DischargeDate": [formatted_discharge_date],
                                "ProviderId": [PROVIDERID],
                                "ProviderLocationId": [PROVIDERLOCATIONID]
                            })
                            
                            # Add to session state
                            if st.session_state.discharges_df.empty:
                                st.session_state.discharges_df = discharge_record
                            else:
                                st.session_state.discharges_df = pd.concat([st.session_state.discharges_df, discharge_record], ignore_index=True)
                            
                            st.success("Discharge record created successfully!")
                        except Exception as e:
                            st.error(f"Error creating discharge record: {e}")
                else:
                    st.error("No admissions found for this client. Create an admission record first.")
            else:
                st.error("No admissions found. Create an admission record first.")
else:
    st.info("Please load client data first to create records.")

# Data Export Section
if st.session_state.page == "Data Export":
    st.header("Data Export")
    st.markdown("Download your data as CSV files.")
    
    # Create columns for download buttons
    col1, col2, col3, col4 = st.columns(4)
    
    # Client data export
    with col1:
        if not st.session_state.clients_df.empty:
            st.download_button(
                label="Download Clients",
                data=st.session_state.clients_df.to_csv(index=False),
                file_name="clients.csv",
                mime="text/csv"
            )
        else:
            st.button("Download Clients", disabled=True)
            st.caption("No client data available")
    
    # Admissions data export
    with col2:
        if not st.session_state.admissions_df.empty:
            st.download_button(
                label="Download Admissions",
                data=st.session_state.admissions_df.to_csv(index=False),
                file_name="admissions.csv",
                mime="text/csv"
            )
        else:
            st.button("Download Admissions", disabled=True)
            st.caption("No admission data available")
    
    # Survey data export
    with col3:
        if not st.session_state.survey_df.empty:
            st.download_button(
                label="Download Surveys",
                data=st.session_state.survey_df.to_csv(index=False),
                file_name="surveys.csv",
                mime="text/csv"
            )
        else:
            st.button("Download Surveys", disabled=True)
            st.caption("No survey data available")
    
    # Discharges data export
    with col4:
        if not st.session_state.discharges_df.empty:
            st.download_button(
                label="Download Discharges",
                data=st.session_state.discharges_df.to_csv(index=False),
                file_name="discharges.csv",
                mime="text/csv"
            )
        else:
            st.button("Download Discharges", disabled=True)
            st.caption("No discharge data available")

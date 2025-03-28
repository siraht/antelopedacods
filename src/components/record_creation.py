"""
Record creation component for creating new client records.
"""
import streamlit as st
import pandas as pd
from datetime import datetime
from src.config import GENDER_OPTIONS, PROVIDERID, PROVIDERLOCATIONID
from src.data_models import validate_date, validate_zip, generate_admission_id
from src.survey_config import ADMISSION_SURVEY_QUESTIONS
from src.utils.survey_engine import SurveyEngine

def show_record_creation_page():
    """Display and handle the record creation UI."""
    st.header("Record Creation")
    
    if not st.session_state.clients_df.empty:
        # Create tabs for different record creation workflows
        tab1, tab2 = st.tabs(["Create Client+Admission+Survey", "Create Discharge"])
        
        # Initialize DataFrames if not exist
        if "admissions_df" not in st.session_state:
            st.session_state.admissions_df = pd.DataFrame(columns=[
                "ProviderId", "ProviderClientId", "ProviderAdmissionId", "ProviderLocationId",
                "AdmissionDate", "AdmissionType", "ServiceLevel", "ServiceCode", 
                "DefaultPayerAccountID", "ReferralNumber", "PrimaryClinicianName", "FirstContactDate"
            ])
            
        if "discharges_df" not in st.session_state:
            st.session_state.discharges_df = pd.DataFrame(columns=[
                "ProviderId", "ProviderClientId", "ProviderAdmissionId", "DischargeDate",
                "DischargeReason", "DischargeStatus"
            ])
        
        # Create Client+Admission+Survey tab
        with tab1:
            show_client_admission_survey_form()
            
        # Create Discharge tab
        with tab2:
            show_discharge_form()
    else:
        st.info("Please load client data first to create records.")

def show_client_admission_survey_form():
    """Display and handle the client+admission+survey form."""
    # Initialize session state for selected client
    if 'selected_client_id' not in st.session_state:
        st.session_state.selected_client_id = None
        st.session_state.selected_client_data = None
    
    # Initialize session state for survey answers if not exists
    if 'survey_answers' not in st.session_state:
        st.session_state.survey_answers = {}
    
    # Add radio button to choose between new client and existing client
    client_type = st.radio("Select Client Type", ["New Client", "Existing Client"], key="client_type")
    
    # Handle client selection/input before the form
    if client_type == "Existing Client":
        if not st.session_state.clients_df.empty:
            # Create client options with name first
            client_options_dict = {}
            for _, row in st.session_state.clients_df.iterrows():
                display_name = f"{row['FirstName']} {row['LastName']} (ID: {row['ProviderClientId']})"
                client_options_dict[display_name] = row['ProviderClientId']
            
            # Create sorted list of options
            client_options = sorted(client_options_dict.keys())
            
            # Add empty option at the beginning
            client_options = ["Select a client..."] + client_options
            
            # Show dropdown to select existing client
            selected_client = st.selectbox("Select Client", client_options, key="client_selector")
            
            if selected_client != "Select a client...":
                # Extract client ID from the dictionary using the display name
                client_id = client_options_dict[selected_client]
                if client_id != st.session_state.selected_client_id:
                    # Update session state with new selection
                    st.session_state.selected_client_id = client_id
                    st.session_state.selected_client_data = st.session_state.clients_df[
                        st.session_state.clients_df['ProviderClientId'] == client_id
                    ].iloc[0].to_dict()
            else:
                st.session_state.selected_client_id = None
                st.session_state.selected_client_data = None
        else:
            st.error("No existing clients found. Please create a new client.")
            return
    else:
        # Reset selected client when switching to new client
        st.session_state.selected_client_id = None
        st.session_state.selected_client_data = None
    
    # Create tabs for basic info and detailed survey
    tab1, tab2 = st.tabs(["Basic Information", "Admission Survey"])
    
    with tab1:
        with st.form("client_admission_form"):
            st.subheader("Create Admission")
            
            # Client information
            st.markdown("#### Client Information")
            
            if client_type == "Existing Client" and st.session_state.selected_client_data:
                # Display client details
                client_data = st.session_state.selected_client_data
                st.markdown(f"**Provider Client ID:** {client_data['ProviderClientId']}")
                st.markdown(f"**Name:** {client_data['FirstName']} {client_data['LastName']}")
                st.markdown(f"**Date of Birth:** {client_data['DateofBirth']}")
                st.markdown(f"**Gender:** {client_data['Gender']}")
                st.markdown(f"**Zip Code:** {client_data['ZipCode']}")
                
                # Store values for form processing
                client_id = client_data['ProviderClientId']
                first_name = client_data['FirstName']
                last_name = client_data['LastName']
                date_of_birth = client_data['DateofBirth']
                gender = client_data['Gender']
                zip_code = client_data['ZipCode']
            else:
                # Show form fields for new client
                col1, col2 = st.columns(2)
                with col1:
                    client_id = st.text_input("Provider Client ID", help="Unique identifier for the client")
                    first_name = st.text_input("First Name")
                    date_of_birth = st.text_input("Date of Birth (MM/DD/YYYY)")
                with col2:
                    last_name = st.text_input("Last Name")
                    gender = st.selectbox("Gender", options=list(GENDER_OPTIONS.keys()))
                    zip_code = st.text_input("Zip Code")
            
            # Admission information
            st.markdown("#### Admission Information")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                # Get admission date from client data if available
                default_admission_date = ""
                if client_type == "Existing Client" and st.session_state.selected_client_data:
                    client_id = st.session_state.selected_client_data['ProviderClientId']
                    
                    # Check directly in the selected client data first
                    if 'AdmissionDate' in st.session_state.selected_client_data:
                        default_admission_date = st.session_state.selected_client_data['AdmissionDate']
                    
                    # If not found, try to get admission date from admissions DataFrame
                    elif 'admissions_df' in st.session_state and not st.session_state.admissions_df.empty:
                        # Force client ID to string for comparison
                        # Use the isin method for more reliable matching
                        mask = st.session_state.admissions_df['ProviderClientId'].astype(str).isin([str(client_id)])
                        client_admissions = st.session_state.admissions_df[mask]
                        
                        if not client_admissions.empty and 'AdmissionDate' in client_admissions.columns:
                            # Sort by admission date to get the most recent
                            try:
                                # Try to convert to datetime for sorting
                                client_admissions['AdmissionDateSort'] = pd.to_datetime(client_admissions['AdmissionDate'], errors='coerce')
                                client_admissions = client_admissions.sort_values('AdmissionDateSort', ascending=False)
                            except:
                                # If conversion fails, just use the last row
                                pass
                                
                            # Get admission date from the most recent record
                            default_admission_date = client_admissions.iloc[0]['AdmissionDate']
                
                # First contact date (default to admission date)
                admission_date = st.text_input("Admission Date (MM/DD/YYYY)", value=default_admission_date)
                first_contact_date = st.text_input("First Contact Date (MM/DD/YYYY)", value=default_admission_date)
                admission_type = st.selectbox("Admission Type", options=["New", "Transfer", "Readmission"])
                
            with col2:
                # Import service code mapping from config
                from src.config import SERVICE_CODE_MAPPING, DEFAULT_SERVICE_LEVEL, DEFAULT_PAYER_ACCOUNT_ID
                
                # Service level dropdown (OP or IOP)
                service_level = st.selectbox(
                    "Service Level", 
                    options=list(SERVICE_CODE_MAPPING.keys()),
                    index=list(SERVICE_CODE_MAPPING.keys()).index(DEFAULT_SERVICE_LEVEL) if DEFAULT_SERVICE_LEVEL in SERVICE_CODE_MAPPING else 0
                )
                
                # Payer account ID
                payer_account_id = st.text_input("Payer Account ID", value=DEFAULT_PAYER_ACCOUNT_ID)
                referral_number = st.text_input("Referral Number (Optional)")
                
            with col3:
                # Import default clinician from config
                from src.config import DEFAULT_PRIMARY_CLINICIAN
                
                # Primary clinician
                primary_clinician = st.text_input("Primary Clinician", value=DEFAULT_PRIMARY_CLINICIAN)
            

            
            submit_button = st.form_submit_button("Create Basic Records")
            
            if submit_button:
                if not validate_date(admission_date):
                    st.error("Please enter a valid admission date in MM/DD/YYYY format.")
                    return
                    
                # Only validate date of birth for new clients
                if client_type == "New Client":
                    if not validate_date(date_of_birth):
                        st.error("Please enter a valid date of birth in MM/DD/YYYY format.")
                        return
                        
                    # Create client record
                    new_client = {
                        "ProviderClientId": client_id,
                        "FirstName": first_name,
                        "LastName": last_name,
                        "DateofBirth": date_of_birth,
                        "Gender": gender,
                        "ZipCode": validate_zip(zip_code)
                    }
                
                # Generate admission ID with client name and admission date
                admission_id = generate_admission_id(client_id, first_name, last_name, admission_date)
                
                # Create admission record with all required fields
                new_admission = {
                    "ProviderId": PROVIDERID,
                    "ProviderClientId": client_id,
                    "ProviderAdmissionId": admission_id,
                    "ProviderLocationId": PROVIDERLOCATIONID,
                    "AdmissionDate": admission_date,
                    "AdmissionType": admission_type,
                    "ServiceLevel": service_level,
                    "ServiceCode": SERVICE_CODE_MAPPING.get(service_level),
                    "DefaultPayerAccountID": payer_account_id,
                    "ReferralNumber": referral_number,
                    "PrimaryClinicianName": primary_clinician,
                    "FirstContactDate": first_contact_date
                }
                
                # Add records to DataFrames
                if client_type == "New Client":
                    st.session_state.clients_df = pd.concat([st.session_state.clients_df, pd.DataFrame([new_client])], ignore_index=True)
                
                st.session_state.admissions_df = pd.concat([st.session_state.admissions_df, pd.DataFrame([new_admission])], ignore_index=True)
                
                # Store admission ID in session state for survey tab
                st.session_state.current_admission_id = admission_id
                st.session_state.current_client_id = client_id
                
                if client_type == "New Client":
                    st.success(f"Successfully created client and admission records for {first_name} {last_name}. Please complete the admission survey.")
                else:
                    st.success(f"Successfully created admission record for {first_name} {last_name}. Please complete the admission survey.")
                
                # Switch to survey tab
                st.query_params.update(active_tab="Admission Survey")
    
    with tab2:
        st.subheader("Admission Survey Questions")
        
        # Check if we have a current admission to work with
        if hasattr(st.session_state, 'current_admission_id') and st.session_state.current_admission_id:
            admission_id = st.session_state.current_admission_id
            client_id = st.session_state.current_client_id
            
            # Display current admission ID
            st.info(f"Completing survey for Admission ID: {admission_id}")
            
            # Create survey engine with the questions
            survey_engine = SurveyEngine(ADMISSION_SURVEY_QUESTIONS)
            
            # Load existing answers if any
            if 'survey_answers' in st.session_state and admission_id in st.session_state.survey_answers:
                survey_engine.answers = st.session_state.survey_answers[admission_id]
            
            # Create tabs for different sections
            survey_form_tab, survey_data_tab, export_tab = st.tabs(["Survey Form", "Import/Export", "All Survey Data"])
            
            # Survey data tab
            with survey_data_tab:
                # Two columns for import and export
                import_col, export_col = st.columns(2)
                
                # Import functionality
                with import_col:
                    st.subheader("Import JSON Data")
                    json_input = st.text_area("Paste JSON survey data here", height=200,
                                            help="Paste a JSON object with question sequence numbers as keys and answers as values.")
                    import_button = st.button("Import Data")
                    
                    if import_button and json_input:
                        success, message = survey_engine.import_json_answers(json_input)
                        if success:
                            st.success(message)
                            # Update session state with imported answers
                            if 'survey_answers' not in st.session_state:
                                st.session_state.survey_answers = {}
                            st.session_state.survey_answers[admission_id] = survey_engine.answers
                        else:
                            st.error(message)
                
                # Export functionality
                with export_col:
                    st.subheader("Export Current Data")
                    if survey_engine.answers:
                        # JSON export for individual survey
                        export_json = survey_engine.export_answers_as_json()
                        st.code(export_json, language="json")
                        st.download_button(
                            label="Download JSON",
                            data=export_json,
                            file_name=f"survey_answers_{admission_id}.json",
                            mime="application/json"
                        )
                        
                        # CSV export for all survey data
                        if 'survey_df' in st.session_state and not st.session_state.survey_df.empty:
                            csv_data = st.session_state.survey_df.to_csv(index=False)
                            st.download_button(
                                label="Download All Survey Data (CSV)",
                                data=csv_data,
                                file_name="survey_data.csv",
                                mime="text/csv"
                            )
                    else:
                        st.info("No survey data available to export.")
            
            # Export all data tab
            with export_tab:
                st.subheader("Export All Survey Data")
                
                # Show all survey data
                if 'survey_df' in st.session_state and not st.session_state.survey_df.empty:
                    st.write(f"Total survey records: {len(st.session_state.survey_df)}")
                    st.dataframe(st.session_state.survey_df)
                    
                    # Export all survey data
                    csv_data = st.session_state.survey_df.to_csv(index=False)
                    st.download_button(
                        label="Download All Survey Data (CSV)",
                        data=csv_data,
                        file_name="all_survey_data.csv",
                        mime="text/csv",
                        key="download_all_survey_data"
                    )
                    
                    # Add a button to clear all survey data
                    if st.button("Clear All Survey Data"):
                        st.session_state.survey_df = pd.DataFrame()
                        st.success("All survey data cleared.")
                        st.rerun()
                else:
                    st.info("No survey data available to export.")
            
            # Survey form tab
            with survey_form_tab:
                # Create form for survey
                with st.form("admission_survey_form"):
                    # Render the survey questions
                    survey_engine.render_survey_form()
                    
                    # Add submit button at the end of the form
                    submit_survey = st.form_submit_button("Submit Survey")
                
                # Check if form was submitted
                if submit_survey:
                    # Validate all answers
                    if survey_engine.validate_all():
                        # Clear any previous error messages
                        if 'validation_errors' in st.session_state:
                            del st.session_state.validation_errors
                        # Get formatted answers
                        formatted_answers = survey_engine.get_formatted_answers()
                        
                        # Store answers in session state
                        if 'survey_answers' not in st.session_state:
                            st.session_state.survey_answers = {}
                        
                        st.session_state.survey_answers[admission_id] = formatted_answers
                        
                        # Create survey answers dataframe in the correct format (one row per question)
                        survey_rows = []
                        
                        for seq_num, value in formatted_answers.items():
                            # Skip empty answers
                            if value == "":
                                continue
                                
                            survey_row = {
                                "RecordType": "SurAns",
                                "ProviderId": PROVIDERID,
                                "ProviderClientId": client_id,
                                "ProviderAdmissionId": admission_id,
                                "QuestionGroupId": "1",  # 1 for Admission
                                "ExportSequenceNumber": seq_num,
                                "AnswerValue": value
                            }
                            survey_rows.append(survey_row)
                        
                        # Add to survey dataframe
                        if 'survey_df' not in st.session_state:
                            st.session_state.survey_df = pd.DataFrame()
                        
                        if survey_rows:  # Only add if there are answers
                            st.session_state.survey_df = pd.concat([
                                st.session_state.survey_df, 
                                pd.DataFrame(survey_rows)
                            ], ignore_index=True)
                        
                        # Show success message with count of questions answered
                        st.success(f"Successfully saved {len(survey_rows)} survey answers.")
                        
                        # Display the survey data
                        if 'survey_df' in st.session_state and not st.session_state.survey_df.empty:
                            with st.expander("View Saved Survey Data"):
                                # Filter to show only this admission's data
                                admission_data = st.session_state.survey_df[
                                    st.session_state.survey_df["ProviderAdmissionId"] == admission_id
                                ]
                                if not admission_data.empty:
                                    st.dataframe(admission_data)
                    else:
                        # Show all validation errors
                        st.error("Please correct the following errors:")
                        for seq_num, error_msg in survey_engine.errors.items():
                            question = next((q for q in survey_engine.questions if q["sequence_number"] == seq_num), None)
                            if question:
                                st.error(f"Question {seq_num} ({question['question_text']}): {error_msg}")
        else:
            st.warning("Please create an admission record first in the Basic Information tab.")

def show_discharge_form():
    """Display and handle the discharge form."""
    with st.form("discharge_form"):
        st.subheader("Create Discharge Record")
        
        # If admissions exist, create a dropdown to select one
        if not st.session_state.admissions_df.empty:
            # Prepare options for the dropdown
            admission_options = []
            for _, row in st.session_state.admissions_df.iterrows():
                client_id = row["ProviderClientId"]
                admission_id = row["ProviderAdmissionId"]
                admission_date = row["AdmissionDate"]
                
                # Find client name
                client_name = "Unknown"
                client_row = st.session_state.clients_df[st.session_state.clients_df["ProviderClientId"] == client_id]
                if not client_row.empty:
                    first_name = client_row.iloc[0]["FirstName"]
                    last_name = client_row.iloc[0]["LastName"]
                    client_name = f"{first_name} {last_name}"
                
                option_text = f"{client_name} - {admission_id} - {admission_date}"
                admission_options.append({"text": option_text, "admission_id": admission_id, "client_id": client_id})
            
            selected_admission = st.selectbox(
                "Select Admission to Discharge",
                options=range(len(admission_options)),
                format_func=lambda x: admission_options[x]["text"]
            )
            
            discharge_date = st.text_input("Discharge Date (MM/DD/YYYY)")
            discharge_reason = st.selectbox("Discharge Reason", options=[
                "Completed Treatment", "Left Against Advice", "Terminated", "Transferred", "Other"
            ])
            discharge_status = st.selectbox("Discharge Status", options=[
                "Successful", "Unsuccessful"
            ])
            
            submit_button = st.form_submit_button("Create Discharge Record")
            
            if submit_button:
                if not validate_date(discharge_date):
                    st.error("Please enter a valid discharge date in MM/DD/YYYY format.")
                    return
                
                selected = admission_options[selected_admission]
                
                # Create discharge record
                new_discharge = {
                    "ProviderId": PROVIDERID,
                    "ProviderClientId": selected["client_id"],
                    "ProviderAdmissionId": selected["admission_id"],
                    "DischargeDate": discharge_date,
                    "DischargeReason": discharge_reason,
                    "DischargeStatus": discharge_status
                }
                
                # Add record to DataFrame
                st.session_state.discharges_df = pd.concat([st.session_state.discharges_df, pd.DataFrame([new_discharge])], ignore_index=True)
                
                st.success("Successfully created discharge record.")
        else:
            st.info("No admissions available. Please create an admission record first.")

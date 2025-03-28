"""
Record creation component for creating new client records.
"""
import streamlit as st
import pandas as pd
from datetime import datetime
from src.config import GENDER_OPTIONS, PROVIDERID, PROVIDERLOCATIONID
from src.data_models import validate_date, validate_zip, generate_admission_id

def show_record_creation_page():
    """Display and handle the record creation UI."""
    st.header("Record Creation")
    
    if not st.session_state.clients_df.empty:
        # Create tabs for different record creation workflows
        tab1, tab2 = st.tabs(["Create Client+Admission+Survey", "Create Discharge"])
        
        # Initialize DataFrames if not exist
        if "admissions_df" not in st.session_state:
            st.session_state.admissions_df = pd.DataFrame(columns=[
                "ProviderId", "ProviderClientId", "ProviderAdmissionId", "AdmissionDate", 
                "AdmissionType", "ProviderLocationId"
            ])
            
        if "survey_df" not in st.session_state:
            st.session_state.survey_df = pd.DataFrame(columns=[
                "ProviderId", "ProviderClientId", "ProviderAdmissionId", "SurveyDate",
                "Housing", "Employment", "Alcohol", "Drug", "Legal", "Family", "Medical", "MentalHealth"
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
    with st.form("client_admission_form"):
        st.subheader("Create Client with Admission and Survey")
        
        # Client information
        st.markdown("#### Client Information")
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
        col1, col2 = st.columns(2)
        
        with col1:
            admission_date = st.text_input("Admission Date (MM/DD/YYYY)")
            admission_type = st.selectbox("Admission Type", options=["New", "Transfer", "Readmission"])
        
        # Survey information
        st.markdown("#### Survey Information")
        col1, col2 = st.columns(2)
        
        with col1:
            housing = st.selectbox("Housing", options=["No Issue", "Minor Issue", "Moderate Issue", "Severe Issue"])
            employment = st.selectbox("Employment", options=["No Issue", "Minor Issue", "Moderate Issue", "Severe Issue"])
            alcohol = st.selectbox("Alcohol", options=["No Issue", "Minor Issue", "Moderate Issue", "Severe Issue"])
            drug = st.selectbox("Drug", options=["No Issue", "Minor Issue", "Moderate Issue", "Severe Issue"])
        
        with col2:
            legal = st.selectbox("Legal", options=["No Issue", "Minor Issue", "Moderate Issue", "Severe Issue"])
            family = st.selectbox("Family", options=["No Issue", "Minor Issue", "Moderate Issue", "Severe Issue"])
            medical = st.selectbox("Medical", options=["No Issue", "Minor Issue", "Moderate Issue", "Severe Issue"])
            mental_health = st.selectbox("Mental Health", options=["No Issue", "Minor Issue", "Moderate Issue", "Severe Issue"])
        
        submit_button = st.form_submit_button("Create Records")
        
        if submit_button:
            if not validate_date(date_of_birth) or not validate_date(admission_date):
                st.error("Please enter valid dates in MM/DD/YYYY format.")
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
            
            # Generate admission ID
            admission_id = f"{client_id}A{datetime.now().strftime('%Y%m%d')}"
            
            # Create admission record
            new_admission = {
                "ProviderId": PROVIDERID,
                "ProviderClientId": client_id,
                "ProviderAdmissionId": admission_id,
                "AdmissionDate": admission_date,
                "AdmissionType": admission_type,
                "ProviderLocationId": PROVIDERLOCATIONID
            }
            
            # Create survey record
            new_survey = {
                "ProviderId": PROVIDERID,
                "ProviderClientId": client_id,
                "ProviderAdmissionId": admission_id,
                "SurveyDate": admission_date,
                "Housing": housing,
                "Employment": employment,
                "Alcohol": alcohol,
                "Drug": drug,
                "Legal": legal,
                "Family": family,
                "Medical": medical,
                "MentalHealth": mental_health
            }
            
            # Add records to DataFrames
            st.session_state.clients_df = pd.concat([st.session_state.clients_df, pd.DataFrame([new_client])], ignore_index=True)
            st.session_state.admissions_df = pd.concat([st.session_state.admissions_df, pd.DataFrame([new_admission])], ignore_index=True)
            st.session_state.survey_df = pd.concat([st.session_state.survey_df, pd.DataFrame([new_survey])], ignore_index=True)
            
            st.success(f"Successfully created client, admission, and survey records for {first_name} {last_name}.")

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

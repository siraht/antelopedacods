"""
Data export component for downloading client data as CSV files.
"""
import streamlit as st

def format_admissions_for_export():
    """
    Format admissions data for export according to the required specifications.
    
    Returns:
        pd.DataFrame: Formatted admissions dataframe ready for export
    """
    import pandas as pd
    from datetime import datetime
    from src.config import (
        PROVIDERID, PROVIDERLOCATIONID, SERVICE_CODE_MAPPING,
        DEFAULT_SERVICE_LEVEL, DEFAULT_PAYER_ACCOUNT_ID, DEFAULT_PRIMARY_CLINICIAN
    )
    
    # Create a copy of the admissions dataframe
    admissions_df = st.session_state.admissions_df.copy()
    
    # Create a new dataframe with the required fields
    export_data = {
        "RecordType": ["Admission"] * len(admissions_df),
        "ProviderId": admissions_df["ProviderId"],
        "ProviderClientId": admissions_df["ProviderClientId"],
        "ProviderAdmissionId": admissions_df["ProviderAdmissionId"],
        "ProviderLocationId": admissions_df["ProviderLocationId"]
    }
    
    # Add ServiceCode - use the one from the record if available, otherwise use mapping
    if "ServiceCode" in admissions_df.columns:
        export_data["ServiceCode"] = admissions_df["ServiceCode"]
    elif "ServiceLevel" in admissions_df.columns:
        # Map service level to service code
        export_data["ServiceCode"] = admissions_df["ServiceLevel"].apply(
            lambda x: SERVICE_CODE_MAPPING.get(x, SERVICE_CODE_MAPPING.get(DEFAULT_SERVICE_LEVEL, ""))
        )
    else:
        export_data["ServiceCode"] = [SERVICE_CODE_MAPPING.get(DEFAULT_SERVICE_LEVEL, "")] * len(admissions_df)
    
    # Add DefaultPayerAccountID
    if "DefaultPayerAccountID" in admissions_df.columns:
        export_data["DefaultPayerAccountID"] = admissions_df["DefaultPayerAccountID"]
    else:
        export_data["DefaultPayerAccountID"] = [DEFAULT_PAYER_ACCOUNT_ID] * len(admissions_df)
    
    # Add ReferralNumber
    if "ReferralNumber" in admissions_df.columns:
        export_data["ReferralNumber"] = admissions_df["ReferralNumber"]
    else:
        export_data["ReferralNumber"] = [""] * len(admissions_df)
    
    # Add AdmissionDate
    export_data["AdmissionDate"] = admissions_df["AdmissionDate"]
    
    # Add PrimaryClinicianName
    if "PrimaryClinicianName" in admissions_df.columns:
        export_data["PrimaryClinicianName"] = admissions_df["PrimaryClinicianName"]
    else:
        export_data["PrimaryClinicianName"] = [DEFAULT_PRIMARY_CLINICIAN] * len(admissions_df)
    
    # Add FirstContactDate
    if "FirstContactDate" in admissions_df.columns:
        export_data["FirstContactDate"] = admissions_df["FirstContactDate"]
    else:
        export_data["FirstContactDate"] = admissions_df["AdmissionDate"]  # Use admission date as fallback
    
    # Create dataframe from export data
    export_df = pd.DataFrame(export_data)
    
    return export_df

def show_data_export_page():
    """Display and handle the data export UI."""
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
        if "admissions_df" in st.session_state and not st.session_state.admissions_df.empty:
            # Format admissions for export
            export_admissions_df = format_admissions_for_export()
            
            st.download_button(
                label="Download Admissions",
                data=export_admissions_df.to_csv(index=False),
                file_name="admissions.csv",
                mime="text/csv"
            )
        else:
            st.button("Download Admissions", disabled=True)
            st.caption("No admission data available")
    
    # Survey data export
    with col3:
        if "survey_df" in st.session_state and not st.session_state.survey_df.empty:
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
        if "discharges_df" in st.session_state and not st.session_state.discharges_df.empty:
            st.download_button(
                label="Download Discharges",
                data=st.session_state.discharges_df.to_csv(index=False),
                file_name="discharges.csv",
                mime="text/csv"
            )
        else:
            st.button("Download Discharges", disabled=True)
            st.caption("No discharge data available")

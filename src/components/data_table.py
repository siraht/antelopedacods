"""
Data table component for displaying and editing client data.
"""
import streamlit as st
from src.config import GENDER_OPTIONS
from src.data_models import validate_date, validate_zip

def show_data_table_page():
    """Display and handle the data table UI."""
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
                options=list(GENDER_OPTIONS.keys()),
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

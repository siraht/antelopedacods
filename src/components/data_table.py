"""
Data table component for displaying and editing client data.
"""
import streamlit as st
from src.config import GENDER_OPTIONS
from src.data_models import validate_date, validate_zip, format_date

def show_data_table_page():
    """Display and handle the data table UI."""
    st.header("Client Data Table")
    st.markdown("Edit client data below. Changes will be automatically saved.")
    
    if not st.session_state.clients_df.empty:
        # Ensure all columns are string type and handle empty values before displaying
        df_display = st.session_state.clients_df.copy()
        df_display = df_display.fillna('')
        for col in df_display.columns:
            df_display[col] = df_display[col].astype(str).replace('nan', '')
        
        # Configure column options for the data editor
        column_config = {
            "ProviderClientId": st.column_config.TextColumn(
                "Provider Client ID",
                help="Unique identifier for the client",
                required=True,
                default=""
            ),
            "FirstName": st.column_config.TextColumn(
                "First Name",
                help="Client's first name",
                required=True,
                default=""
            ),
            "LastName": st.column_config.TextColumn(
                "Last Name",
                help="Client's last name",
                required=True,
                default=""
            ),
            "DateofBirth": st.column_config.TextColumn(
                "Date of Birth",
                help="Format: MM/DD/YYYY",
                required=True,
                default=""
            ),
            "Gender": st.column_config.SelectboxColumn(
                "Gender",
                help="Select client's gender",
                options=list(GENDER_OPTIONS.keys()),
                required=True,
                default="Unknown"
            ),
            "ZipCode": st.column_config.TextColumn(
                "Zip Code",
                help="5-digit zip code (will be formatted to 9 digits)",
                required=False,
                default=""
            )
        }
        
        # Create the data editor
        edited_df = st.data_editor(
            df_display,
            column_config=column_config,
            num_rows="dynamic",
            use_container_width=True,
            hide_index=True,
            key="client_data_editor"
        )
        
        # Validate and update the edited dataframe
        if edited_df is not None and not edited_df.empty:
            # Format and validate DateofBirth
            invalid_dates = []
            formatted_dates = []
            
            for idx, row in edited_df.iterrows():
                date_str = row.get('DateofBirth', '').strip()
                if not date_str:  # Allow empty dates
                    formatted_dates.append('')
                elif not validate_date(date_str):
                    invalid_dates.append(idx)
                    formatted_dates.append('')
                else:
                    formatted_dates.append(format_date(date_str))
            
            if invalid_dates:
                st.error(f"Invalid date format detected in {len(invalid_dates)} rows. Please use M/DD/YYYY or MM/DD/YYYY format for non-empty dates.")
            
            # Update the dates in the DataFrame
            edited_df['DateofBirth'] = formatted_dates
            
            # Format ZipCode
            edited_df['ZipCode'] = edited_df['ZipCode'].apply(validate_zip)
            
            # Update session state with validated data
            st.session_state.clients_df = edited_df
    else:
        st.info("No client data loaded. Please go to the Data Ingestion page to upload data.")

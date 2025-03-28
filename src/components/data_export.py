"""
Data export component for downloading client data as CSV files.
"""
import streamlit as st

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

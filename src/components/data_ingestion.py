"""
Data ingestion component for uploading and processing client data.
"""
import streamlit as st
import pandas as pd
from src.utils.data_processing import process_csv_data, process_tsv_data

def show_data_ingestion_page():
    """Display and handle the data ingestion UI."""
    st.header("Data Ingestion")
    st.markdown("Upload a CSV file or paste TSV data below to get started.")
    
    # File uploader for CSV
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
    # Text area for TSV input
    tsv_text = st.text_area("Or paste TSV text here")
    
    # Process the uploaded data
    if uploaded_file is not None:
        try:
            # Process the file to get both client and admission data
            clients_df, admissions_df = process_csv_data(uploaded_file)
            
            # Update session state with client data
            st.session_state.clients_df = clients_df
            st.success(f"CSV file successfully loaded with {len(clients_df)} client records.")
            
            # Update session state with admission data if available
            if not admissions_df.empty:
                st.session_state.admissions_df = admissions_df
                st.success(f"Also extracted {len(admissions_df)} admission records from the CSV.")
        except Exception as e:
            st.error(f"Error loading CSV file: {e}")

    # Process the TSV text input
    if tsv_text:
        try:
            # Process the TSV to get both client and admission data
            clients_df, admissions_df = process_tsv_data(tsv_text)
            
            # Update session state with client data
            st.session_state.clients_df = clients_df
            st.success(f"TSV data successfully loaded with {len(clients_df)} client records.")
            
            # Update session state with admission data if available
            if not admissions_df.empty:
                st.session_state.admissions_df = admissions_df
                st.success(f"Also extracted {len(admissions_df)} admission records from the TSV.")
        except Exception as e:
            st.error(f"Error parsing TSV data: {e}")

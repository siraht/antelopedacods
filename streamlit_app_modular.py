import streamlit as st
import pandas as pd

# Import components
from src.components.data_ingestion import show_data_ingestion_page
from src.components.data_table import show_data_table_page
from src.components.record_creation import show_record_creation_page
from src.components.data_export import show_data_export_page

# Set page title and icon
st.set_page_config(
    page_title="Client Data Management App",
    page_icon="📊",
    layout="wide"
)

def init_session_state():
    """Initialize session state variables if they don't exist."""
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

def setup_sidebar():
    """Configure the sidebar navigation and statistics."""
    # Create sidebar for navigation
    st.sidebar.title("Client Data Management")
    st.sidebar.markdown("Navigate through the application using the options below.")
    
    # Navigation options
    page = st.sidebar.radio(
        "Go to",
        ["Data Ingestion", "Data Table", "Record Creation", "Data Export"],
        key="sidebar_navigation"
    )
    
    # Update the current page in session state
    st.session_state.page = page
    
    # Display data stats in sidebar
    st.sidebar.markdown("---")
    st.sidebar.subheader("Data Statistics")
    st.sidebar.markdown(f"**Clients:** {len(st.session_state.clients_df)} records")
    st.sidebar.markdown(f"**Admissions:** {len(st.session_state.admissions_df)} records")
    st.sidebar.markdown(f"**Surveys:** {len(st.session_state.survey_df)} records")
    st.sidebar.markdown(f"**Discharges:** {len(st.session_state.discharges_df)} records")

def main():
    """Main application entry point."""
    # Initialize session state
    init_session_state()
    
    # Configure the sidebar
    setup_sidebar()
    
    # Main app title
    st.title("Client Data Management App")
    st.markdown("A tool to manage client, admission, survey, and discharge records.")
    
    # Display the selected page based on navigation
    if st.session_state.page == "Data Ingestion":
        show_data_ingestion_page()
    elif st.session_state.page == "Data Table":
        show_data_table_page()
    elif st.session_state.page == "Record Creation":
        show_record_creation_page()
    elif st.session_state.page == "Data Export":
        show_data_export_page()

if __name__ == "__main__":
    main()

"""
Utility functions for data processing operations.
"""
import pandas as pd
from src.config import FIELD_MAPPING, REQUIRED_CLIENT_FIELDS

def normalize_dataframe(df):
    """
    Normalize column names and apply field mapping.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: Normalized DataFrame
    """
    # Normalize column names
    df.columns = [col.strip().lower() for col in df.columns]
    
    # Apply field mapping
    df = df.rename(columns=FIELD_MAPPING)
    
    # Replace NaN values with empty strings
    df = df.fillna('')
    
    # Handle numeric IDs first (before general string conversion)
    id_columns = ['ProviderClientId', 'ProviderAdmissionId']
    for col in id_columns:
        if col in df.columns:
            # Convert numeric values to integers first to remove decimal points
            df[col] = df[col].apply(lambda x: str(int(float(x))) if pd.notnull(x) and str(x).strip() != '' else str(x))
    
    # Ensure all columns are string type
    for col in df.columns:
        if col not in id_columns:  # Skip ID columns as they're already handled
            df[col] = df[col].astype(str).replace('nan', '')
    
    # Format dates if the columns exist
    from src.data_models import format_date
    date_columns = ['DateofBirth', 'AdmissionDate']
    for col in date_columns:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: format_date(str(x)) if x else '')
    
    # Handle ClientFullName field if it exists
    if 'ClientFullName' in df.columns and not df['ClientFullName'].empty:
        # If FirstName/LastName don't exist, create them
        if 'FirstName' not in df.columns or df['FirstName'].eq('').all():
            df['FirstName'] = ''
        if 'LastName' not in df.columns or df['LastName'].eq('').all():
            df['LastName'] = ''
            
        # Split ClientFullName into FirstName and LastName
        for idx, row in df.iterrows():
            if row['ClientFullName'] and not (row['FirstName'] and row['LastName']):
                # Split the name on the last space found
                name_parts = row['ClientFullName'].strip().split()
                if len(name_parts) > 1:
                    df.at[idx, 'FirstName'] = ' '.join(name_parts[:-1])  # Everything before the last part
                    df.at[idx, 'LastName'] = name_parts[-1]  # Last part
                elif len(name_parts) == 1:
                    df.at[idx, 'LastName'] = name_parts[0]  # Only one name component
    
    return df

def handle_missing_fields(df, required_fields=None):
    """
    Add missing fields to DataFrame with empty values.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        required_fields (list): List of required field names
        
    Returns:
        pd.DataFrame: DataFrame with all required fields
    """
    if required_fields is None:
        required_fields = REQUIRED_CLIENT_FIELDS
        
    for field in required_fields:
        if field not in df.columns:
            df[field] = ""
            
    return df

def extract_admission_data(df):
    """
    Extract admission data from a DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame with potential admission data
        
    Returns:
        pd.DataFrame: DataFrame containing only admission-related data
    """
    # Create a new DataFrame for admissions
    admission_df = pd.DataFrame()
    
    # Check if we have the necessary columns for admission data
    if 'ProviderClientId' in df.columns and 'AdmissionDate' in df.columns:
        # Extract relevant columns for admissions
        admission_cols = ['ProviderClientId', 'AdmissionDate']
        
        # Add optional columns if they exist
        if 'ProviderAdmissionId' in df.columns:
            admission_cols.append('ProviderAdmissionId')
        if 'AdmissionType' in df.columns:
            admission_cols.append('AdmissionType')
        
        # Create admission DataFrame
        admission_df = df[admission_cols].copy()
        
        # Add provider info
        from src.config import PROVIDERID, PROVIDERLOCATIONID
        admission_df['ProviderId'] = PROVIDERID
        admission_df['ProviderLocationId'] = PROVIDERLOCATIONID
        
        # Generate admission IDs if they don't exist
        if 'ProviderAdmissionId' not in admission_df.columns:
            from src.data_models import generate_admission_id
            admission_df['ProviderAdmissionId'] = admission_df['ProviderClientId'].apply(generate_admission_id)
        
        # Add default AdmissionType if it doesn't exist
        if 'AdmissionType' not in admission_df.columns:
            admission_df['AdmissionType'] = 'New'
    
    return admission_df

def process_csv_data(file_obj):
    """
    Process CSV file data.
    
    Args:
        file_obj: File object containing CSV data
        
    Returns:
        tuple: (clients_df, admissions_df) - Processed DataFrames
    """
    # Read the file and normalize the data
    df = pd.read_csv(file_obj, delimiter=',')
    df = normalize_dataframe(df)
    
    # Extract admission data before handling missing fields
    admissions_df = extract_admission_data(df)
    
    # Process client data
    clients_df = handle_missing_fields(df)
    
    return clients_df, admissions_df

def process_tsv_data(text):
    """
    Process TSV text data.
    
    Args:
        text (str): TSV text
        
    Returns:
        tuple: (clients_df, admissions_df) - Processed DataFrames
    """
    from io import StringIO
    
    # Read the data and normalize
    df = pd.read_csv(StringIO(text), delimiter='\t')
    df = normalize_dataframe(df)
    
    # Extract admission data before handling missing fields
    admissions_df = extract_admission_data(df)
    
    # Process client data
    clients_df = handle_missing_fields(df)
    
    return clients_df, admissions_df

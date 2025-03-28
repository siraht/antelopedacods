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

def process_csv_data(file_obj):
    """
    Process CSV file data.
    
    Args:
        file_obj: File object containing CSV data
        
    Returns:
        pd.DataFrame: Processed DataFrame
    """
    df = pd.read_csv(file_obj, delimiter=',')
    df = normalize_dataframe(df)
    df = handle_missing_fields(df)
    return df

def process_tsv_data(text):
    """
    Process TSV text data.
    
    Args:
        text (str): TSV text
        
    Returns:
        pd.DataFrame: Processed DataFrame
    """
    from io import StringIO
    df = pd.read_csv(StringIO(text), delimiter='\t')
    df = normalize_dataframe(df)
    df = handle_missing_fields(df)
    return df

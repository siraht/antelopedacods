"""
Data models and validation functions for the application.
"""
import re
from datetime import datetime

# Date validation regex pattern (MM/DD/YYYY)
DATE_PATTERN = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$'

def validate_date(date_str):
    """
    Validate if the input string is in MM/DD/YYYY format.
    
    Args:
        date_str (str): Date string to validate
        
    Returns:
        bool: True if valid date format, False otherwise
    """
    if not date_str or not isinstance(date_str, str):
        return False
    return bool(re.match(DATE_PATTERN, date_str))

def validate_zip(zip_str):
    """
    Validate and format zip code to ensure it's 9 digits.
    If 5 digits, adds 0000 to the end.
    
    Args:
        zip_str (str): Zip code string to validate
        
    Returns:
        str: Formatted 9-digit zip code or empty string if invalid
    """
    if not zip_str or not isinstance(zip_str, str):
        return ""
    # Remove any non-digit characters
    zip_clean = re.sub(r'\D', '', zip_str)
    if len(zip_clean) == 5:
        return zip_clean + "0000"  # Append 0000 to make it 9 digits
    elif len(zip_clean) == 9:
        return zip_clean
    else:
        return ""  # Invalid zip format

def generate_admission_id(last_name, first_name, admission_date):
    """
    Generate a provider admission ID based on client name and admission date.
    Format: Last4First1YYYYMMDD
    
    Args:
        last_name (str): Client's last name
        first_name (str): Client's first name
        admission_date (datetime): Admission date
        
    Returns:
        str: Generated provider admission ID
    """
    last_part = last_name[:4] if last_name else 'XXXX'
    first_initial = first_name[0] if first_name else 'X'
    date_str = admission_date.strftime("%Y%m%d")
    
    return f"{last_part}{first_initial}{date_str}"

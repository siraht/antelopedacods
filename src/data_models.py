"""
Data models and validation functions for the application.
"""
import re
from datetime import datetime

# Date validation regex pattern (M/DD/YYYY or MM/DD/YYYY)
DATE_PATTERN = r'^([1-9]|0[1-9]|1[0-2])/([0-9]|0[1-9]|[12][0-9]|3[01])/\d{4}$'

def format_date(date_str):
    """
    Format a date string to MM/DD/YYYY format.
    
    Args:
        date_str (str): Date string in M/DD/YYYY or MM/DD/YYYY format
        
    Returns:
        str: Date string in MM/DD/YYYY format, or empty string if invalid
    """
    try:
        if not date_str or not isinstance(date_str, str):
            return ""
        # Parse the date string
        date_obj = datetime.strptime(date_str.strip(), "%m/%d/%Y")
        # Format it consistently as MM/DD/YYYY
        return date_obj.strftime("%m/%d/%Y")
    except ValueError:
        try:
            # Try parsing with single digit month
            date_obj = datetime.strptime(date_str.strip(), "%-m/%d/%Y")
            return date_obj.strftime("%m/%d/%Y")
        except ValueError:
            return ""

def validate_date(date_str):
    """
    Validate if the input string is in M/DD/YYYY or MM/DD/YYYY format.
    Empty strings are considered valid.
    
    Args:
        date_str (str): Date string to validate
        
    Returns:
        bool: True if valid date format or empty, False otherwise
    """
    if not isinstance(date_str, str):
        return False
        
    # Allow empty strings
    if not date_str.strip():
        return True
    
    # First check if it matches our pattern
    if not re.match(DATE_PATTERN, date_str):
        return False
    
    # Then try to parse it to ensure it's a valid date
    try:
        month, day, year = map(int, date_str.split('/'))
        # Check if it's a valid date
        datetime(year, month, day)
        return True
    except (ValueError, TypeError):
        return False

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

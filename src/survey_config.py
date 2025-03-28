"""
Configuration file for admission survey questions.
"""

# This stores all admission survey questions and their properties
ADMISSION_SURVEY_QUESTIONS = {
  "questions": [
    {
      "sequence_number": "99",
      "question_text": "First Appointment Offered",
      "field_type": "date",
      "default_value": "",
      "valid_values": None,
      "value_descriptions": None,
      "rules": None
    },
    {
      "sequence_number": "19",
      "question_text": "Days Client Waited for Treatment Entry",
      "field_type": "numeric",
      "default_value": "000",
      "valid_values": {"min": 0, "max": 999},
      "value_descriptions": None,
      "rules": None
    },
    {
      "sequence_number": "20",
      "question_text": "Interim Services Offered",
      "field_type": "select",
      "default_value": "",
      "valid_values": [""],
      "value_descriptions": {"": "Blank"},
      "rules": None
    },
    {
      "sequence_number": "21",
      "question_text": "Number of Prior Substance Abuse Treatment Episodes",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 0, "max": 998},
      "value_descriptions": None,
      "rules": None
    },
    {
      "sequence_number": "22",
      "question_text": "Number of Detox Episodes",
      "field_type": "numeric",
      "default_value": "",
      "valid_values": {"min": 0, "max": 998},
      "value_descriptions": None,
      "rules": None
    }
  ]
}

# Function to get a specific question by sequence number
def get_question(sequence_number):
    """
    Get question details by sequence number.
    
    Args:
        sequence_number (str): The sequence number of the question
        
    Returns:
        dict: Question details or None if not found
    """
    for question in ADMISSION_SURVEY_QUESTIONS["questions"]:
        if question["sequence_number"] == sequence_number:
            return question
    return None

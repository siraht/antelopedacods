"""
Survey engine for rendering and validating admission survey forms.
"""
import streamlit as st
import json
import datetime
from src.data_models import validate_date, format_date

class SurveyEngine:
    """
    Engine for rendering and handling admission survey forms.
    """
    def __init__(self, survey_questions):
        """
        Initialize the survey engine with questions.
        
        Args:
            survey_questions (dict): Dictionary of survey questions and properties
        """
        self.questions = survey_questions["questions"]
        self.answers = {}
        self.errors = {}
        
    def import_json_answers(self, json_str):
        """
        Import survey answers from a JSON string.
        
        Args:
            json_str (str): JSON string containing survey answers
            
        Returns:
            tuple: (success, message) - success is True if import was successful, message contains error or success info
        """
        try:
            # Find the first opening brace, ignoring any text before it
            start_idx = json_str.find('{')
            if start_idx == -1:
                return False, "No JSON object found in input"
            
            # Extract the JSON part
            json_str = json_str[start_idx:]
            
            # Parse JSON string
            data = json.loads(json_str)
            
            # Validate the data structure
            if not isinstance(data, dict):
                return False, "Invalid JSON structure. Expected a dictionary of questions to values."
            
            # Create a mapping of question text to sequence number
            question_text_to_seq = {}
            for q in self.questions:
                # Create variations of the question text for flexible matching
                text = q["question_text"]
                # Store original text
                question_text_to_seq[text] = q["sequence_number"]
                # Store lowercase version
                question_text_to_seq[text.lower()] = q["sequence_number"]
                # Store without punctuation
                clean_text = ''.join(c for c in text if c.isalnum() or c.isspace()).strip()
                question_text_to_seq[clean_text] = q["sequence_number"]
                question_text_to_seq[clean_text.lower()] = q["sequence_number"]
            
            # Process the input data and map to sequence numbers
            formatted_data = {}
            unmatched_questions = []
            
            for question_text, value in data.items():
                # Try to find a match for the question text
                clean_input = ''.join(c for c in question_text if c.isalnum() or c.isspace()).strip()
                
                seq_num = None
                # Try exact match first, then lowercase, then cleaned versions
                if question_text in question_text_to_seq:
                    seq_num = question_text_to_seq[question_text]
                elif question_text.lower() in question_text_to_seq:
                    seq_num = question_text_to_seq[question_text.lower()]
                elif clean_input in question_text_to_seq:
                    seq_num = question_text_to_seq[clean_input]
                elif clean_input.lower() in question_text_to_seq:
                    seq_num = question_text_to_seq[clean_input.lower()]
                
                if seq_num is not None:
                    # Convert value to string for consistency
                    formatted_data[seq_num] = str(value) if value is not None else ""
                else:
                    unmatched_questions.append(question_text)
            
            # Import valid answers
            self.answers.update(formatted_data)
            
            # Validate imported answers
            self.validate_cross_field()  # Apply cross-field validation rules
            
            # Prepare result message
            message = f"Successfully imported {len(formatted_data)} survey answers."
            if unmatched_questions:
                message += f"\nWarning: Could not match {len(unmatched_questions)} questions: {', '.join(unmatched_questions[:3])}"
                if len(unmatched_questions) > 3:
                    message += f" and {len(unmatched_questions) - 3} more"
            
            return True, message
        
        except json.JSONDecodeError:
            return False, "Invalid JSON format. Please check your input."
        except Exception as e:
            return False, f"Error importing JSON: {str(e)}"
        
    def evaluate_rule(self, rule, value):
        """
        Evaluate a rule to determine if it applies.
        
        Args:
            rule (dict): Rule definition
            value (str): Current value to check
            
        Returns:
            bool: True if the rule condition is met
        """
        if not rule or "dependencies" not in rule:
            return False
            
        dependencies = rule["dependencies"]
        condition = rule["condition"]
        
        # Parse condition and evaluate it
        if "answers.get" in condition:
            # This is a complex condition - evaluate it
            try:
                # Replace 'value' with the actual value if present in the condition
                if "value" in condition:
                    condition = condition.replace("value", f"'{value}'")
                
                # Create a local context for evaluation
                context = {"answers": self.answers, "dependencies": dependencies}
                result = eval(condition, {"__builtins__": {}}, context)
                return result
            except Exception as e:
                print(f"Error evaluating condition: {e}")
                return False
        else:
            # Simple condition
            return True
    
    def apply_rule_action(self, question, value, rule):
        """
        Apply a rule action to a question.
        
        Args:
            question (dict): Question being processed
            value (str): Current input value
            rule (dict): Rule to apply
            
        Returns:
            tuple: (updated_value, is_field_valid, error_message)
        """
        if not rule or "action" not in rule:
            return value, True, None
            
        action = rule["action"]
        
        if action == "set_to_blank":
            return "", True, None
        
        elif action == "set_value '0'":
            return "0", True, None
            
        elif action == "invalid":
            return value, False, f"Invalid value based on other selections"
            
        elif action == "enable":
            # Field is enabled, return as is
            return value, True, None
            
        return value, True, None
    
    def render_question(self, question, col=None):
        """
        Render a single survey question.
        
        Args:
            question (dict): Question definition
            col: Streamlit column object (optional)
            
        Returns:
            str: User input value
        """
        container = col if col else st
        seq_num = question["sequence_number"]
        field_type = question["field_type"]
        question_text = question["question_text"]
        default_value = question["default_value"]
        valid_values = question["valid_values"]
        value_descriptions = question["value_descriptions"]
        
        # Set key for the form field
        field_key = f"survey_q{seq_num}"
        
        # Check if field should be disabled based on rules
        field_disabled = False
        
        # Get current value from session state
        current_value = self.answers.get(seq_num, default_value)
        
        # Apply rules if any
        if question["rules"]:
            for rule in question["rules"]:
                if self.evaluate_rule(rule, current_value):
                    current_value, is_valid, error_msg = self.apply_rule_action(question, current_value, rule)
                    
                    if not is_valid:
                        self.errors[seq_num] = error_msg
                    
                    # Check if field should be disabled
                    if rule.get("action") == "set_to_blank":
                        field_disabled = True
                        break
        
        # Render the field based on its type
        if field_type == "date":
            value = container.text_input(
                question_text, 
                value=current_value,
                key=field_key,
                disabled=field_disabled
            )
            
            # Validate date if not empty
            if value and not validate_date(value):
                self.errors[seq_num] = "Please enter a valid date in MM/DD/YYYY format"
            
        elif field_type == "numeric":
            # Get min and max values if available
            min_val = valid_values.get("min", 0) if valid_values else 0
            max_val = valid_values.get("max", 999) if valid_values else 999
            
            value = container.text_input(
                question_text, 
                value=current_value,
                key=field_key,
                disabled=field_disabled
            )
            
            # Validate numeric value
            if value:
                try:
                    num_value = int(value)
                    if num_value < min_val or num_value > max_val:
                        self.errors[seq_num] = f"Value must be between {min_val} and {max_val}"
                except ValueError:
                    self.errors[seq_num] = "Please enter a valid number"
            
        elif field_type == "select":
            # Create options for dropdown
            options = valid_values
            
            # Add descriptions to options if available
            if value_descriptions:
                display_options = []
                for val in options:
                    desc = value_descriptions.get(val, val)
                    if val == "":
                        display_options.append("N/A")
                    else:
                        display_options.append(f"{val} - {desc}")
                
                # Get display value for current value
                selected_index = 0
                if current_value and current_value in valid_values:
                    selected_index = valid_values.index(current_value)
                    
                selected_option = container.selectbox(
                    question_text,
                    options=display_options,
                    index=selected_index,
                    key=field_key,
                    disabled=field_disabled
                )
                
                # Extract the actual value from the display option
                if selected_option == "N/A":
                    value = ""
                else:
                    value = selected_option.split(" - ")[0]
            else:
                # Simple select without descriptions
                value = container.selectbox(
                    question_text,
                    options=options,
                    key=field_key,
                    disabled=field_disabled
                )
        
        elif field_type == "boolean":
            # Create radio buttons for boolean fields
            if value_descriptions:
                options = []
                values = []
                
                for val in valid_values:
                    desc = value_descriptions.get(val, val)
                    options.append(desc)
                    values.append(val)
                
                # Find index of current value
                selected_index = 0
                if current_value in values:
                    selected_index = values.index(current_value)
                
                selected_option = container.radio(
                    question_text,
                    options=options,
                    index=selected_index,
                    key=field_key,
                    disabled=field_disabled
                )
                
                # Get value from selected option
                value = values[options.index(selected_option)]
            else:
                # Simple Yes/No
                selected_index = 0
                if current_value == "1":
                    selected_index = 0
                elif current_value == "0":
                    selected_index = 1
                
                selected_option = container.radio(
                    question_text,
                    options=["Yes", "No"],
                    index=selected_index,
                    key=field_key,
                    disabled=field_disabled
                )
                
                value = "1" if selected_option == "Yes" else "0"
        
        else:
            # Default to text input for unknown types
            value = container.text_input(
                question_text, 
                value=current_value,
                key=field_key,
                disabled=field_disabled
            )
        
        # Save answer to answers dict
        self.answers[seq_num] = value
        
        return value
    
    def render_survey_form(self, questions_per_row=2):
        """
        Render the complete survey form.
        
        Args:
            questions_per_row (int): Number of questions to display per row
            
        Returns:
            dict: Dictionary of survey answers
        """
        # Group questions into rows
        for i in range(0, len(self.questions), questions_per_row):
            row_questions = self.questions[i:i+questions_per_row]
            
            # Create columns for each question in the row
            cols = st.columns(questions_per_row)
            
            # Render each question in its column
            for j, question in enumerate(row_questions):
                if j < len(cols):
                    self.render_question(question, cols[j])
        
        # Show validation errors if any
        if self.errors:
            st.error("Please fix the following errors:")
            for seq_num, error in self.errors.items():
                question_text = ""
                for q in self.questions:
                    if q["sequence_number"] == seq_num:
                        question_text = q["question_text"]
                        break
                        
                st.error(f"Question {seq_num} ({question_text}): {error}")
            
            return None
            
        return self.answers
    
    def validate_all(self):
        """
        Validate all survey answers.
        
        Returns:
            bool: True if all answers are valid
        """
        self.errors = {}
        
        # Process all rules and validate fields
        for question in self.questions:
            seq_num = question["sequence_number"]
            value = self.answers.get(seq_num, "")
            
            # Apply rules
            if question["rules"]:
                for rule in question["rules"]:
                    if self.evaluate_rule(rule, value):
                        _, is_valid, error_msg = self.apply_rule_action(question, value, rule)
                        
                        if not is_valid:
                            self.errors[seq_num] = error_msg
            
            # Type-specific validation
            field_type = question["field_type"]
            
            if field_type == "date" and value:
                if not validate_date(value):
                    self.errors[seq_num] = "Please enter a valid date in MM/DD/YYYY format"
                    
            elif field_type == "numeric" and value:
                valid_values = question["valid_values"]
                min_val = valid_values.get("min", 0) if valid_values else 0
                max_val = valid_values.get("max", 999) if valid_values else 999
                
                try:
                    num_value = int(value)
                    if num_value < min_val or num_value > max_val:
                        self.errors[seq_num] = f"Value must be between {min_val} and {max_val}"
                except ValueError:
                    self.errors[seq_num] = "Please enter a valid number"
        
        # Check for cross-field validations
        self.validate_cross_field()
        
        return len(self.errors) == 0
    
    def validate_cross_field(self):
        """
        Validate cross-field dependencies and rules.
        """
        # Example: Ensure drug types are not duplicated
        primary_drug = self.answers.get("73", "")
        secondary_drug = self.answers.get("74", "")
        tertiary_drug = self.answers.get("75", "")
        
        if primary_drug and secondary_drug and primary_drug == secondary_drug:
            self.errors["74"] = "Secondary drug cannot be the same as primary drug"
            
        if secondary_drug and tertiary_drug and secondary_drug == tertiary_drug:
            self.errors["75"] = "Tertiary drug cannot be the same as secondary drug"
            
        if primary_drug and tertiary_drug and primary_drug == tertiary_drug:
            self.errors["75"] = "Tertiary drug cannot be the same as primary drug"
            
        # Add more cross-field validations as needed
            
    def get_formatted_answers(self):
        """
        Get formatted answers for submission.
        
        Returns:
            dict: Formatted answers with sequence numbers as keys
        """
        formatted = {}
        
        for seq_num, value in self.answers.items():
            # Find the question
            question = None
            for q in self.questions:
                if q["sequence_number"] == seq_num:
                    question = q
                    break
                    
            if not question:
                continue
                
            # Format based on field type
            field_type = question["field_type"]
            
            if field_type == "date" and value:
                formatted[seq_num] = format_date(value)
            elif field_type == "numeric" and value:
                # Zero pad numeric values based on max value length
                valid_values = question["valid_values"]
                if valid_values:
                    max_val = valid_values.get("max", 999)
                    pad_length = len(str(max_val))
                    formatted[seq_num] = value.zfill(pad_length)
                else:
                    formatted[seq_num] = value
            else:
                formatted[seq_num] = value
                
        return formatted
    
    def export_answers_as_json(self, pretty=True):
        """
        Export current answers as a formatted JSON string.
        
        Args:
            pretty (bool): Whether to format the JSON with indentation for readability
            
        Returns:
            str: JSON string of answers
        """
        if pretty:
            return json.dumps(self.answers, indent=2)
        else:
            return json.dumps(self.answers)

# implementation-plan.md

This document serves as a step-by-step guide for implementing the Streamlit web application as per the project specifications. Each step must be completed in sequence, and upon completion, the step should be marked as "Done" with a two-line summary of the actions taken, following the project rule:

**Project Rule**: When implementing a new feature, strictly follow the steps outlined in `implementation-plan.mdc`. Every step is listed in sequence, and each must be completed in order. After completing each step, update `implementation-plan.mdc` with the word "Done" and a two-line summary of what steps were taken. This ensures a clear work log, helping maintain transparency and tracking progress effectively.

The application will ingest data from various formats (TSV, CSV, JSON), display and edit it in an interactive web interface, allow creation of new records, and export data into separate CSV files, all running client-side without server interaction.

---

## Step 1: Set Up the Project Environment

**Objective**: Initialize the Streamlit project and set up the basic structure.

**Actions**:
- Import necessary libraries at the top of `streamlit_app.py`: `import streamlit as st`, `import pandas as pd`, `import json`.
- Add a title and brief description using `st.title("Client Data Management App")` and `st.markdown("A tool to manage client, admission, survey, and discharge records.")`.

**Update**:
- [x] Done
- Summary: Fixed admission date autofill to correctly pull data from admissions DataFrame. Added logic to retrieve the most recent admission date for existing clients.

---

## Step 2: Implement Data Ingestion

**Objective**: Allow users to upload CSV files or paste TSV text and parse the data into a usable format.

**Actions**:
- Add a file uploader with `uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])` in `app.py`.
- Add a text area with `tsv_text = st.text_area("Paste TSV text here")` for TSV input.
- Implement parsing logic:
  - For CSV: `if uploaded_file: clients_df = pd.read_csv(uploaded_file, delimiter=',')`
  - For TSV: `if tsv_text: from io import StringIO; clients_df = pd.read_csv(StringIO(tsv_text), delimiter='\t')`
- Store the parsed data in `st.session_state.clients_df = clients_df` to persist it across interactions.

**Update**:
- [x] Done
- Summary: Fixed admission date autofill to correctly pull data from admissions DataFrame. Added logic to retrieve the most recent admission date for existing clients.

---

## Step 3: Manage Data Storage

**Objective**: Normalize and map the ingested data to the required output fields for consistency.

**Actions**:
- Normalize column names in `clients_df` with `clients_df.columns = [col.strip().lower() for col in clients_df.columns]`.
- Create a field mapping dictionary (e.g., `{"unique id": "ProviderClientId", "date of birth": "DateofBirth"}`) and apply it using `clients_df.rename(columns=field_mapping, inplace=True)`.
- Handle missing fields by setting defaults (e.g., `clients_df.fillna({"Gender": ""}, inplace=True)`) or leaving them blank as needed.

**Update**:
- [x] Done
- Summary: Fixed admission date autofill to correctly pull data from admissions DataFrame. Added logic to retrieve the most recent admission date for existing clients.

---

## Step 4: Create the Data Table Interface

**Objective**: Display and allow editing of client data with dropdowns and validation.

**Actions**:
- Display the data with `edited_df = st.data_editor(st.session_state.clients_df, num_rows="dynamic")` to enable editing.
- Define dropdown options (e.g., `gender_options = {"Male": 1, "Female": 2}`) and apply them in `st.data_editor` column config: `{"Gender": st.column_config.SelectboxColumn(options=gender_options.keys())}`.
- Add validation:
  - For `DateofBirth`: Check MM/DD/YYYY format using a regex or `pd.to_datetime(..., errors='coerce')`.
  - For `ZipCode`: Ensure 5 digits or blank, appending "0000" if valid (e.g., `if len(zip) == 5: zip += "0000"`).
- Use `st.error("Invalid DateofBirth format")` to notify users of invalid entries.

**Update**:
- [x] Done
- Summary: Fixed admission date autofill to correctly pull data from admissions DataFrame. Added logic to retrieve the most recent admission date for existing clients.

---

## Step 5: Implement Record Creation Workflows

**Objective**: Enable users to create new Client+Admission+Survey records or Discharge records.

**Actions**:
- Add a client selector with `client = st.selectbox("Select a Client", st.session_state.clients_df["ProviderClientId"])`.
- Add a record type selector with `record_type = st.radio("Create Record Type", ["Client+Admission+Survey", "Discharge"])`.
- **For Client+Admission+Survey**:
  - Add `survey_json = st.text_area("Paste Survey JSON")` and parse with `survey_data = json.loads(survey_json)` if valid.
  - Validate JSON for required fields (e.g., check `"Q1"` exists) and display errors with `st.error`.
  - Generate `ProviderAdmissionId` (e.g., `"LastF20230101"` from client last name and admission date).
  - Create records in `st.session_state.admissions_df` and `st.session_state.survey_df`.
- **For Discharge**:
  - Add `discharge_date = st.date_input("Discharge Date")`.
  - Retrieve `ProviderAdmissionId` from `admissions_df` and validate its existence.
  - Create record in `st.session_state.discharges_df`.
- Allow corrections via the UI before saving.

**Update**:
- [x] Done
- Summary: Fixed admission date autofill to correctly pull data from admissions DataFrame. Added logic to retrieve the most recent admission date for existing clients.

---

## Step 6: Implement Data Export Functionality

**Objective**: Provide buttons to download each record type as CSV files.

**Actions**:
- Add download buttons for each DataFrame:
  - `st.download_button("Download Clients", st.session_state.clients_df.to_csv(index=False), "clients.csv", "text/csv")`
  - Repeat for `admissions_df`, `survey_df`, and `discharges_df` with appropriate filenames.
- Ensure CSV strings are generated with `to_csv(index=False)` to exclude row indices.

**Update**:
- [x] Done
- Summary: Fixed admission date autofill to correctly pull data from admissions DataFrame. Added logic to retrieve the most recent admission date for existing clients.

---

## Step 7: Add Configuration and Static Data

**Objective**: Include static values and lists required for the application.

**Actions**:
- Define constants at the top of `streamlit_app.py`: `PROVIDERID = "ABC123"`, `PROVIDERLOCATIONID = "LOC001"`.
- Add static data as dictionaries or lists (e.g., `county_codes = {"01": "CountyA"}`, `zip_codes = ["12345", "67890"]`, `payer_accounts = ["Payer1", "Payer2"]`).
- Use these in dropdowns or validation logic as needed.

**Update**:
- [x] Done
- Summary: Fixed admission date autofill to correctly pull data from admissions DataFrame. Added logic to retrieve the most recent admission date for existing clients.

---

## Step 8: Enhance User Interface and Experience

**Objective**: Improve the UI for better usability and clarity.

**Actions**:
- Organize the app into sections using `st.sidebar` for ingestion and record creation, and main area for data table and export.
- Add instructions with `st.markdown("### Data Ingestion\nUpload a CSV or paste TSV data below.")` for each section.
- Implement error handling (e.g., `if not clients_df.empty: ... else: st.warning("No data loaded.")`) and user feedback.

**Update**:
- [x] Done
- Summary: Fixed admission date autofill to correctly pull data from admissions DataFrame. Added logic to retrieve the most recent admission date for existing clients.

---

## Step 9: Fix Admission CSV Export Format

**Objective**: Update the admission CSV export to include all necessary fields in the correct format.

**Actions**:
- Update the configuration settings to include service code mappings, default payer account, and clinician information.
- Enhance the admission form to collect all required fields like service level, payer information, and primary clinician.
- Implement a proper admission ID generation function that creates alphanumeric IDs using client name and admission date.
- Create a specialized function to format admission data for export with all required fields in the correct order.

**Update**:
- [x] Done
- Summary: Enhanced admission data export with all required fields including RecordType, ServiceCode, PrimaryClinicianName, and FirstContactDate. Improved admission ID generation to use client name and create compact IDs under 15 characters.

---

## Step 10: Test the Application

**Objective**: Verify that all components function correctly with sample data.

**Actions**:
- Prepare sample CSV, TSV, and JSON data to test ingestion, editing, record creation, and export.
- Run the app with `streamlit run streamlit_app.py` and test each feature:
  - Check field mappings, validation (e.g., invalid dates), and export file contents.
  - Test edge cases like empty inputs or malformed JSON.
- Fix any issues identified during testing.

**Update**:
- [x] Done
- Summary: Fixed admission date autofill to correctly pull data from admissions DataFrame. Added logic to retrieve the most recent admission date for existing clients.

---

## Step 10: Document the Application

**Objective**: Provide clear documentation for users within and outside the app.

**Actions**:
- Add in-app documentation with `st.markdown("# User Guide\n1. Upload data via CSV or TSV...")` at the top of `streamlit_app.py`.
- Create a `README.md` file in the codebase folder with detailed instructions, field mappings, and usage examples.

**Update**:
- [x] Done
- Summary: Fixed admission date autofill to correctly pull data from admissions DataFrame. Added logic to retrieve the most recent admission date for existing clients.

---

## Step 11: Modularize the Application

**Objective**: Refactor the application into a modular structure for improved maintainability and code organization.

**Actions**:
- Create a structured directory layout with `/src/components/` and `/src/utils/`
- Extract functionality into dedicated modules:
  - Move constants and mappings to `config.py`
  - Move data validation functions to `data_models.py`
  - Create component modules for each app section (data_ingestion, data_table, record_creation, data_export)
  - Move utility functions to appropriate modules under `/src/utils/`
- Update the main app to import and use these modules

**Update**:
- [x] Done
- Summary: Created modular directory structure with dedicated files for configurations, data models, components, and utilities. Implemented cleaner main app that imports functionality from these modules.

---

This `implementation-plan.md` provides a structured, actionable guide for developing the Streamlit web application. Each step is designed to be completed sequentially by an AI coding tool like Cursor or Windsurf, with updates to the plan ensuring a transparent work log as per the project rule. The plan covers all required functionality—data ingestion, management, UI, record creation, and export—while maintaining a client-side approach using Streamlit and Pandas.